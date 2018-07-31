from PayDevs.constants import DATE_TIME_FORMAT
from PayDevs.serializers import BaseSerializer, ListSerializer, DateFormatSerializer, DateFormatListSerializer
from project.entities import Project, WorkTask, WorkedDay, WorkTime, MonthPayment, HourPayment


class ProjectSerializer:


    @staticmethod
    def serialize(project):
        return {
            'id': project.id,
            'user_id': project.user_id,
            'title': project.title,
            'description': project.description,
            'start_date': project.start_date,
            'end_date': project.end_date,
            'type_of_payment': project.type_of_payment,
            'status': project.status
        }



class ProjectTotalSerializer:

    @staticmethod
    def serialize(project):
        return {
            'id': project.id,
            'user_id': project.user_id,
            'title': project.title,
            'description': project.description,
            'start_date': project.start_date.strftime(DATE_TIME_FORMAT),
            'end_date': project.end_date.strftime(DATE_TIME_FORMAT),
            'type_of_payment': project.type_of_payment,
            'status': project.status,
            'total': project.total
        }


class ProjectListSerializer:
    @staticmethod
    def serialize(projects):
        return [ProjectSerializer.serialize(project) for project in projects]



class WorkTaskSerializer:


    @staticmethod
    def serialize(work_task):
        return {
            'id': work_task.id,
            'project_id': work_task.project_id,
            'title': work_task.title,
            'description': work_task.description,
            'price': work_task.price,
            'completed': work_task.completed,
            'paid': work_task.paid
        }


class WorkTaskListSerializer:

    @staticmethod
    def serialize(work_tasks):
        return [WorkTaskSerializer.serialize(work_task) for work_task in work_tasks]



class MonthPaymentSerializer:

    @staticmethod
    def serialize(month_payment):
        return {
            'id': month_payment.id,
            'project_id': month_payment.project_id,
            'rate': month_payment.rate
        }


class MonthPaymentListSerializer(DateFormatListSerializer):
    model = MonthPayment
    fields = ['id', 'project_id', 'rate']


class WorkedDaySerializer(DateFormatSerializer):
    model = WorkedDay
    fields = ['id', 'day', 'paid', 'month_payment_id']


class WorkedDayListSerializer(DateFormatListSerializer):
    model = WorkedDay
    fields = ['id', 'day', 'paid', 'month_payment_id']



class HourPaymentSerializer(DateFormatSerializer):
    model = HourPayment
    fields = ['id', 'project_id', 'rate']


class HourPaymentListSerializer(DateFormatListSerializer):
    model = HourPayment
    fields = ['id', 'project_id', 'rate']



class WorkTimeSerializer(DateFormatSerializer):
    format = DATE_TIME_FORMAT
    model = WorkTime
    fields = ['id', 'start_work', 'end_work', 'paid', 'hour_payment_id']


class WorkTimeListSerializer(DateFormatListSerializer):
    format = DATE_TIME_FORMAT
    model = WorkTime
    fields = ['id', 'start_work', 'end_work', 'paid', 'hour_payment_id']
