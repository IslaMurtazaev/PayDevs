from account.factories.repo_factories import UserRepoFactory
from account.factories.token_factories import AuthTokenFactory
from account.factories.validate_factories import HashPasswordFactor, \
    UsernameEmailValidatorFactory
from account.interactors import GetUserInteractor, LoginUserInteractor, RegisterUserInteractor, \
    AuthUserInteractor


class GetUserInteractorFactory:
    @staticmethod
    def create():
        user_repo_factory = UserRepoFactory().create()
        return GetUserInteractor(user_repo_factory)



class LoginUserInreractorFactory:
    @staticmethod
    def create():
        user_repo_factory = UserRepoFactory().create()
        get_token = AuthTokenFactory().create()
        return LoginUserInteractor(user_repo_factory, get_token)




class RegisterUserInteractorFactory:
    @staticmethod
    def create():
        user_repo_factory = UserRepoFactory().create()
        validate_username_email_factory = UsernameEmailValidatorFactory().create()
        hashed_password_factory = HashPasswordFactor()
        return RegisterUserInteractor(user_repo_factory, validate_username_email_factory,
                                      hashed_password_factory)


class AuthUserInteractorFactory:
    @staticmethod
    def create():
        token_decoder = AuthTokenFactory().create()
        return AuthUserInteractor(token_decoder)
