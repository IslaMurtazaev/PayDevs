from project.repositories import ProjectRepo, WorkTaskRepo
from project.views import ProjectView, CreateProjectView, AllProjectsView, TotalView, CreateTaskView
from project.interactors import GetProjectInteractor, CreateProjectInteractor, GetAllProjectsInteractor, \
                                 GetTotalInteractor, CreateTaskInteractor
                                 


#------------------------ Project ---------------------------------------------#

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




class GetTotalInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return GetTotalInteractor(project_repo)


def get_total_factory():
    get_total_interactor = GetTotalInteractorFactory.get()
    return TotalView(get_total_interactor)


#--------------------------- Work Task ----------------------------------------#

class WorkTaskRepoFactory(object):
    @staticmethod
    def get():
        return WorkTaskRepo()


class CreateTaskInteractorFactory(object):
    @staticmethod
    def get():
        work_task_repo = WorkTaskRepoFactory.get()
        return CreateTaskInteractor(work_task_repo)


def create_task_factory():
    create_task_interactor = CreateTaskInteractorFactory.get()
    return CreateTaskView(create_task_interactor)
