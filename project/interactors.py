from PayDevs.interactors import Interactor


#------------------------ Project ---------------------------------------------#
from project.entities import Project


class GetProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, project_id, logged_id=None, **kwargs):
        self.logged_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        return self.project_repo.get(logged_id=self.logged_id, project_id=self.project_id)



class CreateProjectInteractor(Interactor):

    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, title, description, type_of_payment, rate, **kwargs):
        self.logged_id = logged_id
        self.title = title
        self.description = description
        self.type_of_payment = type_of_payment
        self.rate = rate
        return self
    
    def execute(self):
        self.validate_user_project.validate_pemission(self.logged_id)
        project = Project(user_id=self.logged_id, title=self.title,
                          description=self.description,
                          type_of_payment=self.type_of_payment)
        return self.project_repo.create(project)




class UpdateProjectInteractor(Interactor):

    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, title, description, start_date,
                   end_date, type_of_payment, status, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.type_of_payment = type_of_payment
        self.status = status
        return self

    def execute(self):
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_pemission(self.user_id, project.user_id)
        title = self.title if self.title is not None else project.title
        description = self.description if self.description is not None else project.description
        start_date = self.start_date if self.start_date is not None else project.start_date
        end_date = self.end_date if self.end_date is not None else project.end_date
        type_of_payment = self.type_of_payment if self.type_of_payment is not None else project.type_of_payment
        status = self.status if self.status else project.status
        update_project = Project(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            type_of_payment=type_of_payment,
            status=status
        )
        return self.project_repo.update(update_project)



class DeleteProjectInteractor(Interactor):

    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self, *args, **kwargs):
        project = self.project_repo.get(project_id=self.project_repo)
        self.validate_user_project.validate_pemission(self.user_id, project.user_id)
        return self.project_repo.delete(project.id)




class GetAllProjectsInteractor(Interactor):

    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, **kwargs):
        self.user_id = logged_id
        return self

    def execute(self):
        self.validate_user_project.validate_pemission(self.user_id)
        return self.project_repo.get_all(self.user_id)



class GetTotalInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self):
        return self.project_repo.get_total(self.user_id, self.project_id)



#--------------------------- Work Task ----------------------------------------#



class GetTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.task_id = kwargs.get('task_id')
        self.title = kwargs.get('title')
        return self

    def execute(self):
        return self.work_task_repo.get(user_id=self.user_id, project_id=self.project_id,
                                       task_id=self.task_id, title=self.title)




class CreateTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.price = kwargs.get('price')
        return self

    def execute(self):
        return self.work_task_repo.create(user_id=self.user_id, project_id=self.project_id, title=self.title,
                                                    description=self.description, price=self.price)





class UpdateTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.task_id = kwargs.get('task_id')
        self.new_attrs = {
            'title': kwargs.get('title'),
            'description': kwargs.get('description'),
            'price': kwargs.get('price'),
            'completed': kwargs.get('completed'),
            'paid': kwargs.get('paid')
        }
        return self

    def execute(self):
        return self.work_task_repo.update(user_id=self.user_id, project_id=self.project_id, task_id=self.task_id,
                                          new_attrs=self.new_attrs)



class DeleteTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.task_id = kwargs.get('task_id')
        return self

    def execute(self, *args, **kwargs):
        return self.work_task_repo.delete(user_id=self.user_id, project_id=self.project_id, task_id=self.task_id)



class GetAllTasksInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self):
        return self.work_task_repo.get_all(user_id=self.user_id, project_id=self.project_id)
