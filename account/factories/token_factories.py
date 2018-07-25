from account.token_auth import AuthToken


class AuthTokenFactory(object):

    @staticmethod
    def create():
        return AuthToken()