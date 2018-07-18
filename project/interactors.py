from PayDevs.interactors import Interactor


#------------------------ Project ---------------------------------------------#

class GetProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.title = kwargs.get('title')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self):
        return self.project_repo.get(user_id=self.user_id, title=self.title, project_id=self.project_id)



class CreateProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.type_of_payment = kwargs.get('type_of_payment')
        self.rate = kwargs.get('rate')
        return self
    
    def execute(self):
        return self.project_repo.create(user_id=self.user_id, title=self.title, description=self.description,
                                                type_of_payment=self.type_of_payment, rate=self.rate)



class GetAllProjectsInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        return self

    def execute(self):
        return self.project_repo.get_all(self.user_id)




class UpdateProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')

        self.project_new_attrs = {
            'title': kwargs.get('title'),
            'description': kwargs.get('description'),
            'start_date': kwargs.get('start_date'),
            'end_date': kwargs.get('end_date'),
            'type_of_payment': kwargs.get('type_of_payment'),
            'status': kwargs.get('status')
        }
        return self

    def execute(self):
        return self.project_repo.update(user_id=self.user_id, project_id=self.project_id,
                                                new_attrs=self.project_new_attrs)



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
        return self.work_task_repo.get(user_id=self.user_id, project_id=self.project_id, task_id=self.task_id, title=self.title)




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



class GetAllTasksInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self):
        return self.work_task_repo.get_all(user_id=self.user_id, project_id=self.project_id)
