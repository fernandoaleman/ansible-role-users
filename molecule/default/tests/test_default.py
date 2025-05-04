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
