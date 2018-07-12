

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
        return self._is_staff


    @property
    def is_staff(self):
        return self._is_staff

    @property
    def password(self):
        return self._password



