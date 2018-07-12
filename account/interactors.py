from account.entities import User
from PayDevs.exceptions import NoPermissionException
from PayDevs.interactors import Interactor



class LoginUserInteractor(Interactor):
    def __init__(self, user_repo, valid_check_password, get_token):
        self.user_repo = user_repo
        self.valid_check_password = valid_check_password
        self.get_token = get_token


    def set_params(self, username, password, secret_key=None, **kwargs):
        self.username = username
        self.password = password
        self.secret_key = secret_key
        return self

    def execute(self, *args, **kwargs):
        user = self.user_repo.get_user(username=self.username)
        chpw = self.valid_check_password.check_password(self.password, user.password)
        token = self.get_token.encode(user, self.secret_key)
        if not chpw:
            raise NoPermissionException('Roles do not match')
        user.token = token
        return user



class RegisterUserInteractor(Interactor):

    def __init__(self, user_repo, validate_username, validate_email, hashed_password):
        self.user_repo = user_repo
        self.validate_username = validate_username
        self.validate_email = validate_email
        self.hashed_password = hashed_password


    def set_params(self, username, email, password, **kwargs):
        self.username = username
        self.email = email
        self.password = password
        return self

    def execute(self, *args, **kwargs):
        valid_user = User(username=self.username, email=self.email)
        self.validate_username.validate(username=self.username, user=valid_user)
        self.validate_email.validate(email=self.email, user=valid_user)
        self.password = self.hashed_password.hashed(password=self.password, user=valid_user)
        new_user = self.user_repo.create_default_user(username=self.username)
        user_update = User(id=new_user.id, username=self.username, email=self.email, password=self.password,
                           is_active=True)
        return self.user_repo.update_user(user_update)



class GetUsersInteractor(Interactor):

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self, id, **kwargs):
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

    def __init__(self, token_decoder):
        self.token_decoder = token_decoder

    def set_params(self, token, secket_key, **kwargs):
        self.token = token
        self.secket_key = secket_key
        return self

    def execute(self, *args, **kwargs):
        user_id = self.token_decoder.decode(self.token, self.secket_key)
        return user_id
