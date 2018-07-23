from account.token_auth import gen_token, token_decoder


class TokenGenFactory(object):

    @staticmethod
    def encode(user, secret_key):
        return gen_token(user, secret_key)




class TokenDecodeFactory(object):

    @staticmethod
    def decode(token, secret_key):
        return token_decoder(token, secret_key)
