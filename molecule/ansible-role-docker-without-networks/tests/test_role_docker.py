import pytest

@pytest.mark.parametrize("package_name", [
    "docker-ce",
    "docker-ce-cli",
    "containerd.io",
    "docker-buildx-plugin",
    "docker-compose-plugin",
])
def test_if_all_packages_are_installed(host, package_name):
    packages = host.package(package_name)
    assert packages.is_installed


def test_docker_service(host):
    service = host.service("docker")
    assert service.is_running
    assert service.is_enabled