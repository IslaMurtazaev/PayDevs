from account.entities import User
from PayDevs.exceptions import NoPermissionException, NoLoggedException


class LoginUserInteractor():
    def __init__(self, user_repo, get_token):
        self.user_repo = user_repo
        self.get_token = get_token

    def set_params(self, username, password, secret_key=None, **kwargs):
        self.username = username
        self.password = password
        self.secret_key = secret_key
        return self

    def execute(self, *args, **kwargs):
        user = self.user_repo.get_user_by_username(username=self.username)
        self.user_repo.check_password(user, self.password)
        token = self.get_token.encode(user, self.secret_key)
        user.token = token
        return user


class RegisterUserInteractor():
    def __init__(self, user_repo, validate_username_email, hashed_password):
        self.user_repo = user_repo
        self.validate_username_email = validate_username_email
        self.hashed_password = hashed_password

    def set_params(self, username, email, password, **kwargs):
        self.username = username
        self.email = email
        self.password = password
        return self

    def execute(self, *args, **kwargs):
        valid_user = User(username=self.username, email=self.email)
        self._validate(valid_user)
        user = User(username=self.username, email=self.email,
                    is_active=True)

        return self.user_repo.create_user(user=user, password=self.password)

    def _validate(self, valid_user):
        self.validate_username_email.validate_username(username=self.username, user=valid_user)
        self.validate_username_email.validate_email(email=self.email, user=valid_user)
        self.hashed_password.hashed(password=self.password, user=valid_user)


class GetUserInteractor():
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self, id, **kwargs):
        self.id = id
        return self

    def execute(self, *args, **kwargs):
        if self.id is None:
            raise NoLoggedException()
        return self.user_repo.get_user_by_id(id=self.id)


class AuthUserInteractor():
    def __init__(self, token_decoder):
        self.token_decoder = token_decoder

    def set_params(self, token, secret_key=None, **kwargs):
        self.token = token
        self.secket_key = secret_key
        return self

    def execute(self, *args, **kwargs):
        user_id = self.token_decoder.decode(self.token, self.secket_key)
        return user_id
