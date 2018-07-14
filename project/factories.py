from project.views import ProjectView, CreateProjectView, AllProjectsView
from project.repositories import ProjectRepo
from project.interactors import GetProjectInteractor, CreateProjectInteractor, GetAllProjectsInteractor


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




class GetAllProjectsInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return GetAllProjectsInteractor(project_repo)


def get_all_projects_factory():
    get_all_projects_interactor = GetAllProjectsInteractorFactory.get()
    return AllProjectsView(get_all_projects_interactor)
