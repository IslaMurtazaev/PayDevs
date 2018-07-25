import jwt



class AuthToken(object):
    @staticmethod
    def encode(user, secret_key):
        return gen_token(user, secret_key)

    @staticmethod
    def decode(token, secret_key):
        return token_decoder(token, secret_key)



def gen_token(user, secret_key):
    payload = {
        'user_id': user.id
    }
    token = jwt.encode(payload, secret_key).decode()
    return token


def token_decoder(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key)
    except :
        payload = {}
    return payload.get('user_id', None)