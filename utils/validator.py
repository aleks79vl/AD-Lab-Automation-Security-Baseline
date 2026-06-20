from typing import Dict, List
import re

from utils.logger import log_validation, log_error


class ConfigValidator:

    FORBIDDEN_USERNAMES = {
        "admin",
        "administrator",
        "guest",
        "root",
        "user",
        "test",
        "demo"
    }

    def __init__(self, config: Dict):
        self.config = config
        self.errors: List[str] = []

    def add_error(self, message: str):
        self.errors.append(message)
        log_error(message)

    def validate_duplicate_users(self):
        users = self.config.get("users", [])
        usernames = []

        for user in users:
            username = user.get("username")

            if username in usernames:
                self.add_error(f"Duplicate username found: {username}")

            usernames.append(username)

    def validate_forbidden_usernames(self):
        users = self.config.get("users", [])

        for user in users:
            username = user.get("username", "").lower()

            if username in self.FORBIDDEN_USERNAMES:
                self.add_error(f"Forbidden username detected: {username}")

    def validate_duplicate_groups(self):
        groups = self.config.get("groups", [])
        group_names = []

        for group in groups:
            group_name = group.get("name")

            if group_name in group_names:
                self.add_error(f"Duplicate group found: {group_name}")

            group_names.append(group_name)

    def validate_duplicate_computers(self):
        computers = self.config.get("computers", [])
        computer_names = []

        for computer in computers:
            computer_name = computer.get("name")

            if computer_name in computer_names:
                self.add_error(f"Duplicate computer found: {computer_name}")

            computer_names.append(computer_name)

    def validate_required_fields(self):
        users = self.config.get("users", [])
        groups = self.config.get("groups", [])
        computers = self.config.get("computers", [])

        required_user_fields = [
            "username",
            "first_name",
            "last_name",
            "password",
            "ou"
        ]

        for user in users:
            for field in required_user_fields:
                if not user.get(field):
                    self.add_error(f"Missing required user field: {field}")

        for group in groups:
            if not group.get("name"):
                self.add_error("Missing required group field: name")

        for computer in computers:
            if not computer.get("name"):
                self.add_error("Missing required computer field: name")

            if not computer.get("ou"):
                self.add_error("Missing required computer field: ou")

    def validate_password_strength(self):
        users = self.config.get("users", [])

        for user in users:
            username = user.get("username", "unknown")
            password = user.get("password", "")

            if len(password) < 12:
                self.add_error(f"Weak password for user {username}: minimum length is 12")

            if not re.search(r"[A-Z]", password):
                self.add_error(f"Weak password for user {username}: missing uppercase letter")

            if not re.search(r"[a-z]", password):
                self.add_error(f"Weak password for user {username}: missing lowercase letter")

            if not re.search(r"\d", password):
                self.add_error(f"Weak password for user {username}: missing digit")

            if not re.search(r"[^A-Za-z0-9]", password):
                self.add_error(f"Weak password for user {username}: missing special character")

    def validate_existing_ous(self):
        existing_ous = set(self.config.get("ous", []))

        users = self.config.get("users", [])
        computers = self.config.get("computers", [])
        groups = self.config.get("groups", [])

        for user in users:
            username = user.get("username", "unknown")
            ou = user.get("ou")

            if ou and ou not in existing_ous:
                self.add_error(
                    f"User {username} references non-existing OU: {ou}"
                )

        for computer in computers:
            computer_name = computer.get("name", "unknown")
            ou = computer.get("ou")

            if ou and ou not in existing_ous:
                self.add_error(
                    f"Computer {computer_name} references non-existing OU: {ou}"
                )

        for group in groups:
            group_name = group.get("name", "unknown")
            ou = group.get("ou")

            if ou and ou not in existing_ous:
                self.add_error(
                    f"Group {group_name} references non-existing OU: {ou}"
                )

    def validate_memberships(self):
        users = self.config.get("users", [])
        groups = self.config.get("groups", [])
        memberships = self.config.get("memberships", [])

        existing_users = {
            user.get("username")
            for user in users
        }

        existing_groups = {
            group.get("name")
            for group in groups
        }

        seen_memberships = set()

        for membership in memberships:
            username = membership.get("user")
            group_name = membership.get("group")

            membership_pair = (username, group_name)

            if username not in existing_users:
                self.add_error(
                    f"Membership references non-existing user: {username}"
                )

            if group_name not in existing_groups:
                self.add_error(
                    f"Membership references non-existing group: {group_name}"
                )

            if membership_pair in seen_memberships:
                self.add_error(
                    f"Duplicate membership found: {username} -> {group_name}"
                )

            seen_memberships.add(membership_pair)


    def validate(self) -> bool:
        log_validation("Starting config validation")

        self.validate_duplicate_users()
        self.validate_forbidden_usernames()
        self.validate_duplicate_groups()
        self.validate_duplicate_computers()
        self.validate_required_fields()
        self.validate_password_strength()
        self.validate_existing_ous()
        self.validate_memberships()

        if self.errors:
            log_validation("Config validation failed")
            return False

        log_validation("Config validation completed successfully")
        return True
        