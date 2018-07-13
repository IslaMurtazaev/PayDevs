import jwt


def gen_token(user, secret_key):
    payload = {
        'user_id': user.id
    }
    token = jwt.encode(payload, secret_key).decode()
    return token


def token_decoder(token, secret_key):
    payload = jwt.decode(token, secret_key)
    return payload.get('user_id', None)