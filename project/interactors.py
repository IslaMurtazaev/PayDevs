from PayDevs.interactors import Interactor


#------------------------ Project ---------------------------------------------#

class GetProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user_id, title, project_id, *args, **kwargs):
        self.user_id = user_id
        self.title = title
        self.project_id = project_id
        return self

    def execute(self):
        return self.project_repo.get(user_id=self.user_id, title=self.title, project_id=self.project_id)



class CreateProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user_id, title, description, type_of_payment, rate, *args, **kwargs):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.type_of_payment = type_of_payment
        self.rate = rate
        return self
    
    def execute(self):
        return self.project_repo.create(user_id=self.user_id, title=self.title, description=self.description,
                                                type_of_payment=self.type_of_payment, rate=self.rate)



class GetAllProjectsInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user_id, *args, **kwargs):
        self.user_id = user_id
        return self

    def execute(self):
        return self.project_repo.get_all(self.user_id)




class UpdateProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user_id, project_id, project_new_attrs, *args, **kwargs):
        self.user_id = user_id
        self.project_id = project_id
        self.project_new_attrs = project_new_attrs
        return self

    def execute(self):
        return self.project_repo.update(user_id=self.user_id, project_id=self.project_id,
                                                new_attrs=self.project_new_attrs)



class GetTotalInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user_id, project_id, *args, **kwargs):
        self.user_id = user_id
        self.project_id = project_id
        return self

    def execute(self):
        return self.project_repo.get_total(self.user_id, self.project_id)



#--------------------------- Work Task ----------------------------------------#

class GetTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, user_id, project_id, task_id, title):
        self.user_id = user_id
        self.project_id = project_id
        self.task_id = task_id
        self.title = title
        return self

    def execute(self):
        return self.work_task_repo.get(user_id=self.user_id, project_id=self.project_id, task_id=self.task_id, title=self.title)




class CreateTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, user_id, project_id, title, description, price, *args, **kwargs):
        self.user_id = user_id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.price = price
        return self

    def execute(self):
        return self.work_task_repo.create(user_id=self.user_id, project_id=self.project_id, title=self.title,
                                                    description=self.description, price=self.price)





class UpdateTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, user_id, project_id, task_id, new_attrs):
        self.user_id = user_id
        self.project_id = project_id
        self.task_id = task_id
        self.new_attrs = new_attrs
        return self

    def execute(self):
        return self.work_task_repo.update(user_id=self.user_id, project_id=self.project_id, task_id=self.task_id,
                                          new_attrs=self.new_attrs)



class GetAllTasksInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, user_id, project_id):
        self.user_id = user_id
        self.project_id = project_id
        return self

    def execute(self):
        return self.work_task_repo.get_all(user_id=self.user_id, project_id=self.project_id)
