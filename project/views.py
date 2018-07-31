from project.serializers import ProjectSerializer, ProjectListSerializer, WorkTaskSerializer, WorkTaskListSerializer, \
    WorkedDaySerializer, WorkedDayListSerializer, WorkTimeSerializer, WorkTimeListSerializer, MonthPaymentSerializer, \
    MonthPaymentListSerializer, HourPaymentSerializer, HourPaymentListSerializer, ProjectTotalSerializer
from PayDevs.decorators import serialize_exception
from PayDevs.constants import StatusCodes



class ProjectView(object):

    def __init__(self, project_interactor):
        self.project_interactors = project_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        project = self.project_interactors.set_params(*args, **kwargs).execute()
        body = ProjectSerializer.serialize(project)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def post(self, *args, **kwargs):
        project = self.project_interactors.set_params(**kwargs).execute()
        body = ProjectSerializer.serialize(project)
        status = StatusCodes.CREATED
        return body, status


    @serialize_exception
    def put(self, *args, **kwargs):
        updated_project = self.project_interactors.set_params(**kwargs).execute()
        body = ProjectSerializer.serialize(updated_project)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_project = self.project_interactors.set_params(**kwargs).execute()
        body = ProjectSerializer.serialize(deleted_project)
        status = StatusCodes.OK
        return body, status


class GetAllProjectsView(object):

    def __init__(self, get_all_projects_interactor):
        self.get_all_projects_interactor = get_all_projects_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        projects = self.get_all_projects_interactor.set_params(**kwargs).execute()
        body = ProjectListSerializer.serialize(projects)
        status = StatusCodes.OK
        return body, status



class GetTotalProjectsView(object):

    def __init__(self, get_total_projects_interactor):
        self.get_total_projects_interactor = get_total_projects_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        pdf = self.get_total_projects_interactor.set_params(**kwargs).execute()
        body = {
            'pdf': pdf
        }
        status = StatusCodes.OK
        return body, status



class TaskView(object):

    def __init__(self, get_task_interactor):
        self.task_interactor = get_task_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        task = self.task_interactor.set_params(**kwargs).execute()
        body = WorkTaskSerializer.serialize(task)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def post(self, *args, **kwargs):
        task = self.task_interactor.set_params(**kwargs).execute()
        body = WorkTaskSerializer.serialize(task)
        status = StatusCodes.CREATED
        return body, status


    @serialize_exception
    def put(self, *args, **kwargs):
        modified_task = self.task_interactor.set_params(**kwargs).execute()
        body = WorkTaskSerializer.serialize(modified_task)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_task = self.task_interactor.set_params(**kwargs).execute()
        body = WorkTaskSerializer.serialize(deleted_task)
        status = StatusCodes.OK
        return body, status



class GetAllTasksView(object):

    def __init__(self, get_all_tasks_interactor):
        self.get_all_tasks_interactor = get_all_tasks_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        tasks = self.get_all_tasks_interactor.set_params(**kwargs).execute()
        body = WorkTaskListSerializer.serialize(tasks)
        status = StatusCodes.OK
        return body, status




class MonthPaymentView(object):

    def __init__(self, month_payment_interactor):
        self.month_payment_interactor = month_payment_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        month_payment = self.month_payment_interactor.set_params(**kwargs).execute()
        body = MonthPaymentSerializer.serialize(month_payment)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def post(self, *args, **kwargs):
        created_month_payment = self.month_payment_interactor.set_params(**kwargs).execute()
        body = MonthPaymentSerializer.serialize(created_month_payment)
        status = StatusCodes.CREATED
        return body, status


    @serialize_exception
    def put(self, *args, **kwargs):
        updated_month_payment = self.month_payment_interactor.set_params(**kwargs).execute()
        body = MonthPaymentSerializer.serialize(updated_month_payment)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_month_payment = self.month_payment_interactor.set_params(**kwargs).execute()
        body = MonthPaymentSerializer.serialize(deleted_month_payment)
        status = StatusCodes.OK
        return body, status


class GetAllMonthPaymentsView(object):

    def __init__(self, get_all_month_payments_interactor):
        self.get_all_month_payments_interactor = get_all_month_payments_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        month_payments = self.get_all_month_payments_interactor.set_params(**kwargs).execute()
        body = MonthPaymentListSerializer.serialize(month_payments)
        status = StatusCodes.OK
        return body, status



class WorkedDayView(object):

    def __init__(self, get_work_day_interactor):
        self.work_day_interactor = get_work_day_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        worked_day = self.work_day_interactor.set_params(**kwargs).execute()
        body = WorkedDaySerializer.serialize(worked_day)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def post(self, *args, **kwargs):
        created_worked_day = self.work_day_interactor.set_params(**kwargs).execute()
        body = WorkedDaySerializer.serialize(created_worked_day)
        status = StatusCodes.CREATED
        return body, status


    @serialize_exception
    def put(self, *args, **kwargs):
        updated_worked_day = self.work_day_interactor.set_params(**kwargs).execute()
        body = WorkedDaySerializer.serialize(updated_worked_day)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_worked_day = self.work_day_interactor.set_params(**kwargs).execute()
        body = WorkedDaySerializer.serialize(deleted_worked_day)
        status = StatusCodes.OK
        return body, status


class GetAllWorkedDaysView(object):

    def __init__(self, get_all_worked_days_interactor):
        self.get_all_worked_days_interactor = get_all_worked_days_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        worked_days = self.get_all_worked_days_interactor.set_params(**kwargs).execute()
        body = WorkedDayListSerializer.serialize(worked_days)
        status = StatusCodes.OK
        return body, status




class HourPaymentView(object):
    def __init__(self, work_time_interactor):
        self.work_time_interactor = work_time_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = HourPaymentSerializer.serialize(worked_time)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def post(self, *args, **kwargs):
        created_worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = HourPaymentSerializer.serialize(created_worked_time)
        status = StatusCodes.CREATED
        return body, status


    @serialize_exception
    def put(self, *args, **kwargs):
        updated_worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = HourPaymentSerializer.serialize(updated_worked_time)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = HourPaymentSerializer.serialize(deleted_worked_time)
        status = StatusCodes.OK
        return body, status



class GetAllHourPaymentView(object):

    def __init__(self, work_time_interactor):
        self.work_time_interactor = work_time_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        worked_times = self.work_time_interactor.set_params(**kwargs).execute()
        body = HourPaymentListSerializer.serialize(worked_times)
        status = StatusCodes.OK
        return body, status


class WorkTimeView(object):

    def __init__(self, work_time_interactor):
        self.work_time_interactor = work_time_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = WorkTimeSerializer.serialize(worked_time)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def post(self, *args, **kwargs):
        created_worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = WorkTimeSerializer.serialize(created_worked_time)
        status = StatusCodes.CREATED
        return body, status


    @serialize_exception
    def put(self, *args, **kwargs):
        updated_worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = WorkTimeSerializer.serialize(updated_worked_time)
        status = StatusCodes.OK
        return body, status


    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = WorkTimeSerializer.serialize(deleted_worked_time)
        status = StatusCodes.OK
        return body, status


class GetWorkTimeListView(object):

    def __init__(self, get_all_work_time_list_interactor):
        self.get_all_work_time_list_interactor = get_all_work_time_list_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        worked_time_list = self.get_all_work_time_list_interactor.set_params(**kwargs).execute()
        body = WorkTimeListSerializer.serialize(worked_time_list)
        status = StatusCodes.OK
        return body, status
