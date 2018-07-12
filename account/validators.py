import json
import os
import bcrypt
import re
from difflib import SequenceMatcher

from PayDevs import settings
from PayDevs.exceptions import InvalidEntityException


# ------------------------------ PASSWORD ------------------------------ #


def hashed_password(password, user=None):
    validate_password(password, user)
    password = password + settings.SECRET_KEY
    password = password.encode()
    return bcrypt.hashpw(password, salt=bcrypt.gensalt())


def check_password(password, hashed):
    password = password + settings.SECRET_KEY
    password = password.encode()
    hashed = hashed.encode()
    return bcrypt.checkpw(password, hashed)


def get_password_validators():
    validators = [
        MinimumLengthValidator(),
        UserAttributeSimilarityValidator(),
        CommonPasswordValidator(),
        NumericPasswordValidator()
    ]

    return validators


def validate_password(password, user=None):
    validate(password, user, get_password_validators())


# ------------------------------ USERNAME ------------------------------ #


def get_username_validators():
    validators = [ForbiddenNamesValidator(),
                  UsernameMinLengthValidator(),
                  UsernameMaxLengthValidator(),
                  UsernameRegex()]  # Username validators
    return validators


def validate_username(username, user=None):
    validate(username, user, get_username_validators())


# ------------------------------ EMAIL ------------------------------ #


def get_email_validators():
    validators = [EmailAtValidators(), EmailForbiddenEmailDomainsValidator()]  # email validators
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
        raise InvalidEntityException(source='validate', code='not_allowed', message=str(errors))


# ------------------------- PASSWORD VALIDATORS --------------------------- #

class MinimumLengthValidator(object):
    def __init__(self, min_len=8):
        self.min_len = min_len

    def validate(self, password, user=None):
        if self.min_len > len(password):
            raise InvalidEntityException(source='password', code='not_allowed', message=
            "Your password must contain at least %d character." % self.min_len)


class UserAttributeSimilarityValidator(object):
    DEFAULT_USER_ATTRIBUTES = ('username', 'password', 'email', 'first_name', 'last_name')

    def __init__(self, user_attrs=DEFAULT_USER_ATTRIBUTES, max_similarity=0.7):
        self.user_attrs = user_attrs
        self.max_similarity = max_similarity

    def validate(self, password, user=None):
        if not user:
            return

        for attr_name in self.user_attrs:
            value = getattr(user, attr_name, None)

            if not value or not isinstance(value, str):
                continue

            value_parts = re.split(r'\W', value) + [value]
            for part in value_parts:
                if SequenceMatcher(None, a=password.lower(), b=value.lower()) \
                        .quick_ratio() >= self.max_similarity:
                    raise InvalidEntityException(source='password', code='not allowed', \
                                                 message="Your password is too similar to your other fields.")


class CommonPasswordValidator(object):
    COMMON_SEQUENCES = ["123456789", "`1234567890-=", "~!@#$%^&*()_+",
                        "abcdefghijklmnopqrstuvwxyz",
                        "qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./",
                        'qwertyuiop{}|asdfghjkl;"zxcvbnm<>?',
                        "qwertyuiopasdfghjklzxcvbnm",
                        "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/-['=]\\",
                        "qazwsxedcrfvtgbyhnujmikolp",
                        "qwertzuiopü+asdfghjklöä#<yxcvbnm,.-",
                        "qwertzuiopü*asdfghjklöä'>yxcvbnm;:_",
                        "qaywsxedcrfvtgbzhnujmikolp",
                        'qwertyui']

    def __init__(self, common_sequences=COMMON_SEQUENCES):
        self.common_sequences = common_sequences

    def validate(self, password, user=None):
        if password in self.common_sequences:
            raise InvalidEntityException(source='password', code='not allowed', \
                                         message="Your password is a common sequence.")


class NumericPasswordValidator(object):
    def validate(self, password, user=None):
        if password.isdigit():
            raise InvalidEntityException(source='password', code='not allowed', \
                                         message="Your password consists of only digits.")


# ----------------------------------- user valid ------------------------------------#

class ForbiddenNamesValidator:
    forbidden_usernames_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                            'data/generic_forbidden_usernames.json')

    with open(forbidden_usernames_path) as f:
        forbidden_usernames = json.loads(f.read())

    def validate(self, username, user=None):
        if username.lower() in self.forbidden_usernames:
            raise InvalidEntityException(source='username', code='not_allowed', message='Username not allowed')


class UsernameMinLengthValidator(object):
    def __init__(self, min_len=3):
        self.min_len = min_len

    def validate(self, username, user=None):
        if len(username) < self.min_len:
            raise InvalidEntityException(source='username', code='not_allowed', message=
            "Your username must contain at least %d character." % self.min_len)


class UsernameMaxLengthValidator(object):
    def __init__(self, max_len=50):
        self.max_len = max_len

    def validate(self, username, user=None):
        if len(username) > self.max_len:
            raise InvalidEntityException(source='username', code='not_allowed', message=
            "Your username is too long. Max allowed length is %d." % self.max_len)


class UsernameRegex(object):
    def __init__(self):
        self.username_regex = "[a-zA-Z][a-zA-Z-'_\\d\\. ]+[a-zA-Z'_\\d\\.]?$"

    def validate(self, username, user=None):
        if not re.match(self.username_regex, username):
            raise InvalidEntityException(source='username', code='not_allowed', message='Username not allowed')


# ------------------------------------ email valid -----------------------------------#



class EmailAtValidators:
    def validate(self, email, user=None):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise InvalidEntityException(source='email', code='not_allowed', message="Invalid email address")


class EmailForbiddenEmailDomainsValidator:
    PATH_FORBIDDEN_EMAIL_DOMAINS = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                'data/forbidden_email_domains.json')
    with open(PATH_FORBIDDEN_EMAIL_DOMAINS) as f:
        forbidden_email_domains = json.loads(f.read())

    def validate(self, email, user=None):
        if email.split('@')[-1] in self.forbidden_email_domains:
            raise InvalidEntityException(source='email', code='not_allowed', message='Email not allowed')
