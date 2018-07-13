from PayDevs.interactors import Interactor
from project.entities import Project


class GetProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, title, *args, **kwargs):
        self.title = title
        return self

    def execute(self):
        return self.project_repo.get_project(title=self.title)



class CreateProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, title, description, user, type_of_payment, *args, **kwargs):
        self.title = title
        self.description = description
        self.user = user
        self.type_of_payment = type_of_payment
        return self
    
    def execute(self):
        return self.project_repo.create_project(self.title, self.description, self.user, self.type_of_payment)
        
