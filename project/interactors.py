from PayDevs.interactors import Interactor
from project.entities import Project


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

    def set_params(self, user, title, description, type_of_payment, *args, **kwargs):
        self.user = user
        self.title = title
        self.description = description
        self.type_of_payment = type_of_payment
        return self
    
    def execute(self):
        return self.project_repo.create_project(self.user, self.title, self.description, self.type_of_payment)



class GetAllProjectsInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, user, *args, **kwargs):
        self.user = user
        return self

    def execute(self):
        return self.project_repo.get_all_projects(self.user)
