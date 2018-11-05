import jwt


class AuthToken:
    @staticmethod
    def encode(user, secret_key):
        payload = {
            'user_id': user.id
        }
        token = jwt.encode(payload, secret_key).decode()
        return token

    @staticmethod
    def decode(token, secret_key):
        try:
            payload = jwt.decode(token, secret_key)
        except:
            payload = {}
        return payload.get('user_id', None)