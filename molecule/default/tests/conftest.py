# molecule/default/tests/conftest.py
import pytest

USERS_ADD = [
    {
        "name": "deploy",
        "ssh_keys": [
            "ssh-ed25519 AAAAC3NzaC1 user1@email.com",
            "ssh-ed25519 AAAAC3NzaC2 user2@email.com",
            "ssh-ed25519 AAAAC3NzaC3 user3@email.com",
        ],
    },
    {
        "name": "devops",
        "groups": ["sudo"],
        "ssh_keys": [
            "ssh-ed25519 AAAAC3NzaC1 user1@email.com",
        ],
    },
    "foo",
]


@pytest.fixture
def test_users_add():
    normalized = []

    for user in USERS_ADD:
        if isinstance(user, str):
            name = user
            user = {"name": name}
        else:
            name = user["name"]

        user_dict = {
            "name": name,
            "home": user.get("home", f"/home/{name}"),
            "shell": user.get("shell", "/bin/bash"),
            "groups": user.get("groups", []),
        }

        # Only add ssh_keys if it exists and is non-empty
        ssh_keys = user.get("ssh_keys", [])
        if ssh_keys:
            user_dict["ssh_keys"] = ssh_keys

        normalized.append(user_dict)

    return normalized
