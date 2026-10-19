from typing import Any
from typing import Literal

from typing_extensions import NotRequired
from typing_extensions import TypedDict


class JenkinsFolder(TypedDict):
    _class: Literal["com.cloudbees.hudson.plugins.folder.Folder"]
    name: str
    url: str


class JenkinsWorkflowJob(TypedDict):
    _class: Literal["org.jenkinsci.plugins.workflow.job.WorkflowJob"]
    name: str
    url: str
    color: NotRequired[str]


class JenkinsModelUnlabeledLoadStatistics(TypedDict):
    _class: Literal["jenkins.model.UnlabeledLoadStatistics"]


class HudsonModelAllView(TypedDict):
    _class: Literal["hudson.model.AllView"]
    name: str
    url: str


class JenkinsListView(TypedDict):
    _class: Literal["hudson.model.ListView"]
    name: str
    url: str


class JenkinsListViewInfo(JenkinsListView):
    # _class: Literal["hudson.model.ListView"]
    description: None
    jobs: list[JenkinsWorkflowJob]
    # name: str
    property: list
    # url: str


o: JenkinsListViewInfo = {
    "_class": "hudson.model.ListView",
    "description": None,
    "jobs": [
        {
            "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
            "name": "pr-1",
            "url": "http://localhost:8080/job/primary/job/ba/job/pr-1/",
            "color": "disabled",
        }
    ],
    "name": "PR",
    "property": [],
    "url": "http://localhost:8080/job/primary/job/ba/view/PR/",
}


class JenkinsRoot(TypedDict):
    _class: Literal["hudson.model.Hudson"]
    assignedLabels: list[dict[str, str]]
    mode: str
    nodeDescription: str
    nodeName: str
    numExecutors: int
    description: None
    jobs: list[JenkinsFolder | JenkinsWorkflowJob]
    overallLoad: dict
    primaryView: HudsonModelAllView
    quietDownReason: None
    quietingDown: bool
    slaveAgentPort: int
    unlabeledLoad: JenkinsModelUnlabeledLoadStatistics
    url: str
    useCrumbs: bool
    useSecurity: bool
    views: list[HudsonModelAllView]


class JenkinsFolderInfo(JenkinsFolder):
    # _class: Literal["com.cloudbees.hudson.plugins.folder.Folder"]
    actions: list[dict[str, str]]
    description: str
    displayName: str
    displayNameOrNull: None
    fullDisplayName: str
    fullName: str
    # name: str
    # url: str
    healthReport: list[str]
    jobs: list[JenkinsFolder | JenkinsWorkflowJob]
    primaryView: HudsonModelAllView
    views: list[HudsonModelAllView | JenkinsListView]


class JenkinsWorkflowRun(TypedDict):
    _class: Literal["org.jenkinsci.plugins.workflow.job.WorkflowRun"]
    number: int
    url: str


class HealthReport(TypedDict):
    description: str
    iconClassName: str
    iconUrl: str
    score: int


class JenkinsQueueBlockedJob(TypedDict):
    _class: Literal["hudson.model.Queue$BlockedItem"]
    blocked: bool
    buildable: bool
    id: int
    inQueueSince: int
    params: str
    stuck: bool
    task: JenkinsWorkflowJob
    url: str
    why: str
    buildableStartMilliseconds: int


class JenkinsWorkflowJobInfo(JenkinsWorkflowJob):
    # _class: Literal["org.jenkinsci.plugins.workflow.job.WorkflowJob"]
    actions: list[dict[str, str]]
    description: str
    displayName: str
    displayNameOrNull: None
    fullDisplayName: str
    fullName: str
    # name: str
    # url: str
    buildable: bool
    builds: list[JenkinsWorkflowRun]
    # color: str
    firstBuild: JenkinsWorkflowRun | None
    healthReport: list[HealthReport]
    keepDependencies: bool
    lastBuild: JenkinsWorkflowRun | None
    lastCompletedBuild: JenkinsWorkflowRun | None
    lastFailedBuild: JenkinsWorkflowRun | None
    lastStableBuild: JenkinsWorkflowRun | None
    lastSuccessfulBuild: JenkinsWorkflowRun | None
    lastUnstableBuild: JenkinsWorkflowRun | None
    lastUnsuccessfulBuild: JenkinsWorkflowRun | None
    nextBuildNumber: int
    property: list
    concurrentBuild: bool
    disabled: bool
    inQueue: bool
    queueItem: JenkinsQueueBlockedJob | None
    resumeBlocked: bool


class Build(TypedDict):
    number: int
    url: str


class JenkinsWorkflowRunInfo(JenkinsWorkflowRun):
    # _class: Literal["org.jenkinsci.plugins.workflow.job.WorkflowRun"]
    actions: list[dict[str, Any]]
    artifacts: list[str]
    building: bool
    description: None
    displayName: str
    duration: int
    estimatedDuration: int
    executor: None
    fullDisplayName: str
    id: str
    keepLog: bool
    # number: int
    queueId: int
    result: str
    timestamp: int
    # url: str
    changeSets: list[str]
    culprits: list[str]
    inProgress: bool
    nextBuild: Build | None
    previousBuild: Build | None


if __name__ == "__main__":
    e: JenkinsRoot = {
        "_class": "hudson.model.Hudson",
        "assignedLabels": [{"name": "built-in"}],
        "mode": "NORMAL",
        "nodeDescription": "the Jenkins controller's built-in node",
        "nodeName": "",
        "numExecutors": 2,
        "description": None,
        "jobs": [
            {
                "_class": "com.cloudbees.hudson.plugins.folder.Folder",
                "name": "primary",
                "url": "http://localhost:8080/job/primary/",
            },
            {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
                "name": "test",
                "url": "http://localhost:8080/job/test/",
                "color": "blue",
            },
        ],
        "overallLoad": {},
        "primaryView": {
            "_class": "hudson.model.AllView",
            "name": "all",
            "url": "http://localhost:8080/",
        },
        "quietDownReason": None,
        "quietingDown": False,
        "slaveAgentPort": 50000,
        "unlabeledLoad": {"_class": "jenkins.model.UnlabeledLoadStatistics"},
        "url": "http://localhost:8080/",
        "useCrumbs": True,
        "useSecurity": True,
        "views": [
            {
                "_class": "hudson.model.AllView",
                "name": "all",
                "url": "http://localhost:8080/",
            }
        ],
    }

    e2: list[JenkinsFolderInfo] = [
        {
            "_class": "com.cloudbees.hudson.plugins.folder.Folder",
            "actions": [
                {},
                {},
                {"_class": "com.cloudbees.plugins.credentials.ViewCredentialsAction"},
            ],
            "description": "",
            "displayName": "primary",
            "displayNameOrNull": None,
            "fullDisplayName": "primary",
            "fullName": "primary",
            "name": "primary",
            "url": "http://localhost:8080/job/primary/",
            "healthReport": [],
            "jobs": [
                {
                    "_class": "com.cloudbees.hudson.plugins.folder.Folder",
                    "name": "ba",
                    "url": "http://localhost:8080/job/primary/job/ba/",
                }
            ],
            "primaryView": {
                "_class": "hudson.model.AllView",
                "name": "All",
                "url": "http://localhost:8080/job/primary/",
            },
            "views": [
                {
                    "_class": "hudson.model.AllView",
                    "name": "All",
                    "url": "http://localhost:8080/job/primary/",
                }
            ],
        },
        {
            "_class": "com.cloudbees.hudson.plugins.folder.Folder",
            "actions": [
                {},
                {},
                {"_class": "com.cloudbees.plugins.credentials.ViewCredentialsAction"},
            ],
            "description": "",
            "displayName": "ba",
            "displayNameOrNull": None,
            "fullDisplayName": "primary \u00bb ba",
            "fullName": "primary/ba",
            "name": "ba",
            "url": "http://localhost:8080/job/primary/job/ba/",
            "healthReport": [],
            "jobs": [
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
                    "name": "project",
                    "url": "http://localhost:8080/job/primary/job/ba/job/project/",
                    "color": "blue",
                }
            ],
            "primaryView": {
                "_class": "hudson.model.AllView",
                "name": "All",
                "url": "http://localhost:8080/job/primary/job/ba/",
            },
            "views": [
                {
                    "_class": "hudson.model.AllView",
                    "name": "All",
                    "url": "http://localhost:8080/job/primary/job/ba/",
                }
            ],
        },
        {
            "_class": "com.cloudbees.hudson.plugins.folder.Folder",
            "actions": [
                {},
                {},
                {"_class": "com.cloudbees.plugins.credentials.ViewCredentialsAction"},
            ],
            "description": "",
            "displayName": "ba",
            "displayNameOrNull": None,
            "fullDisplayName": "primary \u00bb ba",
            "fullName": "primary/ba",
            "name": "ba",
            "url": "http://localhost:8080/job/primary/job/ba/",
            "healthReport": [],
            "jobs": [
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
                    "name": "project",
                    "url": "http://localhost:8080/job/primary/job/ba/job/project/",
                    "color": "blue",
                }
            ],
            "primaryView": {
                "_class": "hudson.model.AllView",
                "name": "All",
                "url": "http://localhost:8080/job/primary/job/ba/",
            },
            "views": [
                {
                    "_class": "hudson.model.AllView",
                    "name": "All",
                    "url": "http://localhost:8080/job/primary/job/ba/",
                }
            ],
        },
    ]

    e3: list[JenkinsWorkflowJobInfo] = [
        {
            "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
            "actions": [
                {},
                {},
                {},
                {},
                {},
                {},
                {"_class": "org.jenkinsci.plugins.displayurlapi.actions.JobDisplayAction"},
                {},
                {},
                {"_class": "com.cloudbees.plugins.credentials.ViewCredentialsAction"},
            ],
            "description": "",
            "displayName": "test",
            "displayNameOrNull": None,
            "fullDisplayName": "test",
            "fullName": "test",
            "name": "test",
            "url": "http://localhost:8080/job/test/",
            "buildable": True,
            "builds": [
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 7,
                    "url": "http://localhost:8080/job/test/7/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 6,
                    "url": "http://localhost:8080/job/test/6/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 5,
                    "url": "http://localhost:8080/job/test/5/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 4,
                    "url": "http://localhost:8080/job/test/4/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 3,
                    "url": "http://localhost:8080/job/test/3/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 2,
                    "url": "http://localhost:8080/job/test/2/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 1,
                    "url": "http://localhost:8080/job/test/1/",
                },
            ],
            "color": "blue",
            "firstBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 1,
                "url": "http://localhost:8080/job/test/1/",
            },
            "healthReport": [
                {
                    "description": "Build stability: 2 out of the last 5 builds failed.",
                    "iconClassName": "icon-health-40to59",
                    "iconUrl": "health-40to59.png",
                    "score": 60,
                }
            ],
            "keepDependencies": False,
            "lastBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 7,
                "url": "http://localhost:8080/job/test/7/",
            },
            "lastCompletedBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 7,
                "url": "http://localhost:8080/job/test/7/",
            },
            "lastFailedBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 4,
                "url": "http://localhost:8080/job/test/4/",
            },
            "lastStableBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 7,
                "url": "http://localhost:8080/job/test/7/",
            },
            "lastSuccessfulBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 7,
                "url": "http://localhost:8080/job/test/7/",
            },
            "lastUnstableBuild": None,
            "lastUnsuccessfulBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 4,
                "url": "http://localhost:8080/job/test/4/",
            },
            "nextBuildNumber": 8,
            "property": [],
            "concurrentBuild": True,
            "disabled": False,
            "inQueue": False,
            "queueItem": None,
            "resumeBlocked": False,
        },
        {
            "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
            "actions": [
                {},
                {},
                {},
                {},
                {"_class": "org.jenkinsci.plugins.displayurlapi.actions.JobDisplayAction"},
                {},
                {},
                {"_class": "com.cloudbees.plugins.credentials.ViewCredentialsAction"},
            ],
            "description": "",
            "displayName": "project",
            "displayNameOrNull": None,
            "fullDisplayName": "primary \u00bb ba \u00bb project",
            "fullName": "primary/ba/project",
            "name": "project",
            "url": "http://localhost:8080/job/primary/job/ba/job/project/",
            "buildable": True,
            "builds": [
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 1,
                    "url": "http://localhost:8080/job/primary/job/ba/job/project/1/",
                }
            ],
            "color": "blue",
            "firstBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 1,
                "url": "http://localhost:8080/job/primary/job/ba/job/project/1/",
            },
            "healthReport": [
                {
                    "description": "Build stability: No recent builds failed.",
                    "iconClassName": "icon-health-80plus",
                    "iconUrl": "health-80plus.png",
                    "score": 100,
                }
            ],
            "keepDependencies": False,
            "lastBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 1,
                "url": "http://localhost:8080/job/primary/job/ba/job/project/1/",
            },
            "lastCompletedBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 1,
                "url": "http://localhost:8080/job/primary/job/ba/job/project/1/",
            },
            "lastFailedBuild": None,
            "lastStableBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 1,
                "url": "http://localhost:8080/job/primary/job/ba/job/project/1/",
            },
            "lastSuccessfulBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 1,
                "url": "http://localhost:8080/job/primary/job/ba/job/project/1/",
            },
            "lastUnstableBuild": None,
            "lastUnsuccessfulBuild": None,
            "nextBuildNumber": 2,
            "property": [],
            "concurrentBuild": True,
            "disabled": False,
            "inQueue": False,
            "queueItem": None,
            "resumeBlocked": False,
        },
        {
            "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
            "actions": [
                {},
                {},
                {},
                {},
                {"_class": "org.jenkinsci.plugins.displayurlapi.actions.JobDisplayAction"},
                {},
                {},
                {"_class": "com.cloudbees.plugins.credentials.ViewCredentialsAction"},
            ],
            "description": "",
            "displayName": "o",
            "displayNameOrNull": None,
            "fullDisplayName": "primary » ba » o",
            "fullName": "primary/ba/o",
            "name": "o",
            "url": "http://localhost:8080/job/primary/job/ba/job/o/",
            "buildable": True,
            "builds": [],
            "color": "notbuilt",
            "firstBuild": None,
            "healthReport": [],
            "keepDependencies": False,
            "lastBuild": None,
            "lastCompletedBuild": None,
            "lastFailedBuild": None,
            "lastStableBuild": None,
            "lastSuccessfulBuild": None,
            "lastUnstableBuild": None,
            "lastUnsuccessfulBuild": None,
            "nextBuildNumber": 1,
            "property": [],
            "concurrentBuild": True,
            "disabled": False,
            "inQueue": False,
            "queueItem": None,
            "resumeBlocked": False,
        },
        {
            "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
            "actions": [
                {},
                {},
                {},
                {},
                {},
                {},
                {"_class": "org.jenkinsci.plugins.displayurlapi.actions.JobDisplayAction"},
                {},
                {},
                {"_class": "com.cloudbees.plugins.credentials.ViewCredentialsAction"},
            ],
            "description": "",
            "displayName": "test",
            "displayNameOrNull": None,
            "fullDisplayName": "test",
            "fullName": "test",
            "name": "test",
            "url": "http://localhost:8080/job/test/",
            "buildable": True,
            "builds": [
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 10,
                    "url": "http://localhost:8080/job/test/10/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 9,
                    "url": "http://localhost:8080/job/test/9/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 8,
                    "url": "http://localhost:8080/job/test/8/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 7,
                    "url": "http://localhost:8080/job/test/7/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 6,
                    "url": "http://localhost:8080/job/test/6/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 5,
                    "url": "http://localhost:8080/job/test/5/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 4,
                    "url": "http://localhost:8080/job/test/4/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 3,
                    "url": "http://localhost:8080/job/test/3/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 2,
                    "url": "http://localhost:8080/job/test/2/",
                },
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                    "number": 1,
                    "url": "http://localhost:8080/job/test/1/",
                },
            ],
            "color": "blue_anime",
            "firstBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 1,
                "url": "http://localhost:8080/job/test/1/",
            },
            "healthReport": [
                {
                    "description": "Build stability: No recent builds failed.",
                    "iconClassName": "icon-health-80plus",
                    "iconUrl": "health-80plus.png",
                    "score": 100,
                }
            ],
            "keepDependencies": False,
            "lastBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 10,
                "url": "http://localhost:8080/job/test/10/",
            },
            "lastCompletedBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 7,
                "url": "http://localhost:8080/job/test/7/",
            },
            "lastFailedBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 4,
                "url": "http://localhost:8080/job/test/4/",
            },
            "lastStableBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 7,
                "url": "http://localhost:8080/job/test/7/",
            },
            "lastSuccessfulBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 7,
                "url": "http://localhost:8080/job/test/7/",
            },
            "lastUnstableBuild": None,
            "lastUnsuccessfulBuild": {
                "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
                "number": 4,
                "url": "http://localhost:8080/job/test/4/",
            },
            "nextBuildNumber": 11,
            "property": [
                {
                    "_class": "org.jenkinsci.plugins.workflow.job.properties.DisableConcurrentBuildsJobProperty"
                }
            ],
            "concurrentBuild": False,
            "disabled": False,
            "inQueue": True,
            "queueItem": {
                "_class": "hudson.model.Queue$BlockedItem",
                "blocked": True,
                "buildable": False,
                "id": 22,
                "inQueueSince": 1777750181665,
                "params": "",
                "stuck": False,
                "task": {
                    "_class": "org.jenkinsci.plugins.workflow.job.WorkflowJob",
                    "name": "test",
                    "url": "http://localhost:8080/job/test/",
                },
                "url": "queue/item/22/",
                "why": "Build #10 is already in progress (ETA: 29 min)",
                "buildableStartMilliseconds": 1777750181666,
            },
            "resumeBlocked": False,
        },
    ]

    e4: JenkinsWorkflowRunInfo = {
        "_class": "org.jenkinsci.plugins.workflow.job.WorkflowRun",
        "actions": [
            {
                "_class": "hudson.model.CauseAction",
                "causes": [
                    {
                        "_class": "hudson.model.Cause$UserIdCause",
                        "shortDescription": "Started by user admin",
                        "userId": "admin",
                        "userName": "admin",
                    }
                ],
            },
            {
                "_class": "jenkins.metrics.impl.TimeInQueueAction",
                "blockedDurationMillis": 0,
                "blockedTimeMillis": 0,
                "buildableDurationMillis": 0,
                "buildableTimeMillis": 1,
                "buildingDurationMillis": 2720,
                "executingTimeMillis": 2511,
                "executorUtilization": 0.92,
                "subTaskCount": 1,
                "waitingDurationMillis": 0,
                "waitingTimeMillis": 0,
            },
            {"_class": "org.jenkinsci.plugins.workflow.libs.LibrariesAction"},
            {},
            {},
            {},
            {},
            {},
            {"_class": "org.jenkinsci.plugins.displayurlapi.actions.RunDisplayAction"},
            {
                "_class": "org.jenkinsci.plugins.pipeline.modeldefinition.actions.RestartDeclarativePipelineAction"
            },
            {},
            {"_class": "org.jenkinsci.plugins.workflow.job.views.FlowGraphAction"},
            {},
            {},
        ],
        "artifacts": [],
        "building": False,
        "description": None,
        "displayName": "#5",
        "duration": 2720,
        "estimatedDuration": 2347947,
        "executor": None,
        "fullDisplayName": "test #5",
        "id": "5",
        "keepLog": False,
        "number": 5,
        "queueId": 9,
        "result": "SUCCESS",
        "timestamp": 1777738420839,
        "url": "http://localhost:8080/job/test/5/",
        "changeSets": [],
        "culprits": [],
        "inProgress": False,
        "nextBuild": {"number": 6, "url": "http://localhost:8080/job/test/6/"},
        "previousBuild": {"number": 4, "url": "http://localhost:8080/job/test/4/"},
    }
