from PayDevs.constants import DATE_TIME_FORMAT, DATE_FORMAT


class ProjectSerializer:
    @staticmethod
    def serialize(project):
        return {
            'id': project.id,
            'user_id': project.user_id,
            'title': project.title,
            'description': project.description,
            'start_date': project.start_date.strftime(DATE_TIME_FORMAT) if project.start_date else None,
            'end_date': project.end_date.strftime(DATE_TIME_FORMAT) if project.end_date else None,
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
            'start_date': project.start_date.strftime(DATE_TIME_FORMAT) if project.start_date else None,
            'end_date': project.end_date.strftime(DATE_TIME_FORMAT) if project.end_date else None,
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


class MonthPaymentListSerializer:
    @staticmethod
    def serialize(month_payments):
        return [MonthPaymentSerializer.serialize(month_payment) for month_payment in month_payments]


class WorkedDaySerializer:
    @staticmethod
    def serialize(worked_day):
        return {
            'id': worked_day.id,
            'day': worked_day.day.strftime(DATE_FORMAT) if worked_day.day else None,
            'paid': worked_day.paid,
            'month_payment_id': worked_day.month_payment_id
        }



class WorkedDayListSerializer:
    @staticmethod
    def serialize(worked_days):
        return [WorkedDaySerializer.serialize(worked_day) for worked_day in worked_days]



class HourPaymentSerializer:
    @staticmethod
    def serialize(hour_payment):
        return {
            'id': hour_payment.id,
            'project_id': hour_payment.project_id,
            'rate': hour_payment.rate
        }


class HourPaymentListSerializer:
    @staticmethod
    def serialize(hour_payments):
        return [HourPaymentSerializer.serialize(hour_payment) for hour_payment in hour_payments]


class WorkTimeSerializer:
    @staticmethod
    def serialize(work_time):
        return {
            'id': work_time.id,
            'start_work': work_time.start_work.strftime(DATE_TIME_FORMAT) if work_time.start_work else None,
            'end_work': work_time.end_work.strftime(DATE_TIME_FORMAT) if work_time.end_work else None,
            'paid': work_time.paid,
            'hour_payment_id': work_time.hour_payment_id
        }


class WorkTimeListSerializer:
    @staticmethod
    def serialize(work_times):
        return [WorkTimeSerializer.serialize(work_time) for work_time in work_times]
