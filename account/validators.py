import bcrypt

from PayDevs import settings
from PayDevs.exceptions import InvalidEntityException




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
    validators = [MinimumLengthValidator(),]
    return validators


def validate_password(password, user=None):
    errors = []
    password_validators = get_password_validators()
    for validator in password_validators:
        try:
            validator.validate(password, user)
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



