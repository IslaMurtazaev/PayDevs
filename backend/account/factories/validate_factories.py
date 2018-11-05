from account.validators import check_password, hashed_password, \
    UsernameEmailValidator


class ValidateCheckPasswordFactory:
    @staticmethod
    def check_password(passoword, hashed):
        return check_password(passoword, hashed)


class UsernameEmailValidatorFactory:
    @staticmethod
    def create():
        return UsernameEmailValidator()



class HashPasswordFactor:
    @staticmethod
    def hashed(password, user=None):
        return hashed_password(password=password, user=user) # .decode()