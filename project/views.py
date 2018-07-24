from project.serializers import ProjectSerializer, ProjectListSerializer, WorkTaskSerializer, WorkTaskListSerializer, \
    WorkDaySerializer, WorkDayListSerializer, WorkTimeSerializer, WorkTimeListSerializer
from PayDevs.decorators import serialize_exception
from PayDevs.constants import StatusCodes

# ------------------------ Project ---------------------------------------------#

class ProjectView(object):

    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        project = self.get_project_interactor.set_params(**kwargs).execute()

        body = ProjectSerializer.serialize(project)
        status = StatusCodes.OK
        return body, status



class CreateProjectView(object):

    def __init__(self, create_project_interactor):
        self.create_project_interactor = create_project_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        project = self.create_project_interactor.set_params(**kwargs).execute()
        body = ProjectSerializer.serialize(project)
        status = StatusCodes.CREATED
        return body, status



class UpdateProjectView(object):

    def __init__(self, update_project_interactor):
        self.update_project_interactor = update_project_interactor

    @serialize_exception
    def put(self, *args, **kwargs):
        updated_project = self.update_project_interactor.set_params(**kwargs).execute()

        body = ProjectSerializer.serialize(updated_project)
        status = StatusCodes.OK
        return body, status



class DeleteProjectView(object):

    def __init__(self, delete_project_interactor):
        self.delete_project_interactor = delete_project_interactor

    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_project = self.delete_project_interactor.set_params(**kwargs).execute()

        body = ProjectSerializer.serialize(deleted_project)
        status = StatusCodes.OK
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



class TotalView(object):

    def __init__(self, get_type_of_payment_interactor, get_timestamp_interactor, get_worked_interactor, get_total_interactor, get_bill_interactor):
        self.get_type_of_payment_interactor = get_type_of_payment_interactor
        self.get_timestamp_interactor = get_timestamp_interactor
        self.get_worked_interactor = get_worked_interactor #TODO make one interactor
        self.get_total_interactor = get_total_interactor
        self.get_bill_interactor = get_bill_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        type_of_payment = self.get_type_of_payment_interactor.set_params(**kwargs).execute()
        worked = self.get_worked_interactor.set_params(type_of_payment, **kwargs).execute()
        timestamp = self.get_timestamp_interactor.set_params(type_of_payment, worked, **kwargs).execute()
        total = self.get_total_interactor.set_params(type_of_payment, worked, **kwargs).execute()
        bill = self.get_bill_interactor.set_params(type_of_payment, timestamp, total, **kwargs).execute()

        body = bill
        status = StatusCodes.OK
        return body, status


# --------------------------- Work Task ----------------------------------------#

class GetTaskView(object):

    def __init__(self, get_task_interactor):
        self.get_task_interactor = get_task_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        task = self.get_task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serialize(task)
        status = StatusCodes.OK
        return body, status



class CreateTaskView(object):

    def __init__(self, create_task_interactor):
        self.create_task_interactor = create_task_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        task = self.create_task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serialize(task)
        status = StatusCodes.CREATED
        return body, status



class UpdateTaskView(object):

    def __init__(self, update_task_interactor):
        self.update_task_interactor = update_task_interactor

    @serialize_exception
    def put(self, *args, **kwargs):
        modified_task = self.update_task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serialize(modified_task)
        status = StatusCodes.OK
        return body, status



class DeleteTaskView(object):

    def __init__(self, delete_task_interactor):
        self.delete_task_interactor = delete_task_interactor

    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_task = self.delete_task_interactor.set_params(**kwargs).execute()

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


# -------------------------- Work Day ----------------------------- #

class GetWorkDayView(object):

    def __init__(self, get_work_day_interactor):
        self.get_work_day_interactor = get_work_day_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        worked_day = self.get_work_day_interactor.set_params(**kwargs).execute()

        body = WorkDaySerializer.serialize(worked_day)
        status = StatusCodes.OK
        return body, status



class CreateWorkDayView(object):

    def __init__(self, create_work_day_interactor):
        self.create_work_day_interactor = create_work_day_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        created_worked_day = self.create_work_day_interactor.set_params(**kwargs).execute()

        body = WorkDaySerializer.serialize(created_worked_day)
        status = StatusCodes.OK
        return body, status



class UpdateWorkDayView(object):

    def __init__(self, update_work_day_interactor):
        self.update_work_day_interactor = update_work_day_interactor

    @serialize_exception
    def put(self, *args, **kwargs):
        updated_worked_day = self.update_work_day_interactor.set_params(**kwargs).execute()

        body = WorkDaySerializer.serialize(updated_worked_day)
        status = StatusCodes.OK
        return body, status



class DeleteWorkDayView(object):

    def __init__(self, delete_work_day_interactor):
        self.delete_work_day_interactor = delete_work_day_interactor

    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_worked_day = self.delete_work_day_interactor.set_params(**kwargs).execute()

        body = WorkDaySerializer.serialize(deleted_worked_day)
        status = StatusCodes.OK
        return body, status



class GetAllWorkDaysView(object):

    def __init__(self, get_all_work_days_interactor):
        self.get_all_work_days_interactor = get_all_work_days_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        worked_day = self.get_all_work_days_interactor.set_params(**kwargs).execute()

        body = WorkDayListSerializer.serialize(worked_day)
        status = StatusCodes.OK
        return body, status


# ------------------------------ Work Time ------------------------------ #

class GetWorkTimeView(object):

    def __init__(self, get_work_time_interactor):
        self.get_work_time_interactor = get_work_time_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        worked_time = self.get_work_time_interactor.set_params(**kwargs).execute()

        body = WorkTimeSerializer.serialize(worked_time)
        status = StatusCodes.OK
        return body, status



class CreateWorkTimeView(object):

    def __init__(self, create_work_time_interactor):
        self.create_work_time_interactor = create_work_time_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        created_worked_time = self.create_work_time_interactor.set_params(**kwargs).execute()

        body = WorkTimeSerializer.serialize(created_worked_time)
        status = StatusCodes.CREATED
        return body, status



class UpdateWorkTimeView(object):

    def __init__(self, update_work_time_interactor):
        self.update_work_time_interactor = update_work_time_interactor

    @serialize_exception
    def put(self, *args, **kwargs):
        updated_worked_time = self.update_work_time_interactor.set_params(**kwargs).execute()

        body = WorkTimeSerializer.serialize(updated_worked_time)
        status = StatusCodes.OK
        return body, status



class DeleteWorkTimeView(object):

    def __init__(self, delete_work_time_interactor):
        self.delete_work_time_interactor = delete_work_time_interactor

    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_worked_time = self.delete_work_time_interactor.set_params(**kwargs).execute()

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
