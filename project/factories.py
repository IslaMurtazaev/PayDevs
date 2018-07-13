from project.views import ProjectView, CreateProjectView
from project.repositories import ProjectRepo
from project.interactors import GetProjectInteractor, CreateProjectInteractor


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



class CreateProjectInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return CreateProjectInteractor(project_repo)


def create_project_factory():
    create_project_interactor = CreateProjectInteractorFactory.get()
    return CreateProjectView(create_project_interactor)
