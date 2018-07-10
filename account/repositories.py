from account.entities import User
from account.models import UserORM
from account.validators import hashed_password
from PayDevs.exceptions import EntityDoesNotExistException, EntityIntegrityException
from django.db.utils import IntegrityError



class UserRepo:


    def get_user(self, id=None, username=None, email=None):
        try:
            if id is not None:
                db_user = UserORM.objects.get(id=id)
            elif username is not None:
                db_user = UserORM.objects.get(username=username)
            else:
                db_user = UserORM.objects.get(email=email)

        except UserORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_user(db_user)


    def create_default_user(self, username):
        try:
            db_user = UserORM.objects.create(username=username)
        except IntegrityError:
            raise EntityIntegrityException(username=username)
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

    def all(self):
        try:
            db_users = UserORM.objects.all()
        except UserORM.DoesNotExist:
            raise EntityDoesNotExistException
        users = list()
        for db_user in db_users:
            users.append(self._decode_db_user(db_user))
        return users

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
