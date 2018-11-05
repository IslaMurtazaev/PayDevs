from account.token_auth import AuthToken


class AuthTokenFactory:
    @staticmethod
    def create():
        return AuthToken()