import os
import socket
from collections.abc import Generator
from typing import TypeVar
from urllib.parse import urljoin

import httpx
import pytest
from pydantic import TypeAdapter
from pydantic import ValidationError
from typing_extensions import TypeIs

from jenkins_typed.types import JenkinsFolderInfo
from jenkins_typed.types import JenkinsRoot
from jenkins_typed.types import JenkinsWorkflowJobInfo
from tests.jenkins_container import JenkinsContainer
from tests.jenkins_container import JenkinsInfo

T = TypeVar("T")

VOLUME_MOUNT = os.path.realpath("./ignore/jenkins_home")
VOLUME_MOUNT_EXISTED = os.path.isdir(VOLUME_MOUNT)


def jenkins_setup(info: JenkinsInfo) -> None:
    if os.path.exists(os.path.join(VOLUME_MOUNT, "jenkins.model.JenkinsLocationConfiguration.xml")):
        # NOTE: Find a way to check for this with a http request
        return
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(info.base_url)
        page.get_by_label("Administrator password").fill(info.password)
        page.get_by_role("button").click()
        page.locator("a.install-recommended").click()
        page.locator("button.skip-first-user").click(timeout=100_000)
        page.locator("button.save-configure-instance").click()
        page.locator("button.install-done").click()
        browser.close()


def get_existing_jenkins() -> JenkinsInfo | None:
    password_file = os.path.join(VOLUME_MOUNT, "secrets/initialAdminPassword")
    if not os.path.isfile(password_file):
        return None
    with open(password_file) as f:
        password = f.read().strip()

    default_port = JenkinsContainer.JENKINS_PORT
    host = "127.0.0.1"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        if s.connect_ex((host, default_port)) != 0:
            return None
    return JenkinsInfo(f"http://{host}:{default_port}", "admin", password)


@pytest.fixture(scope="session")
def jenkins_info() -> Generator[JenkinsInfo]:
    existing_jenkins = get_existing_jenkins()
    if existing_jenkins:
        jenkins_setup(existing_jenkins)
        yield existing_jenkins
        return
    os.makedirs(VOLUME_MOUNT, exist_ok=True)
    with JenkinsContainer(volumes=[(VOLUME_MOUNT, "/var/jenkins_home", "rw")]) as jenkins:
        info = jenkins.get_triple()
        jenkins_setup(info)
        yield info


@pytest.fixture(scope="session")
def jenkins_http_client(jenkins_info: JenkinsInfo) -> httpx.Client:
    return httpx.Client(
        base_url=jenkins_info.base_url, auth=(jenkins_info.username, jenkins_info.password)
    )


def test_bar(jenkins_http_client: httpx.Client) -> None:
    assert jenkins_http_client.base_url
    assert 1 == 2


# @pytest.mark.parametrize(
#     ("url", "_type"),
#     [
#         ("http://localhost:8080", JenkinsRoot),
#         ("http://localhost:8080/job/primary/", JenkinsFolderInfo),
#         ("http://localhost:8080/job/primary/job/ba/", JenkinsFolderInfo),
#         (
#             "http://localhost:8080/job/primary/job/ba/job/o/",
#             JenkinsWorkflowJobInfo,
#         ),
#         (
#             "http://localhost:8080/job/primary/job/ba/job/project/",
#             JenkinsWorkflowJobInfo,
#         ),
#         (
#             "http://localhost:8080/job/primary/job/ba/job/project/1/",
#             JenkinsWorkflowRunInfo,
#         ),
#         ("http://localhost:8080/job/test/", JenkinsWorkflowJobInfo),
#         ("http://localhost:8080/job/test/12/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/11/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/10/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/9/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/8/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/7/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/6/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/5/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/4/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/3/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/2/", JenkinsWorkflowRunInfo),
#         ("http://localhost:8080/job/test/1/", JenkinsWorkflowRunInfo),
#     ],
# )
# def test_typed_dict(url: str, _type: type) -> None:
#     response = client.get(f"{url}/api/json")
#     obj = response.json()
#     strict_validate(obj, _type)


def strict_validate(obj: object, _type: type[T]) -> T:
    return TypeAdapter(_type).validate_python(obj, strict=True, extra="forbid")


def is_type(obj: object, _type: type[T]) -> TypeIs[T]:
    try:
        strict_validate(obj, _type)
    except ValidationError as _:
        return False
    else:
        return True


if __name__ == "__main__":

    def recurse(url: str) -> None:
        print(f'("{url}", ', end="")
        response = client.get(urljoin(url, "api/json"))
        response.raise_for_status()
        item = response.json()
        if is_type(item, JenkinsWorkflowRunInfo):
            print("OrgJenkinsciPluginsWorkflowJobWorkflowRunDetail)")

        elif is_type(item, JenkinsWorkflowJobInfo):
            print("OrgJenkinsciPluginsWorkflowJobWorkflowJobDetail)")
            for j in item["builds"]:
                recurse(j["url"])

        elif is_type(item, JenkinsFolderInfo):
            print("ComCloudbeesHudsonPluginsFolderFolderDetail)")
            for j in item["jobs"]:
                recurse(j["url"])

        elif is_type(item, JenkinsRoot):
            print("HudsonModelHudson)")
            for j in item["jobs"]:
                recurse(j["url"])
        else:
            type_dict = {"com.cloudbees.hudson.plugins.folder.Folder": JenkinsFolderInfo}
            _type = type_dict[item["_class"]]
            strict_validate(item, _type)

    recurse(JENKINS_BASE_URL)
