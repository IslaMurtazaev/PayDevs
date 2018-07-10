from account.entities import User
from account.validators import check_password, validate_password, hashed_password, validate_email
from PayDevs.exceptions import NoPermissionException
from PayDevs.interactors import Interactor


class LoginUserInteractor(Interactor):
    def __init__(self, user_repo):
        self.user_repo = user_repo


    def set_params(self, username, password):
        self.username = username
        self.password = password
        return self

    def execute(self, *args, **kwargs):
        user = self.user_repo.get_user(username=self.username)
        chpw = check_password(self.password, user.password)
        if not chpw:
            raise NoPermissionException('Roles do not match')
        return user



class RegisterUserInteractor(Interactor):

    def __init__(self, user_repo):
        self.user_repo = user_repo


    def set_params(self, username, email, password):
        self.username = username
        self.email = email
        validate_email(email)
        valid_user = User(username=self.username, email=self.email)
        self.password = hashed_password(password, user=valid_user).decode()

        return self

    def execute(self, *args, **kwargs):
        new_user = self.user_repo.create_default_user(username=self.username)
        user_update = User(id=new_user.id, username=self.username, email=self.email, password=self.password)
        return self.user_repo.update_user(user_update)



class GetUsersInteractor(Interactor):

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self, username):
        self.username = username
        return self

    def execute(self, *args, **kwargs):
        return self.user_repo.get_user(username=self.username)


class GetUsersAllInteractor(Interactor):
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self, *args, **kwargs):
        return self

    def execute(self, *args, **kwargs):
        return self.user_repo.all()