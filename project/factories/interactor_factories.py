from project.factories.repo_factories import ProjectRepoFactory, WorkTaskRepoFactory, WorkDayRepoFactory, WorkTimeRepoFactory

from project.interactors import GetProjectInteractor, CreateProjectInteractor, GetAllProjectsInteractor, GetWorkedInteractor,\
            GetTotalInteractor, GetBillInteractor, CreateTaskInteractor, GetAllTasksInteractor, UpdateProjectInteractor, \
            GetTaskInteractor, UpdateTaskInteractor, DeleteProjectInteractor, DeleteTaskInteractor, CreateWorkDayInteractor, \
            CreateWorkTimeInteractor, GetWorkDayInteractor, GetWorkTimeInteractor, UpdateWorkDayInteractor, \
            UpdateWorkTimeInteractor, DeleteWorkDayInteractor, DeleteWorkTimeInteractor, GetTypeOfPaymentInteractor, \
            GetAllWorkDaysInteractor, GetWorkTimeListInteractor, GetTimestampInteractor


# ------------------------ Project --------------------------------------------- #

class GetProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        return GetProjectInteractor(project_repo)


class CreateProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        return CreateProjectInteractor(project_repo)


class UpdateProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        return UpdateProjectInteractor(project_repo)


class DeleteProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        return DeleteProjectInteractor(project_repo)


class GetAllProjectsInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        return GetAllProjectsInteractor(project_repo)


class GetTypeOfPaymentInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        return GetTypeOfPaymentInteractor(project_repo)


class GetTimestampInteractorFactory(object):
    @staticmethod
    def create():
        return GetTimestampInteractor()


class GetWorkedInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        return GetWorkedInteractor(project_repo)


class GetTotalInteractorFactory(object):
    @staticmethod
    def create():
        return GetTotalInteractor()


class GetBillInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        return GetBillInteractor(project_repo)


# --------------------------- Work Task ---------------------------------------- #

class GetTaskInteractorFactory(object):
    @staticmethod
    def create():
        work_task_repo = WorkTaskRepoFactory.create()
        return GetTaskInteractor(work_task_repo)


class CreateTaskInteractorFactory(object):
    @staticmethod
    def create():
        work_task_repo = WorkTaskRepoFactory.create()
        return CreateTaskInteractor(work_task_repo)


class UpdateTaskInteractorFactory(object):
    @staticmethod
    def create():
        work_task_repo = WorkTaskRepoFactory.create()
        return UpdateTaskInteractor(work_task_repo)


class DeleteTaskInteractorFactory(object):
    @staticmethod
    def create():
        task_repo = WorkTaskRepoFactory.create()
        return DeleteTaskInteractor(task_repo)


class GetAllTasksInteractorFactory(object):
    @staticmethod
    def create():
        work_task_repo = WorkTaskRepoFactory.create()
        return GetAllTasksInteractor(work_task_repo)


# -------------------------- Work Day -------------------------------------------- #

class GetWorkDayInteractorFactory(object):
    @staticmethod
    def create():
        work_day_repo = WorkDayRepoFactory.create()
        return GetWorkDayInteractor(work_day_repo)


class CreateWorkDayInteractorFactory(object):
    @staticmethod
    def create():
        work_day_repo = WorkDayRepoFactory.create()
        return CreateWorkDayInteractor(work_day_repo)


class UpdateWorkDayInteractorFactory(object):
    @staticmethod
    def create():
        work_day_repo = WorkDayRepoFactory.create()
        return UpdateWorkDayInteractor(work_day_repo)


class DeleteWorkDayInteractorFactory(object):
    @staticmethod
    def create():
        work_day_repo = WorkDayRepoFactory.create()
        return DeleteWorkDayInteractor(work_day_repo)


class GetAllWorkDaysInteractorFactory(object):
    @staticmethod
    def create():
        work_day_repo = WorkDayRepoFactory.create()
        return GetAllWorkDaysInteractor(work_day_repo)


# ------------------------ Work Time ------------------------------------- #

class GetWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        return GetWorkTimeInteractor(work_time_repo)


class CreateWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        return CreateWorkTimeInteractor(work_time_repo)


class UpdateWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        return UpdateWorkTimeInteractor(work_time_repo)


class DeleteWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        return DeleteWorkTimeInteractor(work_time_repo)


class GetWorkTimeListInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        return GetWorkTimeListInteractor(work_time_repo)
