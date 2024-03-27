def test_docker_is_installed(host):
    package = host.package("docker-ce")
    assert package.is_installed

def test_docker_cli_is_installed(host):
    package = host.package("docker-ce-cli")
    assert package.is_installed

def test_docker_buildx_is_installed(host):
    package = host.package("containerd.io")
    assert package.is_installed

def test_docker_compose_is_installed(host):
    package = host.package("docker-buildx-plugin")
    assert package.is_installed

def test_docker_compose_is_installed(host):
    package = host.package("docker-compose-plugin")
    assert package.is_installed

def test_pip_is_installed(host):
    package = host.package("python3-pip")
    assert package.is_installed

def test_docker_service(host):
    service = host.service("docker")
    assert service.is_running
    assert service.is_enabled

def test_if_pip_is_installed(host):
    pip_package = host.package("requests").is_installed

def test_if_networks_foo_exists(host):
    networks = host.run("docker network list | grep foo")
    assert networks.rc == 0

def test_if_networks_bar_exists(host):
    networks = host.run("docker network list | grep bar")
    assert networks.rc == 0