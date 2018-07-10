import bcrypt

from PayDevs import settings
from PayDevs.exceptions import InvalidEntityException

# ------------------------------ PASSWORD ------------------------------ #


def hashed_password(password):
    validate_password(password)
    password = password + settings.SECRET_KEY
    password = password.encode()
    return bcrypt.hashpw(password, salt=bcrypt.gensalt())


def check_password(password, hashed):
    password = password + settings.SECRET_KEY
    password = password.encode()
    hashed = hashed.encode()
    return bcrypt.checkpw(password, hashed)


def get_password_validators():
    validators = [MinimumLengthValidator(), ]
    return validators


def validate_password(password, user=None):
    validate(password, user, get_password_validators())

# ------------------------------ USERNAME ------------------------------ #


def get_username_validators():
    validators = []  # Username validators
    return validators


def validate_username(username, user=None):
    validate(username, user, get_username_validators())


# ------------------------------ EMAIL ------------------------------ #


def get_email_validators():
    validators = []  # email validators
    return validators


def validate_email(email, user=None):
    validate(email, user, get_email_validators())


def validate(value, user=None, validators=None):
    errors = []
    for validator in validators:
        try:
            validator.validate(value, user)
        except Exception as error:
            errors.append(error)
    if errors:
        raise InvalidEntityException(source='password', code='not_allowed', message=str(errors))


# ----------------------------------- class valid ------------------------------------#


class MinimumLengthValidator(object):
    def __init__(self, min_len=8):
        self.min_len = min_len

    def validate(self, password, user=None):
        if self.min_len > len(password):
            raise InvalidEntityException(source='password', code='not_allowed', message=
            "Your password must contain at least %d character." % self.min_len)

# class


# ----------------------------------- user valid ------------------------------------#
