from project.serializers import ProjectSerializer, ProjectListSerializer, WorkTaskSerializer, WorkTaskListSerializer, \
    WorkDaySerializer, WorkDayListSerializer, WorkTimeSerializer
from PayDevs.decorators import serialize_exception


# ------------------------ Project ---------------------------------------------#

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




class AllProjectsView(object):

    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        projects = self.get_project_interactor.set_params(**kwargs).execute()

        body = ProjectListSerializer.serializer(projects)
        status = 200
        return body, status



class TotalView(object):
    def __init__(self, get_total_interactor):
        self.get_total_interactor = get_total_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        total = self.get_total_interactor.set_params(**kwargs).execute()

        body = total
        status = 200
        return body, status


# --------------------------- Work Task ----------------------------------------#

class TaskView(object):
    def __init__(self, get_task_interactor):
        self.task_interactor = get_task_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        task = self.task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serializer(task)
        status = 200
        return body, status

    @serialize_exception
    def post(self, *args, **kwargs):
        task = self.task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serializer(task)
        status = 201
        return body, status

    @serialize_exception
    def put(self, *args, **kwargs):
        modified_task = self.task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serializer(modified_task)
        status = 200
        return body, status

    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_task = self.task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serializer(deleted_task)
        status = 200
        return body, status




class GetAllTasksView(object):
    def __init__(self, get_all_tasks_interactor):
        self.get_all_tasks_interactor = get_all_tasks_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        tasks = self.get_all_tasks_interactor.set_params(**kwargs).execute()

        body = WorkTaskListSerializer.serializer(tasks)
        status = 200
        return body, status



# -------------------------- Work Day ----------------------------- #


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




