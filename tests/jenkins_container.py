from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any
from typing import NamedTuple

from testcontainers.core.container import DockerContainer

if TYPE_CHECKING:
    from testcontainers.core.network import Network
    from testcontainers.core.waiting_utils import WaitStrategy


class JenkinsInfo(NamedTuple):
    base_url: str
    username: str
    password: str


class JenkinsContainer(DockerContainer):
    JENKINS_PORT = 8080

    def __init__(  # noqa: PLR0913
        self,
        image: str = "jenkins/jenkins:latest",
        docker_client_kw: dict[str, Any] | None = None,
        command: str | None = None,
        env: dict[str, str] | None = None,
        name: str | None = None,
        ports: list[int] | None = None,
        volumes: list[tuple[str, str, str]] | None = None,
        network: Network | None = None,
        network_aliases: list[str] | None = None,
        _wait_strategy: WaitStrategy | None = None,
        **kwargs: Any,  # noqa: ANN401
    ) -> None:

        super().__init__(
            image=image,
            docker_client_kw=docker_client_kw,
            command=command,
            env=env,
            name=name,
            ports=ports,
            volumes=volumes,
            network=network,
            network_aliases=network_aliases,
            _wait_strategy=_wait_strategy,
            **kwargs,
        )
        from testcontainers.core.wait_strategies import LogMessageWaitStrategy

        self.with_exposed_ports(self.JENKINS_PORT)
        self.waiting_for(LogMessageWaitStrategy("Jenkins is fully up and running"))

    def get_triple(self) -> JenkinsInfo:
        result = self.exec("cat /var/jenkins_home/secrets/initialAdminPassword")
        output: bytes = result.output
        password = output.decode().strip()

        return JenkinsInfo(
            f"http://{self.get_container_host_ip()}:{self.get_exposed_port(self.JENKINS_PORT)}",
            "admin",
            password,
        )
