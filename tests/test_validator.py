from utils.validator import ConfigValidator


def test_validator_detects_multiple_errors():

    config = {
        "ous": ["IT"],

        "users": [
            {
                "username": "administrator",
                "first_name": "Admin",
                "last_name": "User",
                "password": "weakpass",
                "ou": "Finance"
            },
            {
                "username": "administrator",
                "first_name": "Admin2",
                "last_name": "User2",
                "password": "weakpass",
                "ou": "Finance"
            }
        ],

        "groups": [
            {"name": "IT Admins"},
            {"name": "IT Admins"}
        ],

        "computers": [
            {"name": "PC-001", "ou": "IT"},
            {"name": "PC-001", "ou": "IT"}
        ],

        "memberships": [
            {
                "user": "john",
                "group": "IT Admins"
            },
            {
                "user": "john",
                "group": "IT Admins"
            }
        ]
    }

    validator = ConfigValidator(config)

    result = validator.validate()

    assert result is False

    errors = "\n".join(validator.errors)

    assert "Duplicate username found" in errors
    assert "Forbidden username detected" in errors
    assert "Duplicate group found" in errors
    assert "Duplicate computer found" in errors
    assert "Weak password" in errors
    assert "references non-existing OU" in errors
    assert "Membership references non-existing user" in errors
    assert "Duplicate membership found" in errors
    