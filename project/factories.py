from project.views import ProjectView
from project.repositories import ProjectRepo
from project.interactors import GetProjectInteractor


class ProjectRepoFactory(object):
    @staticmethod
    def get():
        return ProjectRepo()


class GetProjectInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return GetProjectInteractor(project_repo)


def get_project_factory():
    get_project_interactor = GetProjectInteractorFactory.get()
    return ProjectView(get_project_interactor)
