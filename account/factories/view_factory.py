from account.factories.interactor_factories import GetUsersInteractorFactory, GetUsersAllInteractorFactory, \
    RegisterUserInteractorFactory, LoginUserInreractorFactory
from account.views import UserView, UserAllView, UserRegisterView, LoginUserView


def get_user_factories():
    create_user_interactor = GetUsersInteractorFactory().create()
    return UserView(create_user_interactor)


def get_user_all_factories():
    create_user_interactor = GetUsersAllInteractorFactory().create()
    return UserAllView(create_user_interactor)



def get_user_regist_factories():
    create_user_interactor = RegisterUserInteractorFactory().create()
    create_auth_interactor = LoginUserInreractorFactory().create()
    return UserRegisterView(create_user_interactor, create_auth_interactor)


def get_user_login_factories():
    create_user_interactor = LoginUserInreractorFactory().create()
    return LoginUserView(create_user_interactor)