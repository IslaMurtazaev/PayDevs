from PayDevs.interactors import Interactor
from project.entities import Project


class GetProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, title, **kwargs):
        self.title = title
        return self

    def execute(self, *args, **kwargs):
        return self.project_repo.get_project(title=self.title)
        
