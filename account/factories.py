from account.interactors import GetUsersInteractor, GetUsersAllInteractor, RegisterUserInteractor, LoginUserInteractor
from account.repositories import UserRepo
from account.views import UserView, UserAllView, UserRegisterView, LoginUserView


class UserRepoFactory(object):
    @staticmethod
    def get():
        return UserRepo()


class GetUsersInteractorFactory(object):
    @staticmethod
    def get():
        user_repo = UserRepoFactory().get()
        return GetUsersInteractor(user_repo)


class GetUsersAllInteractorFactory(object):
    @staticmethod
    def get():
        user_repo = UserRepoFactory().get()
        return GetUsersAllInteractor(user_repo)


class LoginUserInreractorFactory(object):
    @staticmethod
    def get():
        user_repo = UserRepoFactory().get()
        return LoginUserInteractor(user_repo)


class RegisterUserInteractorFactory(object):
    @staticmethod
    def get():
        user_repo = UserRepoFactory().get()
        return RegisterUserInteractor(user_repo)


def get_user_factories():
    get_user_interactor = GetUsersInteractorFactory().get()
    return UserView(get_user_interactor)


def get_user_all_factories():
    get_user_interactor = GetUsersAllInteractorFactory().get()
    return UserAllView(get_user_interactor)



def get_user_regist_factories():
    get_user_interactor = RegisterUserInteractorFactory().get()
    return UserRegisterView(get_user_interactor)


def get_user_login_factories():
    get_user_interactor = LoginUserInreractorFactory().get()
    return LoginUserView(get_user_interactor)
