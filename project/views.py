from project.serializers import ProjectSerializer, ProjectListSerializer, WorkTaskSerializer, WorkTaskListSerializer, \
    WorkDaySerializer, WorkDayListSerializer, WorkTimeSerializer, WorkTimeListSerializer
from PayDevs.decorators import serialize_exception
from PayDevs.constants import StatusCodes



class ProjectView(object):

    def __init__(self, get_project_interactor):
        self.project_interactors = get_project_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        project = self.project_interactors.set_params(*args, **kwargs).execute()
        body = ProjectSerializer.serializer(project)
        status = 200
        return body, status


    @serialize_exception
    def post(self, *args, **kwargs):
        project = self.project_interactors.set_params(**kwargs).execute()
        body = ProjectSerializer.serializer(project)
        status = 201
        return body, status


    @serialize_exception
    def put(self, *args, **kwargs):
        updated_project = self.project_interactors.set_params(**kwargs).execute()
        body = ProjectSerializer.serializer(updated_project)
        status = 200
        return body, status


    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_project = self.project_interactors.set_params(**kwargs).execute()
        body = ProjectSerializer.serializer(deleted_project)
        status = 200
        return body, status




class GetAllProjectsView(object):

    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        projects = self.get_project_interactor.set_params(**kwargs).execute()
        body = ProjectListSerializer.serialize(projects)
        status = StatusCodes.OK
        return body, status



# class TotalView(object):
#
#     def __init__(self, get_type_of_payment_interactor, get_timestamp_interactor, get_worked_interactor, get_total_interactor, get_bill_interactor):
#         self.get_type_of_payment_interactor = get_type_of_payment_interactor
#         self.get_timestamp_interactor = get_timestamp_interactor
#         self.get_worked_interactor = get_worked_interactor #TODO make one interactor
#         self.get_total_interactor = get_total_interactor
#         self.get_bill_interactor = get_bill_interactor
#
#     @serialize_exception
#     def get(self, *args, **kwargs):
#         type_of_payment = self.get_type_of_payment_interactor.set_params(**kwargs).execute()
#         worked = self.get_worked_interactor.set_params(type_of_payment, **kwargs).execute()
#         timestamp = self.get_timestamp_interactor.set_params(type_of_payment, worked, **kwargs).execute()
#         total = self.get_total_interactor.set_params(type_of_payment, worked, **kwargs).execute()
#         bill = self.get_bill_interactor.set_params(type_of_payment, timestamp, total, **kwargs).execute()
#
#         body = bill
#         status = StatusCodes.OK
#         return body, status



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



# class GetWorkDayView(object):
#
#     def __init__(self, get_work_day_interactor):
#         self.get_work_day_interactor = get_work_day_interactor
#
#     @serialize_exception
#     def get(self, *args, **kwargs):
#         worked_day = self.get_work_day_interactor.set_params(**kwargs).execute()
#         body = WorkDaySerializer.serialize(worked_day)
#         status = StatusCodes.OK
#         return body, status
#
#
# class CreateWorkDayView(object):
#
#     def __init__(self, create_work_day_interactor):
#         self.create_work_day_interactor = create_work_day_interactor
#
#     @serialize_exception
#     def post(self, *args, **kwargs):
#         created_worked_day = self.create_work_day_interactor.set_params(**kwargs).execute()
#         body = WorkDaySerializer.serialize(created_worked_day)
#         status = StatusCodes.OK
#         return body, status
#
#
# class UpdateWorkDayView(object):
#
#     def __init__(self, update_work_day_interactor):
#         self.update_work_day_interactor = update_work_day_interactor
#
#     @serialize_exception
#     def put(self, *args, **kwargs):
#         updated_worked_day = self.update_work_day_interactor.set_params(**kwargs).execute()
#         body = WorkDaySerializer.serialize(updated_worked_day)
#         status = StatusCodes.OK
#         return body, status
#
#
# class DeleteWorkDayView(object):
#
#     def __init__(self, delete_work_day_interactor):
#         self.delete_work_day_interactor = delete_work_day_interactor
#
#     @serialize_exception
#     def delete(self, *args, **kwargs):
#         deleted_worked_day = self.delete_work_day_interactor.set_params(**kwargs).execute()
#         body = WorkDaySerializer.serialize(deleted_worked_day)
#         status = StatusCodes.OK
#         return body, status
#
#
# class GetAllWorkDaysView(object):
#
#     def __init__(self, get_all_work_days_interactor):
#         self.get_all_work_days_interactor = get_all_work_days_interactor
#
#     @serialize_exception
#     def get(self, *args, **kwargs):
#         worked_day = self.get_all_work_days_interactor.set_params(**kwargs).execute()
#         body = WorkDayListSerializer.serialize(worked_day)
#         status = StatusCodes.OK
#         return body, status
#
#
#
# class GetWorkTimeView(object):
#
#     def __init__(self, get_work_time_interactor):
#         self.get_work_time_interactor = get_work_time_interactor
#
#     @serialize_exception
#     def get(self, *args, **kwargs):
#         worked_time = self.get_work_time_interactor.set_params(**kwargs).execute()
#         body = WorkTimeSerializer.serialize(worked_time)
#         status = StatusCodes.OK
#         return body, status
#
#
# class CreateWorkTimeView(object):
#
#     def __init__(self, create_work_time_interactor):
#         self.create_work_time_interactor = create_work_time_interactor
#
#     @serialize_exception
#     def post(self, *args, **kwargs):
#         created_worked_time = self.create_work_time_interactor.set_params(**kwargs).execute()
#         body = WorkTimeSerializer.serialize(created_worked_time)
#         status = StatusCodes.CREATED
#         return body, status
#
#
# class UpdateWorkTimeView(object):
#
#     def __init__(self, update_work_time_interactor):
#         self.update_work_time_interactor = update_work_time_interactor
#
#     @serialize_exception
#     def put(self, *args, **kwargs):
#         updated_worked_time = self.update_work_time_interactor.set_params(**kwargs).execute()
#         body = WorkTimeSerializer.serialize(updated_worked_time)
#         status = StatusCodes.OK
#         return body, status
#
#
# class DeleteWorkTimeView(object):
#
#     def __init__(self, delete_work_time_interactor):
#         self.delete_work_time_interactor = delete_work_time_interactor
#
#     @serialize_exception
#     def delete(self, *args, **kwargs):
#         deleted_worked_time = self.delete_work_time_interactor.set_params(**kwargs).execute()
#         body = WorkTimeSerializer.serialize(deleted_worked_time)
#         status = StatusCodes.OK
#         return body, status



class WorkDayView(object):

    def __init__(self, get_work_day_interactor):
        self.work_day_interactor = get_work_day_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        worked_day = self.work_day_interactor.set_params(**kwargs).execute()
        body = WorkDaySerializer.serializer(worked_day)
        status = 200
        return body, status


    @serialize_exception
    def post(self, *args, **kwargs):
        created_worked_day = self.work_day_interactor.set_params(**kwargs).execute()
        body = WorkDaySerializer.serializer(created_worked_day)
        status = 201
        return body, status


    @serialize_exception
    def put(self, *args, **kwargs):
        updated_worked_day = self.work_day_interactor.set_params(**kwargs).execute()
        body = WorkDaySerializer.serializer(updated_worked_day)
        status = 201
        return body, status


    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_worked_day = self.work_day_interactor.set_params(**kwargs).execute()

        body = WorkDaySerializer.serializer(deleted_worked_day)
        status = 201
        return body, status


class GetAllWorkDaysView(object):

    def __init__(self, get_all_work_days_interactor):
        self.get_all_work_days_interactor = get_all_work_days_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        worked_day = self.get_all_work_days_interactor.set_params(**kwargs).execute()

        body = WorkDayListSerializer.serializer(worked_day)
        status = 200
        return body, status



class WorkTimeView(object):

    def __init__(self, work_time_interactor):
        self.work_time_interactor = work_time_interactor


    @serialize_exception
    def get(self, *args, **kwargs):
        worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = WorkTimeSerializer.serializer(worked_time)
        status = 200
        return body, status


    @serialize_exception
    def post(self, *args, **kwargs):
        created_worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = WorkTimeSerializer.serializer(created_worked_time)
        status = 201
        return body, status


    @serialize_exception
    def put(self, *args, **kwargs):
        updated_worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = WorkTimeSerializer.serializer(updated_worked_time)
        status = 201
        return body, status


    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_worked_time = self.work_time_interactor.set_params(**kwargs).execute()
        body = WorkTimeSerializer.serializer(deleted_worked_time)
        status = 201
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
