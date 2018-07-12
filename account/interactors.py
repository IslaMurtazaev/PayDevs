from account.entities import User
from account.validators import *
from PayDevs.exceptions import NoPermissionException
from PayDevs.interactors import Interactor
import jwt


class LoginUserInteractor(Interactor):
    def __init__(self, user_repo):
        self.user_repo = user_repo


    def set_params(self, username, password, secret_key=None):
        self.username = username
        self.password = password
        self.secret_key = secret_key
        return self

    def execute(self, *args, **kwargs):
        user = self.user_repo.get_user(username=self.username)
        chpw = check_password(self.password, user.password)
        payload = {'id': user.id, 'username': user.username}
        token = jwt.encode(payload, self.secret_key).decode()
        if not chpw:
            raise NoPermissionException('Roles do not match')
        return user, token



class RegisterUserInteractor(Interactor):

    def __init__(self, user_repo):
        self.user_repo = user_repo


    def set_params(self, username, email, password):
        validate_username(username=username)
        validate_email(email=email)
        self.username = username
        self.email = email
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

    def set_params(self, id):
        self.id = id
        return self

    def execute(self, *args, **kwargs):
        return self.user_repo.get_user(id=self.id)


class GetUsersAllInteractor(Interactor):
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self, *args, **kwargs):
        return self

    def execute(self, *args, **kwargs):
        return self.user_repo.all()


class AuthUserInteractor(Interactor):

    def set_params(self, token, secket_key):
        self.token = token
        self.secket_key = secket_key
        return self

    def execute(self, *args, **kwargs):
        payload = jwt.decode(self.token, self.secket_key)
        try:
            logged_id = payload['id']
            return logged_id
        except Exception:
            return None
