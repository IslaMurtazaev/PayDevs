from account.factories.repo_factories import UserRepoFactory
from account.factories.token_factories import AuthTokenFactory
from account.factories.validate_factories import HashPasswordFactor, \
    UsernameEmailValidatorFactory
from account.interactors import GetUsersInteractor, LoginUserInteractor, RegisterUserInteractor, \
    AuthUserInteractor


class GetUsersInteractorFactory(object):
    @staticmethod
    def create():
        user_repo_factory = UserRepoFactory().create()
        return GetUsersInteractor(user_repo_factory)



class LoginUserInreractorFactory(object):
    @staticmethod
    def create():
        user_repo_factory = UserRepoFactory().create()
        get_token = AuthTokenFactory().create()
        return LoginUserInteractor(user_repo_factory, get_token)




class RegisterUserInteractorFactory(object):
    @staticmethod
    def create():
        user_repo_factory = UserRepoFactory().create()
        validate_username_email_factory = UsernameEmailValidatorFactory().create()
        hashed_password_factory = HashPasswordFactor()
        return RegisterUserInteractor(user_repo_factory, validate_username_email_factory,
                                      hashed_password_factory)


class AuthUserInteractorFactory(object):

    @staticmethod
    def create():
        token_decoder = AuthTokenFactory().create()
        return AuthUserInteractor(token_decoder)
