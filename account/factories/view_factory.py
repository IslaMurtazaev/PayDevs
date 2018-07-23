from account.factories.interactor_factories import GetUsersInteractorFactory, GetUsersAllInteractorFactory, \
    RegisterUserInteractorFactory, LoginUserInreractorFactory
from account.views import UserView, UserAllView, UserRegisterView, LoginUserView


def get_user_factories():
    get_user_interactor = GetUsersInteractorFactory().get()
    return UserView(get_user_interactor)


def get_user_all_factories():
    get_user_interactor = GetUsersAllInteractorFactory().get()
    return UserAllView(get_user_interactor)



def get_user_regist_factories():
    get_user_interactor = RegisterUserInteractorFactory().get()
    get_auth_interactor = LoginUserInreractorFactory().get()
    return UserRegisterView(get_user_interactor, get_auth_interactor)


def get_user_login_factories():
    get_user_interactor = LoginUserInreractorFactory().get()
    return LoginUserView(get_user_interactor)