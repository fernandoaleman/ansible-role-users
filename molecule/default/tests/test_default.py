# molecule/default/tests/test_default.py


def test_user_exists_and_configured(host, test_users_add):
    for user in test_users_add:
        u = host.user(user["name"])

        assert u.exists
        assert u.name == user["name"]
        assert u.home == user["home"]
        assert u.shell == user["shell"]

        for group in user["groups"]:
            assert group in u.groups


def test_ssh_directory_exists(host, test_users_add):
    for user in test_users_add:
        if "ssh_keys" not in user:
            continue

        f = host.file(f"/home/{user['name']}/.ssh")

        assert f.exists
        assert f.is_directory
        assert f.user == user["name"]
        assert f.group == user["name"]
        assert f.mode == 0o700


def test_authorized_keys_file_exists_and_contents(host, test_users_add):
    for user in test_users_add:
        if "ssh_keys" not in user:
            continue

        path = f"/home/{user['name']}/.ssh/authorized_keys"

        f = host.file(path)

        assert f.exists
        assert f.user == user["name"]
        assert f.group == user["name"]
        assert f.mode == 0o600

        content = f.content_string.strip().splitlines()
        for key in user["ssh_keys"]:
            assert key in content, f"Key missing from {path}:\n{key}"
