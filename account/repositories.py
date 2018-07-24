from account.entities import User
from account.models import UserORM
from PayDevs.exceptions import EntityDoesNotExistException, EntityIntegrityException, NoPermissionException
from django.db.utils import IntegrityError


class UserRepo:
    def check_password(self, user, password):
        db_user = UserORM.objects.get(username=user.username)
        if not db_user.check_password(password):
            raise NoPermissionException('Roles do not match')

    def get_user_by_id(self, id=None):
        try:
            db_user = UserORM.objects.get(id=id)

        except UserORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_user(db_user)

    def get_user_by_username(self, username=None):
        try:
            db_user = UserORM.objects.get(username=username)
        except UserORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_user(db_user)

    def get_user_by_user_email(self, email=None):
        try:
            db_user = UserORM.objects.get(username=email)
        except UserORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_user(db_user)

    def create_user(self, user):
        try:
            db_user = UserORM.objects.create_user(
                username=user.username,
                email=user.email,
                password=user.password,
                is_staff=user.is_staff
            )

        except IntegrityError:
            raise EntityIntegrityException(username=user.username)
        return self._decode_db_user(db_user)

    def update_user(self, user):
        db_user = UserORM.objects.get(id=user.id)
        db_user.username = user.username
        db_user.email = user.email
        db_user.is_active = user.is_active
        db_user.is_staff = user.is_staff
        db_user.password = user.password
        db_user.save()

        return self._decode_db_user(db_user)

    def get_user_project(self):
        pass

    def _decode_db_user(self, db_user):
        fileds = {
            'id': db_user.id,
            'username': db_user.username,
            'email': db_user.email,
            'is_active': db_user.is_active,
            'is_staff': db_user.is_staff,
            'password': db_user.password
        }

        return User(**fileds)
