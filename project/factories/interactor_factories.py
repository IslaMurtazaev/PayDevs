from account.factories.repo_factories import UserRepoFactory
from project.factories.repo_factories import ProjectRepoFactory, WorkTaskRepoFactory, MonthPaymentRepoFactory, \
    WorkedDayRepoFactory, HourPaymentRepoFactory, WorkTimeRepoFactory
from project.factories.validator_factories import PermissionValidatorFactory, FieldValidatorFactory
from project.interactors import CreateProjectInteractor, UpdateProjectInteractor, DeleteProjectInteractor, \
    GetProjectInteractor, GetAllProjectsInteractor, CreateTaskInteractor, GetTaskInteractor, UpdateTaskInteractor, \
    DeleteTaskInteractor, GetAllTasksInteractor, CreateMonthPaymentInteractor, GetMonthPaymentInteractor, \
    UpdateMonthPaymentInteractor, DeleteMonthPaymentInteractor, GetAllMonthPaymentsInteractor, \
    CreateHourPaymentInteractor, GetHourPaymentInteractor, UpdateHourPaymentInteractor, DeleteHourPaymentInteractor, \
    GetAllHourPaymentInteractor, CreateWorkTimeInteractor, GetWorkTimeInteractor, UpdateWorkTimeInteractor, \
    DeleteWorkTimeInteractor, GetAllWorkTimeInteractor, GetWorkedDayInteractor, CreateWorkedDayInteractor, \
    UpdateWorkedDayInteractor, DeleteWorkedDayInteractor, GetAllWorkedDaysInteractor, ProjectGetTotalInteractor


class CreateProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return CreateProjectInteractor(project_repo, permission_validator, field_validator)


class UpdateProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return UpdateProjectInteractor(project_repo, permission_validator, field_validator)


class DeleteProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return DeleteProjectInteractor(project_repo, permission_validator)


class GetProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return GetProjectInteractor(project_repo, permission_validator)


class GetAllProjectsInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return GetAllProjectsInteractor(project_repo, permission_validator)


class GetTotalProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        user_repo = UserRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        datetime_validator = FieldValidatorFactory.create()
        return ProjectGetTotalInteractor(project_repo, user_repo, permission_validator, datetime_validator)




class CreateTaskInteractorFactory(object):
    @staticmethod
    def create():
        task_repo = WorkTaskRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        field_validator = FieldValidatorFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return CreateTaskInteractor(task_repo, project_repo, permission_validator, field_validator)



class GetTaskInteractorFactory(object):
    @staticmethod
    def create():
        task_repo = WorkTaskRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return GetTaskInteractor(task_repo, permission_validator)



class UpdateTaskInteractorFactory(object):
    @staticmethod
    def create():
        task_repo = WorkTaskRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return UpdateTaskInteractor(task_repo, project_repo, permission_validator)


class DeleteTaskInteractorFactory(object):
    @staticmethod
    def create():
        task_repo = WorkTaskRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return DeleteTaskInteractor(task_repo, permission_validator)


class GetAllTasksInteractorFactory(object):
    @staticmethod
    def create():
        task_repo = WorkTaskRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return GetAllTasksInteractor(task_repo, permission_validator, field_validator)




class CreateMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return CreateMonthPaymentInteractor(month_payment_repo, project_repo, permission_validator, field_validator)


class GetMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return GetMonthPaymentInteractor(month_payment_repo, permission_validator)


class UpdateMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return UpdateMonthPaymentInteractor(month_payment_repo, project_repo, permission_validator, field_validator)


class DeleteMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return DeleteMonthPaymentInteractor(month_payment_repo, permission_validator)


class GetAllMonthPaymentsInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return GetAllMonthPaymentsInteractor(month_payment_repo, permission_validator)



class CreateWorkedDayInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return CreateWorkedDayInteractor(worked_day_repo, month_payment_repo, project_repo, permission_validator,
                                         field_validator)


class GetWorkedDayInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return GetWorkedDayInteractor(worked_day_repo, permission_validator)


class UpdateWorkedDayInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return UpdateWorkedDayInteractor(worked_day_repo, month_payment_repo, project_repo, permission_validator,
                                         field_validator)


class DeleteWorkedDayInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return DeleteWorkedDayInteractor(worked_day_repo, permission_validator)


class GetAllWorkedDaysInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        month_payment_repo = MonthPaymentRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return GetAllWorkedDaysInteractor(worked_day_repo, month_payment_repo, permission_validator)




class CreateHourPaymentInteractorFactory():
    @staticmethod
    def create():
        hour_payment_repo = HourPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return CreateHourPaymentInteractor(hour_payment_repo, project_repo, permission_validator,
                                           field_validator)


class GetHourPaymentInteractorFactory(object):
    @staticmethod
    def create():
        hour_payment_repo = HourPaymentRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return GetHourPaymentInteractor(hour_payment_repo, permission_validator)


class GetAllHourPaymentInteractorFactory(object):
    @staticmethod
    def create():
        hour_payment_repo = HourPaymentRepoFactory.create()
        validate_user_project = PermissionValidatorFactory.create()
        return GetAllHourPaymentInteractor(hour_payment_repo, validate_user_project)


class UpdateHourPaymentInteractorFactory(object):
    @staticmethod
    def create():
        hour_payment_repo = HourPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return UpdateHourPaymentInteractor(hour_payment_repo, project_repo, permission_validator, field_validator)


class DeleteHourPaymentInteractorFactory(object):
    @staticmethod
    def create():
        hour_payment_repo = HourPaymentRepoFactory.create()
        permission_validator = PermissionValidatorFactory().create()
        return DeleteHourPaymentInteractor(hour_payment_repo, permission_validator)




class CreateWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        hour_payment_repo = HourPaymentRepoFactory.create()
        permission_validator = PermissionValidatorFactory().create()
        field_validator = FieldValidatorFactory.create()
        return CreateWorkTimeInteractor(work_time_repo, hour_payment_repo,
                                        permission_validator, field_validator)


class GetWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        permission_validator = PermissionValidatorFactory().create()
        return GetWorkTimeInteractor(work_time_repo, permission_validator)


class UpdateWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        hour_payment_repo = HourPaymentRepoFactory().create()
        project_repo = ProjectRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        field_validator = FieldValidatorFactory.create()
        return UpdateWorkTimeInteractor(work_time_repo, project_repo, hour_payment_repo,
                                        permission_validator, field_validator)



class DeleteWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return DeleteWorkTimeInteractor(work_time_repo, permission_validator)



class GetAllWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        work_time_repo = WorkTimeRepoFactory.create()
        permission_validator = PermissionValidatorFactory.create()
        return GetAllWorkTimeInteractor(work_time_repo, permission_validator)
