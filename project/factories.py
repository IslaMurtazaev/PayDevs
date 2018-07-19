from project.repositories import ProjectRepo, WorkTaskRepo, WorkDayRepo, WorkTimeRepo
from project.views import ProjectView, CreateProjectView, AllProjectsView, TotalView, CreateTaskView, \
            GetAllTasksView, UpdateProjectView, GetTaskView, UpdateTaskView, DeleteProjectView, DeleteTaskView, \
            CreateWorkDayView, CreateWorkTimeView, GetWorkDayView, GetWorkTimeView, UpdateWorkDayView, UpdateWorkTimeView, \
            DeleteWorkDayView, DeleteWorkTimeView
from project.interactors import GetProjectInteractor, CreateProjectInteractor, GetAllProjectsInteractor, \
            GetTotalInteractor, CreateTaskInteractor, GetAllTasksInteractor, UpdateProjectInteractor, GetTaskInteractor, \
            UpdateTaskInteractor, DeleteProjectInteractor, DeleteTaskInteractor, CreateWorkDayInteractor, \
            CreateWorkTimeInteractor, GetWorkDayInteractor, GetWorkTimeInteractor, UpdateWorkDayInteractor, \
            UpdateWorkTimeInteractor, DeleteWorkDayInteractor, DeleteWorkTimeInteractor
                                 


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




class UpdateProjectInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return UpdateProjectInteractor(project_repo)





class DeleteProjectInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return DeleteProjectInteractor(project_repo)


def delete_project_factory():
    delete_project_interactor = DeleteProjectInteractorFactory.get()
    return DeleteProjectView(delete_project_interactor)




class GetAllProjectsInteractorFactory(object):
    @staticmethod
    def get():
        project_repo = ProjectRepoFactory.get()
        return GetAllProjectsInteractor(project_repo)


def get_all_projects_factory():
    get_all_projects_interactor = GetAllProjectsInteractorFactory.get()
    return AllProjectsView(get_all_projects_interactor)


def update_project_factory():
    update_project_interactor = UpdateProjectInteractorFactory.get()
    return UpdateProjectView(update_project_interactor)




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




class GetTaskInteractorFactory(object):
    @staticmethod
    def get():
        work_task_repo = WorkTaskRepoFactory.get()
        return GetTaskInteractor(work_task_repo)



def get_task_factory():
    get_task_interactor = GetTaskInteractorFactory.get()
    return GetTaskView(get_task_interactor)



class CreateTaskInteractorFactory(object):
    @staticmethod
    def get():
        work_task_repo = WorkTaskRepoFactory.get()
        return CreateTaskInteractor(work_task_repo)


def create_task_factory():
    create_task_interactor = CreateTaskInteractorFactory.get()
    return CreateTaskView(create_task_interactor)




class UpdateTaskInteractorFactory(object):
    @staticmethod
    def get():
        work_task_repo = WorkTaskRepoFactory.get()
        return UpdateTaskInteractor(work_task_repo)


def update_task_factory():
    update_task_interactor = UpdateTaskInteractorFactory.get()
    return UpdateTaskView(update_task_interactor)




class DeleteTaskInteractorFactory(object):
    @staticmethod
    def get():
        task_repo = WorkTaskRepoFactory.get()
        return DeleteTaskInteractor(task_repo)


def delete_task_factory():
    delete_task_interactor = DeleteTaskInteractorFactory.get()
    return DeleteTaskView(delete_task_interactor)




class GetAllTasksInteractorFactory(object):
    @staticmethod
    def get():
        work_task_repo = WorkTaskRepo()
        return GetAllTasksInteractor(work_task_repo)


def get_all_tasks_factory():
    get_all_tasks_interactor = GetAllTasksInteractorFactory.get()
    return GetAllTasksView(get_all_tasks_interactor)


# -------------------------- Work Day -------------------------------------------- #

class WorkDayRepoFactory(object):
    @staticmethod
    def get():
        return WorkDayRepo()



class GetWorkDayInteractorFactory(object):
    @staticmethod
    def get():
        work_day_repo = WorkDayRepoFactory.get()
        return GetWorkDayInteractor(work_day_repo)


def get_work_day_factory():
    get_work_day_interactor = GetWorkDayInteractorFactory.get()
    return GetWorkDayView(get_work_day_interactor)



class CreateWorkDayInteractorFactory(object):
    @staticmethod
    def get():
        work_day_repo = WorkDayRepoFactory.get()
        return CreateWorkDayInteractor(work_day_repo)


def create_work_day_factory():
    create_work_day_interactor = CreateWorkDayInteractorFactory.get()
    return CreateWorkDayView(create_work_day_interactor)



class UpdateWorkDayInteractorFactory(object):
    @staticmethod
    def get():
        work_day_repo = WorkDayRepoFactory.get()
        return UpdateWorkDayInteractor(work_day_repo)


def update_work_day_factory():
    update_work_day_interactor = UpdateWorkDayInteractorFactory.get()
    return UpdateWorkDayView(update_work_day_interactor)




class DeleteWorkDayInteractorFactory(object):
    @staticmethod
    def get():
        work_day_repo = WorkDayRepoFactory.get()
        return DeleteWorkDayInteractor(work_day_repo)


def delete_work_day_factory():
    delete_work_day_interactor = DeleteWorkDayInteractorFactory.get()
    return DeleteWorkDayView(delete_work_day_interactor)


# ------------------------ Work Time ------------------------------------- #

class WorkTimeRepoFactory(object):
    @staticmethod
    def get():
        return WorkTimeRepo()



class GetWorkTimeInteractorFactory(object):
    @staticmethod
    def get():
        work_time_repo = WorkTimeRepoFactory.get()
        return GetWorkTimeInteractor(work_time_repo)


def get_work_time_factory():
    get_work_time_interactor = GetWorkTimeInteractorFactory.get()
    return GetWorkTimeView(get_work_time_interactor)



class CreateWorkTimeInteractorFactory(object):
    @staticmethod
    def get():
        work_time_repo = WorkTimeRepoFactory.get()
        return CreateWorkTimeInteractor(work_time_repo)


def create_work_time_factory():
    create_work_time_interactor = CreateWorkTimeInteractorFactory.get()
    return CreateWorkTimeView(create_work_time_interactor)



class UpdateWorkTimeInteractorFactory(object):
    @staticmethod
    def get():
        work_time_repo = WorkTimeRepoFactory.get()
        return UpdateWorkTimeInteractor(work_time_repo)


def update_work_time_factory():
    update_work_time_interactor = UpdateWorkTimeInteractorFactory.get()
    return UpdateWorkTimeView(update_work_time_interactor)



class DeleteWorkTimeInteractorFactory(object):
    @staticmethod
    def get():
        work_time_repo = WorkTimeRepoFactory.get()
        return DeleteWorkTimeInteractor(work_time_repo)


def delete_work_time_factory():
    delete_work_time_interactor = DeleteWorkTimeInteractorFactory.get()
    return DeleteWorkTimeView(delete_work_time_interactor)
