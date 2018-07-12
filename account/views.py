from account.serializers import UserSerializer, UserListSerializer
from PayDevs.decorators import serialize_exception


class UserView(object):
    def __init__(self, get_user_interactor):
        self.get_user_interactor = get_user_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        user = self.get_user_interactor.set_params(id=kwargs['user_id']).execute()
        body = UserSerializer.serializer(user)
        status = 200
        return body, status


class UserAllView(object):
    def __init__(self, get_user_interactor):
        self.get_user_interactor = get_user_interactor

    @serialize_exception
    def get(self):
        users = self.get_user_interactor.set_params().execute()
        body = UserListSerializer.serializer(users)
        status = 200
        return body, status


class UserRegisterView(object):
    def __init__(self, get_user_interactor, get_auth_interactor):
        self.get_user_interactor = get_user_interactor
        self.get_auth_interactor = get_auth_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        secret_key = kwargs.get('secret_key')
        self.get_user_interactor.set_params(username=username,
                                                   email=email, password=password).execute()
        user, token = self.auth(username, password, secret_key=secret_key)

        body = UserSerializer.serializer(user)
        body.update({'token': token})
        status = 200
        return body, status

    def auth(self, username, password, secret_key=None):
        return self.get_auth_interactor.set_params(username=username, password=password,
                                                   secret_key=secret_key).execute()


class LoginUserView(object):
    def __init__(self, get_user_interactor):
        self.get_user_interactor = get_user_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        secret_key = kwargs.get('secret_key')
        user, token = self.get_user_interactor.set_params(username=username,
                                                          password=password, secret_key=secret_key).execute()
        body = UserSerializer.serializer(user)
        body.update({'token': token})
        status = 200
        return body, status
