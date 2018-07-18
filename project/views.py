from project.serializers import ProjectSerializer, ProjectListSerializer, WorkTaskSerializer, WorkTaskListSerializer
from PayDevs.decorators import serialize_exception


# ------------------------ Project ---------------------------------------------#

class ProjectView(object):
    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        project = self.get_project_interactor.set_params(**kwargs).execute()

        body = ProjectSerializer.serializer(project)
        status = 200
        return body, status



class CreateProjectView(object):
    def __init__(self, create_project_interactor):
        self.create_project_interactor = create_project_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        project = self.create_project_interactor.set_params(**kwargs).execute()
        body = ProjectSerializer.serializer(project)
        status = 201
        return body, status



class UpdateProjectView(object):

    def __init__(self, update_project_interactor):
        self.update_project_interactor = update_project_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        updated_project = self.update_project_interactor.set_params(**kwargs).execute()

        body = ProjectSerializer.serializer(updated_project)
        status = 200
        return body, status



class DeleteProjectView(object):

    def __init__(self, delete_project_interactor):
        self.delete_project_interactor = delete_project_interactor

    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_project = self.delete_project_interactor.set_params(**kwargs).execute()

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

class GetTaskView(object):
    def __init__(self, get_task_interactor):
        self.get_task_interactor = get_task_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        task = self.get_task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serializer(task)
        status = 200
        return body, status



class CreateTaskView(object):
    def __init__(self, create_task_interactor):
        self.create_task_interactor = create_task_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        task = self.create_task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serializer(task)
        status = 201
        return body, status



class UpdateTaskView(object):
    def __init__(self, update_task_interactor):
        self.update_task_interactor = update_task_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        modified_task = self.update_task_interactor.set_params(**kwargs).execute()

        body = WorkTaskSerializer.serializer(modified_task)
        status = 200
        return body, status



class DeleteTaskView(object):

    def __init__(self, delete_task_interactor):
        self.delete_task_interactor = delete_task_interactor

    @serialize_exception
    def delete(self, *args, **kwargs):
        deleted_task = self.delete_task_interactor.set_params(**kwargs).execute()

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
