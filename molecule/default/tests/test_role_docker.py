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

def test_docker_service(host):
    service = host.service("docker")
    assert service.is_running
    assert service.is_enabled
