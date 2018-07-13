from PayDevs.serializer import BaseSerializer, ListSerializer
from account.entities import User


class UserSerializer(BaseSerializer):
    model = User
    fields = ['id', 'username', 'email', 'is_active', 'is_staff']


class UserListSerializer(ListSerializer):
    model = User
    fields = ['id', 'username', 'email']




