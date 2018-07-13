

class User(object):

    def __init__(self, id=None, username=None, email=None, is_active=False, is_staff=False, password=None):
        self._id = id
        self._username = username
        self._email = email
        self._is_active = is_active
        self._is_staff = is_staff
        self._password = password


    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username


    @property
    def email(self):
        return self._email


    @property
    def is_active(self):
        return self._is_active


    @property
    def is_staff(self):
        return self._is_staff

    @property
    def password(self):
        return self._password



class TokenUser(object):

    def __init__(self, token=None, user_id=None):
        self._token = token
        self._user_id = user_id



    @property
    def token(self):
        return self._token

    @property
    def user_id(self):
        return self._user_id

    def payload(self):
        return {
            'user_id': self.user_id,
        }





