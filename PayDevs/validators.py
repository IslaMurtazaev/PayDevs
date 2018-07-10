import re

def _validate_username(self, username):
    if (len(username) < 4):
        raise UsernameError(message='Username length is too short!')
    elif (len(username) > 50):
        raise UsernameError(message='Username length is too long!')
    elif (re.search(r" ", username) is not None):
        raise UsernameError(message='Username must not have whitespaces!')

    return True


def _validate_password(self, password):
    if (len(password) < 8):
        raise PasswordError(message='Password length is too short!')
    elif (len(password) > 20):
        raise PasswordError(message='Password length is too long!')
    elif (re.search(r"\d", password) is None):
        raise PasswordError(message='Password must contain at least one digit!')
    elif (re.search(r"[A-z]", password) is None):
        raise PasswordError(message='Password must contain at least one letter!')
    elif (re.search(r" ", password) is not None):
        raise PasswordError(message='Password must not have whitespaces!')

    return True