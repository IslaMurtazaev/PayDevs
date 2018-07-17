from project.serializers import ProjectSerializer, ProjectListSerializer, WorkTaskSerializer, WorkTaskListSerializer
from PayDevs.decorators import serialize_exception


#------------------------ Project ---------------------------------------------#

class ProjectView(object):

    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        title = kwargs.get('title')
        user_id = kwargs.get('user_id')
        project_id = kwargs.get('project_id')
        project = self.get_project_interactor.set_params(user_id=user_id, title=title, project_id=project_id).execute()

        body = ProjectSerializer.serializer(project)
        status = 200
        return body, status




class CreateProjectView(object):

    def __init__(self, create_project_interactor):
        self.create_project_interactor = create_project_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        user_id = kwargs.get('user_id')
        type_of_payment = kwargs.get('type_of_payment')
        rate = kwargs.get('rate')
        project = self.create_project_interactor.set_params(title=title, description=description, user_id=user_id,
                                                            type_of_payment=type_of_payment, rate=rate).execute()
        body = ProjectSerializer.serializer(project)
        status = 201
        return body, status




class AllProjectsView(object):

    def __init__(self, get_project_interactor):
        self.get_project_interactor = get_project_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        user_id = kwargs.get('user_id')
        projects = self.get_project_interactor.set_params(user_id).execute()

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

        user_id = kwargs.get('user_id')
        project_id = kwargs.get('project_id')
        updated_project = self.update_project_interactor.set_params(user_id=user_id, project_id=project_id,
                                                                    project_new_attrs=project_new_attrs).execute()

        body = ProjectSerializer.serializer(updated_project)
        status = 200
        return body, status



class TotalView(object):

    def __init__(self, get_total_interactor):
        self.get_total_interactor = get_total_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        user_id = kwargs.get('user_id')
        project_id = kwargs.get('project_id')
        total = self.get_total_interactor.set_params(user_id=user_id, project_id=project_id).execute()

        body = total
        status = 200
        return body, status



#--------------------------- Work Task ----------------------------------------#

class GetTaskView(object):

    def __init__(self, get_task_interactor):
        self.get_task_interactor = get_task_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        user_id = kwargs.get('user_id')
        project_id = kwargs.get('project_id')
        task_id = kwargs.get('task_id')
        task_title = kwargs.get('title')
        task = self.get_task_interactor.set_params(user_id=user_id, project_id=project_id, task_id=task_id, title=task_title).execute()

        body = WorkTaskSerializer.serializer(task)
        status = 200
        return body, status



class CreateTaskView(object):

    def __init__(self, create_task_interactor):
        self.create_task_interactor = create_task_interactor

    @serialize_exception
    def post(self, *args, **kwargs):
        user_id = kwargs.get('user_id')
        project_id = kwargs.get('project_id')
        title = kwargs.get('title')
        description = kwargs.get('description')
        price = kwargs.get('price')
        task = self.create_task_interactor.set_params(user_id=user_id, project_id=project_id, title=title,
                                                           description=description, price=price).execute()
        body = WorkTaskSerializer.serializer(task)
        status = 201
        return body, status



class GetAllTasksView(object):

    def __init__(self, get_all_tasks_interactor):
        self.get_all_tasks_interactor = get_all_tasks_interactor

    @serialize_exception
    def get(self, *args, **kwargs):
        user_id = kwargs.get('user_id')
        project_id = kwargs.get('project_id')
        tasks = self.get_all_tasks_interactor.set_params(user_id=user_id, project_id=project_id).execute()

        body = WorkTaskListSerializer.serializer(tasks)
        status = 200
        return body, status
