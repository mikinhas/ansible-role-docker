# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2026-01-21

### Changed

- Replace deprecated `apt_key` module with `get_url` + `signed-by`
- Replace libvirt Molecule driver with VirtualBox
- Simplify CI workflow

### Added

- Add `requirements.yml` for Ansible collections
- Add CHANGELOG.md
- Add pre-commit configuration with yamllint and ansible-lint

## [0.1.0] - 2024-06-01

### Added

- Initial release
- Install Docker CE and related packages
- Add user to docker group
- Optional Docker networks creation
- Molecule tests with Vagrant
- Pre-commit hooks (yamllint, ansible-lint)
