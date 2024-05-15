import pytest

@pytest.mark.parametrize("package_name", [
    "docker-ce",
    "docker-ce-cli",
    "containerd.io",
    "docker-buildx-plugin",
    "docker-compose-plugin",
    "python3-requests",
])
def test_if_all_packages_are_installed(host, package_name):
    packages = host.package(package_name)
    assert packages.is_installed


def test_if_networks_foo_exists(host):
    networks = host.run("docker network list | grep foo")
    assert networks.rc == 0


def test_if_networks_bar_exists(host):
    networks = host.run("docker network list | grep bar")
    assert networks.rc == 0
