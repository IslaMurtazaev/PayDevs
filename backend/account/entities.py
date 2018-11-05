class User:
    def __init__(self, id=None, username=None, email=None, is_active=False, is_staff=False):
        self.id = id
        self.username = username
        self.email = email
        self.is_active = is_active
        self.is_staff = is_staff


   
class TokenUser:
    def __init__(self, token=None, user_id=None):
        self.token = token
        self.user_id = user_id


    def payload(self):
        return {
            'user_id': self.user_id,
        }

