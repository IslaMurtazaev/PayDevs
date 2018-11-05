from PayDevs.serializers import BaseSerializer, ListSerializer
from account.entities import User


class UserSerializer:
    @staticmethod
    def serialize(user):
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active,
            'is_staff': user.is_staff
        }



class UserListSerializer:

    @staticmethod
    def serialize(users):
        return [UserSerializer.serialize(user) for user in users]





