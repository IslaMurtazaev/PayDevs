from account.validators import check_password, validate_username, validate_email, hashed_password


class ValidateCheckPasswordFactory(object):
    @staticmethod
    def check_password(passoword, hashed):
        return check_password(passoword, hashed)


class UsernameValidatorFactory(object):
    @staticmethod
    def validate(username, user=None):
        return validate_username(username=username, user=user)


class EmailValidatorFactory(object):
    @staticmethod
    def validate(email, user=None):
        return validate_email(email=email, user=user)



class HashPasswordFactor(object):
    @staticmethod
    def hashed(password, user=None):
        return hashed_password(password=password, user=user).decode()