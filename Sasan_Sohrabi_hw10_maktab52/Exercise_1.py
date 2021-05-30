# Import relevant libraries
import re


def name_validation(name: str) -> bool:
    name_validation_pattern = r"^[a-zA-Z_][a-zA-Z_]{4,13}$"
    if re.match(name_validation_pattern, name):
        return True
    return False


def email_validation(name: str) -> bool:
    email_validation_pattern = r"^[a-zA-Z0-9_+-.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$"
    if re.match(email_validation_pattern, name):
        return True
    return False


def phone_validation(name: str) -> bool:
    phone_validation_pattern = r"^(09|\+989)+\d{9}$"
    if re.match(phone_validation_pattern, name):
        return True
    return False
