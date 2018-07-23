from PayDevs.exceptions import NoLoggedException, NoPermissionException


class UserPermissionsValidator:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def validate_pemission(self, logged_id, user_id=None):
        if logged_id is None:
            raise NoLoggedException
        if user_id is not None and logged_id != user_id:
            raise NoPermissionException
