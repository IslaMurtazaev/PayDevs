from project.factories.repo_factories import ProjectRepoFactory, WorkTaskRepoFactory, MonthPaymentRepoFactory
from project.factories.validator_factories import UserPermissionsValidatorFactory, ProjectDateTimeValidatorFactory
from project.interactors import CreateProjectInteractor, UpdateProjectInteractor, DeleteProjectInteractor, \
    GetProjectInteractor, GetAllProjectsInteractor, CreateTaskInteractor, GetTaskInteractor, UpdateTaskInteractor, \
    DeleteTaskInteractor, GetAllTasksInteractor, CreateMonthPaymentInteractor, GetMonthPaymentInteractor, \
    UpdateMonthPaymentInteractor, DeleteMonthPaymentInteractor, GetAllMonthPaymentsInteractor


class CreateProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        project_date_time = ProjectDateTimeValidatorFactory.create()
        return CreateProjectInteractor(project_repo, validate_user_project, project_date_time)


class UpdateProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return UpdateProjectInteractor(project_repo, validate_user_project)


class DeleteProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return DeleteProjectInteractor(project_repo, validate_user_project)



class GetProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return GetProjectInteractor(project_repo, validate_user_project)


class GetAllProjectsInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return GetAllProjectsInteractor(project_repo, validate_user_project)



class CreateTaskInteractorFactory(object):
    @staticmethod
    def create():
        create_task_repo = WorkTaskRepoFactory().create()
        create_project_repo = ProjectRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return CreateTaskInteractor(create_task_repo, create_project_repo, validate_user_project)



class GetTaskInteractorFactory(object):
    @staticmethod
    def create():
        create_task_repo = WorkTaskRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return GetTaskInteractor(create_task_repo, validate_user_project)





class UpdateTaskInteractorFactory(object):
    @staticmethod
    def create():
        create_task_repo = WorkTaskRepoFactory().create()
        create_project_repo = ProjectRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return UpdateTaskInteractor(create_task_repo, create_project_repo, validate_user_project)


class DeleteTaskInteractorFactory(object):
    @staticmethod
    def create():
        create_task_repo = WorkTaskRepoFactory().create()
        create_project_repo = ProjectRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return DeleteTaskInteractor(create_task_repo, create_project_repo, validate_user_project)


class GetAllTaskInteractorFactory(object):
    @staticmethod
    def create():
        create_task_repo = WorkTaskRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        create_project_repo = ProjectRepoFactory().create()
        return GetAllTasksInteractor(create_task_repo, create_project_repo, validate_user_project)



class GetMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory().create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return GetMonthPaymentInteractor(month_payment_repo, user_permission_validator)


class CreateMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory().create()
        project_repo = ProjectRepoFactory().create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return CreateMonthPaymentInteractor(month_payment_repo, project_repo, user_permission_validator)


class UpdateMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory().create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return UpdateMonthPaymentInteractor(month_payment_repo, user_permission_validator)


class DeleteMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory().create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return DeleteMonthPaymentInteractor(month_payment_repo, user_permission_validator)


class GetAllMonthPaymentsInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory().create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return GetAllMonthPaymentsInteractor(month_payment_repo, user_permission_validator)
