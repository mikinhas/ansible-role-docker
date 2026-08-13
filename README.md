# Ansible Role: Docker

Ansible role to install and configure Docker CE on Ubuntu and Debian.

## Description

This role performs the following actions:

- Install Docker CE and related components (CLI, containerd, BuildX, Compose)
- Add a user to the `docker` group to allow rootless execution
- Optionally create custom Docker networks

## Requirements

- Ansible >= 2.16
- Ubuntu 22.04 (Jammy) or Debian 12 (Bookworm)

The repository is declared with `ansible.builtin.deb822_repository`, which needs
`python3-debian` on the target — the role installs it itself.

### Required Collections

```yaml
collections:
  - community.docker
```

## Variables

### Default Variables

| Variable                   | Default                             | Description                                     |
| -------------------------- | ----------------------------------- | ----------------------------------------------- |
| `docker_user`              | `{{ ansible_user }}`                | User to add to the docker group                 |
| `docker_packages`          | see below                           | List of Docker packages to install              |
| `docker_networks`          | undefined                           | List of Docker networks to create (optional)    |
| `docker_apt_distribution`  | `{{ ansible_distribution \| lower }}` | Docker repository flavour (`ubuntu`, `debian`) |
| `docker_apt_architecture`  | `amd64`                             | Architecture published from the repository      |

### Default Packages

```yaml
docker_packages:
  - docker-ce
  - docker-ce-cli
  - containerd.io
  - docker-buildx-plugin
  - docker-compose-plugin
```

## Usage

### Basic Installation

```yaml
- hosts: servers
  roles:
    - role: mikinhas.docker
      vars:
        docker_user: deploy
```

### With Network Creation

```yaml
- hosts: servers
  roles:
    - role: mikinhas.docker
      vars:
        docker_user: deploy
        docker_networks:
          - frontend
          - backend
```

### Full Playbook Example

```yaml
---
- name: Install Docker
  hosts: docker_hosts
  become: true

  roles:
    - role: mikinhas.docker
      vars:
        docker_user: "{{ ansible_user }}"
        docker_networks:
          - app_network
          - monitoring
```

## Role Structure

```text
ansible-role-docker/
├── defaults/
│   └── main.yml          # Default variables
├── meta/
│   └── main.yml          # Role metadata
├── tasks/
│   ├── main.yml          # Main task entry point
│   ├── docker.yml        # Docker installation
│   └── networks.yml      # Network management
└── molecule/
    ├── default/                             # Installation without networks
    └── ansible-role-docker-with-networks/   # Installation with networks
```

## Testing

This role includes two Molecule test scenarios, each running against Ubuntu
22.04 and Debian 12:

```bash
# Test installation without networks
molecule test

# Test installation with networks
molecule test -s ansible-role-docker-with-networks
```

### Test Dependencies

```bash
pip install -r requirements.txt
```

## License

MIT

## Author

Michael MACHADO
