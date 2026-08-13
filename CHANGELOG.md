# Changelog

All notable changes to this project will be documented in this file.

## [0.3.1] - 2026-08-13

### Fixed

- Fall back to the `ansible_user_id` fact when `ansible_user` is unset.

## [0.3.0] - 2026-08-13

### Changed

- Replace `apt_repository` with `deb822_repository`: the former requires
  `apt-key` or `gpg` on the target even for a plain repository, and neither
  ships with modern Debian images
- Derive the repository URL from the target distribution instead of hardcoding
  `ubuntu`, so Debian hosts get the Debian repository

### Added

- `docker_apt_distribution` and `docker_apt_architecture` variables
- Install `python3-debian`, required by `deb822_repository`
- Remove the legacy one-line repository file left by <= 0.2.0
- Debian Bookworm in the supported platforms and in both Molecule scenarios
- Test asserting the repository is declared for the running distribution

### Fixed

- Install the Docker packages in a single `apt` transaction instead of looping,
  which refreshed the cache once per package
- Document the actual Molecule scenario names in the README
- Drop the unused `community.general` collection from `requirements.yml`
- Set `ANSIBLE_LIBRARY` in both Molecule scenarios so the `vagrant` module
  resolves again, and document the Python version requirement in the README

## [0.2.0] - 2026-01-21

### Changed

- Replace deprecated `apt_key` module with `get_url` + `signed-by`
- Replace libvirt Molecule driver with VirtualBox
- Simplify CI workflow

### Added

- Add `requirements.yml` for Ansible collections
- Add CHANGELOG.md
- Add pre-commit configuration with yamllint and ansible-lint
- Add `.ansible-lint` configuration with mock roles

## [0.1.0] - 2024-06-01

### Added

- Initial release
- Install Docker CE and related packages
- Add user to docker group
- Optional Docker networks creation
- Molecule tests with Vagrant
- Pre-commit hooks (yamllint, ansible-lint)
