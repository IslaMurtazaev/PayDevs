from PayDevs.serializer import BaseSerializer, ListSerializer, DateFormatSerializer, DateFormatListSerializer
from project.entities import Project, WorkTask, WorkedDay, WorkTime


class ProjectSerializer(DateFormatSerializer):
    model = Project
    fields = ['id', 'user', 'title', 'description', 'start_date', 'end_date',  'type_of_payment', 'status']


class ProjectListSerializer(DateFormatListSerializer):
    model = Project
    fields = ['id', 'user', 'title', 'description', 'start_date', 'end_date',  'type_of_payment', 'status']



class WorkTaskSerializer(BaseSerializer):
    model = WorkTask
    fields = ['id', 'project', 'title', 'description', 'price', 'completed', 'paid']


class WorkTaskListSerializer(ListSerializer):
    model = WorkTask
    fields = ['id', 'project', 'title', 'description', 'price', 'completed', 'paid']



class WorkDaySerializer(DateFormatSerializer):
    model = WorkedDay
    fields = ['id', 'month_payment', 'day', 'paid']



class WorkTimeSerializer(DateFormatSerializer):
    model = WorkTime
    fields = ['id', 'hour_payment', 'start_work', 'end_work', 'paid']
