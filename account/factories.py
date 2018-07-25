from account.interactors import GetUsersInteractor, RegisterUserInteractor, LoginUserInteractor,\
    AuthUserInteractor
from account.token_auth import token_decoder, gen_token
from account.validators import *
from account.repositories import UserRepo
from account.views import UserView, UserRegisterView, LoginUserView

# TODO divide factories into one module
class UserRepoFactory(object):
    @staticmethod
    def get():
        return UserRepo()


class GetUsersInteractorFactory(object):
    @staticmethod
    def get():
        user_repo_factory = UserRepoFactory().get()
        return GetUsersInteractor(user_repo_factory)


class ValidateCheckPasswordFactory(object):
    @staticmethod
    def check_password(passoword, hashed):
        return check_password(passoword, hashed)


class GetUsersAllInteractorFactory(object):
    @staticmethod
    def get():
        user_repo_factory = UserRepoFactory().get()
        return GetUsersInteractor(user_repo_factory)


class TokenGenFactory(object):

    @staticmethod
    def encode(user, secret_key):
        return gen_token(user, secret_key)


class LoginUserInreractorFactory(object):
    @staticmethod
    def get():
        user_repo_factory = UserRepoFactory().get()
        valid_check_password_factory = ValidateCheckPasswordFactory()
        get_token = TokenGenFactory()
        return LoginUserInteractor(user_repo_factory, valid_check_password_factory, get_token)


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



class RegisterUserInteractorFactory(object):
    @staticmethod
    def get():
        user_repo_factory = UserRepoFactory().get()
        validate_username_factory = UsernameValidatorFactory()
        validate_email_factory = EmailValidatorFactory()
        hashed_password_factory = HashPasswordFactor()
        return RegisterUserInteractor(user_repo_factory, validate_username_factory,
                                      validate_email_factory, hashed_password_factory)


class TokenDecodeFactory(object):

    @staticmethod
    def decode(token, secret_key):
        return token_decoder(token, secret_key)


class AuthUserInteractorFactory(object):

    @staticmethod
    def create():
        token_decoder = TokenDecodeFactory()
        return AuthUserInteractor(token_decoder)


def get_user_factories():
    get_user_interactor = GetUsersInteractorFactory().get()
    return UserView(get_user_interactor)


# def get_user_all_factories():
#     get_user_interactor = GetUsersAllInteractorFactory().get()
#     return UserAllView(get_user_interactor)



def get_user_regist_factories():
    get_user_interactor = RegisterUserInteractorFactory().get()
    get_auth_interactor = LoginUserInreractorFactory().get()
    return UserRegisterView(get_user_interactor, get_auth_interactor)


def get_user_login_factories():
    get_user_interactor = LoginUserInreractorFactory().get()
    return LoginUserView(get_user_interactor)
