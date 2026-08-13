import pytest

@pytest.mark.parametrize("package_name", [
    "docker-ce",
    "docker-ce-cli",
    "containerd.io",
    "docker-buildx-plugin",
    "docker-compose-plugin",
    "python3-debian",
])
def test_if_all_packages_are_installed(host, package_name):
    packages = host.package(package_name)
    assert packages.is_installed


def test_docker_repository(host):
    sources = host.file("/etc/apt/sources.list.d/docker.sources")
    assert sources.exists
    assert host.system_info.distribution in sources.content_string


def test_docker_service(host):
    service = host.service("docker")
    assert service.is_running
    assert service.is_enabled
