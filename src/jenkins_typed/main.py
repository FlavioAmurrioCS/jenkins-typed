from __future__ import annotations

from typing import TYPE_CHECKING
from typing import NamedTuple
from urllib.parse import urljoin

from jenkins_typed.type_utils import is_jekins_root
from jenkins_typed.type_utils import is_jenkins_folder_info
from jenkins_typed.type_utils import is_jenkins_list_view_info
from jenkins_typed.type_utils import is_jenkins_workflow_job

if TYPE_CHECKING:
    from collections.abc import Generator

    import httpx

    from jenkins_typed.types import JenkinsFolderInfo
    from jenkins_typed.types import JenkinsRoot
    from jenkins_typed.types import JenkinsWorkflowJobInfo


class JenkinsClient(NamedTuple):
    client: httpx.Client

    def api_json(self, *args: str) -> JenkinsRoot | JenkinsFolderInfo | JenkinsWorkflowJobInfo:
        url = ""
        for p in args:
            url += f"/job/{p}"

        response = self.client.get(f"{url}/api/json")
        response.raise_for_status()
        return response.json()

    def get_jenkins_job_urls(self, path: str = "/") -> Generator[str]:
        yield from self._get_jenkins_job_urls_helper(path=path, seen=set())

    def _get_jenkins_job_urls_helper(self, path: str, seen: set[str]) -> Generator[str]:  # noqa: C901
        response = self.client.get(urljoin(path, "api/json"))
        response.raise_for_status()
        item = response.json()
        if is_jekins_root(item) or is_jenkins_folder_info(item):
            for job in item["jobs"]:
                job_url = job["url"]
                if is_jenkins_workflow_job(job):
                    if job_url in seen:
                        continue
                    seen.add(job_url)
                    yield job_url
                else:
                    yield from self._get_jenkins_job_urls_helper(job["url"], seen)
            for view in item["views"]:
                if view["url"] == item["primaryView"]["url"]:
                    continue
                yield from self._get_jenkins_job_urls_helper(view["url"], seen)
        elif is_jenkins_list_view_info(item):
            for job in item["jobs"]:
                job_url = job["url"]
                if is_jenkins_workflow_job(job):
                    if job_url in seen:
                        continue
                    seen.add(job_url)
                    yield job_url
                else:
                    msg = "Views Should Only Contain JenkinsWorkflowJob"
                    raise ValueError(msg)


if __name__ == "__main__":
    import os

    import httpx

    JENKINS_USERNAME = os.environ["JENKINS_USERNAME"]
    JENKINS_PASSWORD = os.environ["JENKINS_PASSWORD"]
    JENKINS_BASE_URL = os.environ["JENKINS_BASE_URL"]
    client = httpx.Client(base_url=JENKINS_BASE_URL, auth=(JENKINS_USERNAME, JENKINS_PASSWORD))
    jclient = JenkinsClient(client)

    response = jclient.api_json()

    # print(json.dumps(response, indent=2))
    for i in jclient.get_jenkins_job_urls():
        print(i)
