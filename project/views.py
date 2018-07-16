from project.serializers import ProjectSerializer, ProjectListSerializer, WorkTaskSerializer, WorkTaskListSerializer
from PayDevs.decorators import serialize_exception
from account.models import UserORM
from project.models import ProjectORM



#------------------------ Project ---------------------------------------------#

class CreateProjectView(object):
    def __init__(self, create_project_interactor):
        self.create_project_interactor = create_project_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        user = UserORM.objects.get(id=kwargs.get('user_id'))
        type_of_payment = kwargs.get('type_of_payment')
        rate = kwargs.get('rate')
        project = self.create_project_interactor.set_params(title=title, description=description, user=user,
                                                            type_of_payment=type_of_payment, rate=rate).execute()
        body = ProjectSerializer.serializer(project)
        status = 201
        return body, status



class ProjectView(object):
    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        title = kwargs.get('title')
        user = UserORM.objects.get(id=kwargs.get('user_id'))
        project = self.get_project_interactor.set_params(user=user, title=title).execute()

        body = ProjectSerializer.serializer(project)
        status = 200
        return body, status



class AllProjectsView(object):
    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        user = UserORM.objects.get(id=kwargs.get('user_id'))
        projects = self.get_project_interactor.set_params(user).execute()

        body = ProjectListSerializer.serializer(projects)
        status = 200
        return body, status




class UpdateProjectView(object):
    def __init__(self, update_project_interactor):
        self.update_project_interactor = update_project_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        project_new_attrs = {
            'title': kwargs.get('title'),
            'start_date': kwargs.get('start_date'),
            'end_date': kwargs.get('end_date'),
            'type_of_payment': kwargs.get('type_of_payment'),
            'status': kwargs.get('status')
        }

        user = UserORM.objects.get(id=kwargs.get('user_id'))
        project_id = kwargs.get('project_id')
        updated_project = self.update_project_interactor.set_params(user=user, project_id=project_id,
                                                                    project_new_attrs=project_new_attrs).execute()

        body = ProjectSerializer.serializer(updated_project)
        status = 200
        return body, status



class TotalView(object):
    def __init__(self, get_total_interactor):
        self.get_total_interactor = get_total_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        user = UserORM.objects.get(id=kwargs.get('user_id'))
        title = kwargs.get('title')
        total = self.get_total_interactor.set_params(user=user, title=title).execute()

        body = total
        status = 200
        return body, status



#--------------------------- Work Task ----------------------------------------#


class CreateTaskView(object):
    def __init__(self, create_task_interactor):
        self.create_task_interactor = create_task_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        user = UserORM.objects.get(id=kwargs.get('user_id'))
        project = ProjectORM.objects.get(user=user, id=kwargs.get('project_id'))
        title = kwargs.get('title')
        description = kwargs.get('description')
        price = kwargs.get('price')
        work_task = self.create_task_interactor.set_params(project=project, title=title,
                                                           description=description, price=price).execute()
        body = WorkTaskSerializer.serializer(work_task)
        status = 201
        return body, status



class GetAllTasksView(object):
    def __init__(self, get_all_tasks_interactor):
        self.get_all_tasks_interactor = get_all_tasks_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        user = UserORM.objects.get(id=kwargs.get('user_id'))
        project = ProjectORM.objects.get(user=user, id=kwargs.get('project_id'))
        work_tasks = self.get_all_tasks_interactor.set_params(project=project).execute()

        body = WorkTaskListSerializer.serializer(work_tasks)
        status = 200
        return body, status
