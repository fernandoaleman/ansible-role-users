# molecule/default/tests/conftest.py
import pytest

USERS_ADD = [
    {"name": "deploy"},
    {"name": "devops", "groups": ["sudo"]},
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

        normalized.append(
            {
                "name": name,
                "home": user.get("home", f"/home/{name}"),
                "shell": user.get("shell", "/bin/bash"),
                "groups": user.get("groups", []),
            }
        )

    return normalized
