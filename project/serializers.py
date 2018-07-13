from PayDevs.serializer import BaseSerializer, ListSerializer
from project.entities import Project


class ProjectSerializer(BaseSerializer):
    model = Project
    fields = ['id', 'title', 'description', 'start_date', 'end_date', 'user', 'type_of_payment', 'status']


class ProjectListSerializer(ListSerializer):
    model = Project
    fields = ['id', 'title', 'user']