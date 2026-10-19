# flake8: noqa: PLR2004
from __future__ import annotations

from typing import TYPE_CHECKING

from typing_extensions import TypeIs

if TYPE_CHECKING:
    from jenkins_typed.types import JenkinsFolder
    from jenkins_typed.types import JenkinsFolderInfo
    from jenkins_typed.types import JenkinsListViewInfo
    from jenkins_typed.types import JenkinsRoot
    from jenkins_typed.types import JenkinsWorkflowJob
    from jenkins_typed.types import JenkinsWorkflowJobInfo
    from jenkins_typed.types import JenkinsWorkflowRun
    from jenkins_typed.types import JenkinsWorkflowRunInfo


def is_jenkins_folder(
    obj: object,
) -> TypeIs[JenkinsFolder]:
    return (
        isinstance(obj, dict) and obj.get("_class") == "com.cloudbees.hudson.plugins.folder.Folder"
    )


def is_jenkins_workflow_job(
    obj: object,
) -> TypeIs[JenkinsWorkflowJob]:
    return (
        isinstance(obj, dict)
        and obj.get("_class") == "org.jenkinsci.plugins.workflow.job.WorkflowJob"
    )


def is_jekins_root(obj: object) -> TypeIs[JenkinsRoot]:
    return isinstance(obj, dict) and obj.get("_class") == "hudson.model.Hudson"


def is_jenkins_folder_info(
    obj: object,
) -> TypeIs[JenkinsFolderInfo]:
    return (
        isinstance(obj, dict)
        and obj.get("_class") == "com.cloudbees.hudson.plugins.folder.Folder"
        and len(obj) > 4
    )


def is_jenkins_workflow_run(
    obj: object,
) -> TypeIs[JenkinsWorkflowRun]:
    return (
        isinstance(obj, dict)
        and obj.get("_class") == "org.jenkinsci.plugins.workflow.job.WorkflowRun"
    )


def is_jenkins_workflow_job_info(
    obj: object,
) -> TypeIs[JenkinsWorkflowJobInfo]:
    return (
        isinstance(obj, dict)
        and obj.get("_class") == "org.jenkinsci.plugins.workflow.job.WorkflowJob"
        and len(obj) > 4
    )


def is_jenkins_workflow_run_info(
    obj: object,
) -> TypeIs[JenkinsWorkflowRunInfo]:
    return (
        isinstance(obj, dict)
        and obj.get("_class") == "org.jenkinsci.plugins.workflow.job.WorkflowRun"
        and len(obj) > 4
    )


def is_jenkins_list_view_info(
    obj: object,
) -> TypeIs[JenkinsListViewInfo]:
    return isinstance(obj, dict) and obj.get("_class") == "hudson.model.ListView" and len(obj) > 4
