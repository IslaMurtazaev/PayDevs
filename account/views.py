from account.serializers import UserSerializer, UserListSerializer
from PayDevs.decorators import serialize_exception



class UserView(object):
    def __init__(self, get_user_interactor):
        self.get_user_interactor = get_user_interactor

    @serialize_exception
    def get(self, username):
        user = self.get_user_interactor.set_params(username=username).execute()
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
    def __init__(self, get_user_interactor):
        self.get_user_interactor = get_user_interactor

    @serialize_exception
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = self.get_user_interactor.set_params(username=username,
                                                   email=email, password=password).execute()
        body = UserSerializer.serializer(user)
        status = 200
        return body, status


class LoginUserView(object):
    def __init__(self, get_user_interactor):
        self.get_user_interactor = get_user_interactor

    @serialize_exception
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = self.get_user_interactor.set_params(username=username,
                                                   password=password).execute()
        body = UserSerializer.serializer(user)
        status = 200
        return body, status