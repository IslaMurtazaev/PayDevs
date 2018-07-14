from PayDevs.interactors import Interactor
from project.entities import Project


#------------------------ Project ---------------------------------------------#

class GetProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user, title, *args, **kwargs):
        self.user = user
        self.title = title
        return self

    def execute(self):
        return self.project_repo.get_project(user=self.user, title=self.title)



class CreateProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user, title, description, type_of_payment, rate, *args, **kwargs):
        self.user = user
        self.title = title
        self.description = description
        self.type_of_payment = type_of_payment
        self.rate = rate
        return self
    
    def execute(self):
        return self.project_repo.create_project(self.user, self.title, self.description,\
                                                 self.type_of_payment, self.rate)



class GetAllProjectsInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user, *args, **kwargs):
        self.user = user
        return self

    def execute(self):
        return self.project_repo.get_all_projects(self.user)




class GetTotalInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user, title, *args, **kwargs):
        self.user = user
        self.title = title
        return self

    def execute(self):
        return self.project_repo.get_total(self.user, self.title)



#--------------------------- Work Task ----------------------------------------#


class CreateTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, project, title, description, price, *args, **kwargs):
        self.project = project
        self.title = title
        self.description = description
        self.price = price
        return self

    def execute(self):
        return self.work_task_repo.create_work_task(self.project, self.title, self.description, self.price)
