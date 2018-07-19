from PayDevs.serializer import BaseSerializer, ListSerializer
from project.entities import Project, WorkTask, WorkedDay


class ProjectSerializer(BaseSerializer):
    model = Project
    fields = ['id', 'user', 'title', 'description', 'start_date', 'end_date',  'type_of_payment', 'status']


class ProjectListSerializer(ListSerializer):
    model = Project
    fields = ['id', 'user', 'title', 'description', 'start_date', 'end_date',  'type_of_payment', 'status']


class WorkTaskSerializer(BaseSerializer):
    model = WorkTask
    fields = ['id', 'project', 'title', 'description', 'price', 'completed', 'paid']


class WorkTaskListSerializer(ListSerializer):
    model = WorkTask
    fields = ['id', 'project', 'title', 'description', 'price', 'completed', 'paid']


class WorkDaySerializer(BaseSerializer):
    model = WorkedDay
    fields = ['id', 'month_payment', 'day', 'paid']
