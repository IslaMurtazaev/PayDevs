from account.factories.repo_factories import UserRepoFactory
from account.factories.token_factories import TokenGenFactory, TokenDecodeFactory
from account.factories.validate_factories import ValidateCheckPasswordFactory, UsernameValidatorFactory, \
    EmailValidatorFactory, HashPasswordFactor
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
        valid_check_password_factory = ValidateCheckPasswordFactory()
        get_token = TokenGenFactory()
        return LoginUserInteractor(user_repo_factory, valid_check_password_factory, get_token)




class RegisterUserInteractorFactory(object):
    @staticmethod
    def create():
        user_repo_factory = UserRepoFactory().create()
        validate_username_factory = UsernameValidatorFactory()
        validate_email_factory = EmailValidatorFactory()
        hashed_password_factory = HashPasswordFactor()
        return RegisterUserInteractor(user_repo_factory, validate_username_factory,
                                      validate_email_factory, hashed_password_factory)


class AuthUserInteractorFactory(object):

    @staticmethod
    def create():
        token_decoder = TokenDecodeFactory()
        return AuthUserInteractor(token_decoder)
