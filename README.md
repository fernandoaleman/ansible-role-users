# Ansible Role: Users

[![CI](https://github.com/1000Bulbs/ansible-role-users/actions/workflows/ci.yml/badge.svg)](https://github.com/1000Bulbs/ansible-role-users/actions/workflows/ci.yml)

This role manages Linux user accounts including:

- Creating users with default or custome shell/home/group
- Validating username formatting
- Managing SSH keys
- Removing users when needed

## Requirements

- Ansible 2.13+
- Tested on Ubuntu 22.04+
- Python >= 3.9 (if using Molecule + pytest)

## Role Variables

These variables can be defined in your inventory, playbooks, or group_vars:

### Default Variables

- **`users_add`**: Default = `[]`
- **`users_del`**: Default = `[]`

### Other Role Variables

_No variables defined._

## Dependencies

_No dependencies defined._

## Installing the Role via `ansible-galaxy`

To include this role in your project using a `requirements.yml` file:

```yaml
roles:
  - name: okb.users
    src: git@github.com:1000bulbs/ansible-role-users.git
    scm: git
    version: master
```

Then install it with:

```bash
ansible-galaxy role install -r requirements.yml
```

This will install the role under `~/.ansible/roles/users` by default, or to the directory defined in your `ansible.cfg`.

## Example Playbook

```yaml
- name: Manage users
  hosts: all
  become: true
  roles:
    - role: okb.users
      vars:
        users_add:
          - name: deploy
            shell: /bin/bash
            ssh_keys:
              - "ssh-ed25519 AAAAC3N... user1@domain.com"
              - "ssh-ed25519 AAAAC3N... user2@domain.com"
          - name: devops
            groups: ["sudo"]
            ssh_keys:
              - "ssh-ed25519 AAAAC3N... user1@domain.com"

        users_del:
          - olduser
```

## Deleting Users

To delete users, provide a `users_del` list:

```yaml
users_del:
  - user1
  - user2
```

## Testing

This role supports [Molecule](https://molecule.readthedocs.io/) and `pytest-testinfra`.

### Run tests

```bash
pip install -r requirements.txt
molecule test
```
