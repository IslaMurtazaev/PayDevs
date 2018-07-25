from account.serializers import UserSerializer, UserListSerializer
from PayDevs.decorators import serialize_exception
from PayDevs.constants import StatusCodes


class UserView(object):
    def __init__(self, get_user_interactor):
        self.get_user_interactor = get_user_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        user = self.get_user_interactor.set_params(id=kwargs['logged_id']).execute()
        body = UserSerializer.serialize(user)

        status = StatusCodes.OK
        return body, status



class UserRegisterView(object):
    def __init__(self, get_user_interactor, get_auth_interactor):
        self.get_user_interactor = get_user_interactor
        self.get_auth_interactor = get_auth_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        self.get_user_interactor.set_params(**kwargs).execute()
        user = self.auth(**kwargs)
        body = UserSerializer.serialize(user)
        body.update({'token': user.token})
        status = StatusCodes.CREATED
        return body, status

    def auth(self, username, password, secret_key=None, **kwargs):
        return self.get_auth_interactor.set_params(username=username, password=password,
                                                   secret_key=secret_key).execute()


class LoginUserView(object):
    def __init__(self, get_user_interactor):
        self.get_user_interactor = get_user_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        user = self.get_user_interactor.set_params(**kwargs).execute()
        body = UserSerializer.serialize(user)
        body.update({'token': user.token})
        status = StatusCodes.OK
        return body, status
