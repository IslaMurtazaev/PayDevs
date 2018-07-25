from PayDevs.serializer import BaseSerializer, ListSerializer, DateFormatSerializer, DateFormatListSerializer
from project.entities import Project, WorkTask, WorkedDay, WorkTime, MonthPayment, HourPayment


class ProjectSerializer(DateFormatSerializer):
    model = Project
    fields = ['id', 'user_id', 'title', 'description', 'start_date', 'end_date',  'type_of_payment', 'status']


class ProjectListSerializer(DateFormatListSerializer):
    model = Project
    fields = ['id', 'user_id', 'title', 'description', 'start_date', 'end_date',  'type_of_payment', 'status']



class WorkTaskSerializer(BaseSerializer):
    model = WorkTask
    fields = ['id', 'project_id', 'title', 'description', 'price', 'completed', 'paid']


class WorkTaskListSerializer(ListSerializer):
    model = WorkTask
    fields = ['id', 'project_id', 'title', 'description', 'price', 'completed', 'paid']



class MonthPaymentSerializer(DateFormatSerializer):
    model = MonthPayment
    fields = ['id', 'project_id', 'rate']


class MonthPaymentListSerializer(DateFormatListSerializer):
    model = MonthPayment
    fields = ['id', 'project_id', 'rate']



class HourPaymentSerializer(DateFormatSerializer):
    model = HourPayment
    fields = ['id', 'project_id', 'rate']


class HourPaymentListSerializer(DateFormatListSerializer):
    model = HourPayment
    fields = ['id', 'project_id', 'rate']


class WorkDaySerializer(DateFormatSerializer):
    model = WorkedDay
    fields = ['id', 'day', 'paid']


class WorkDayListSerializer(DateFormatListSerializer):
    model = WorkedDay
    fields = ['id', 'day', 'paid']



class WorkTimeSerializer(DateFormatSerializer):
    model = WorkTime
    fields = ['id', 'start_work', 'end_work', 'paid', 'hour_payment_id']


class WorkTimeListSerializer(DateFormatListSerializer):
    model = WorkTime
    fields = ['id', 'start_work', 'end_work', 'paid', 'hour_payment_id']
