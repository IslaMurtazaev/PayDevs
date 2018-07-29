from account.factories.repo_factories import UserRepoFactory
from project.factories.repo_factories import ProjectRepoFactory, WorkTaskRepoFactory, MonthPaymentRepoFactory, \
    WorkedDayRepoFactory, HourPaymentRepoFactory, WorkTimeRepoFactory
from project.factories.validator_factories import UserPermissionsValidatorFactory, ProjectDateTimeValidatorFactory, \
    RateValidatorFactory
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
        validate_user_project = UserPermissionsValidatorFactory.create()
        project_date_time = ProjectDateTimeValidatorFactory.create()
        return CreateProjectInteractor(project_repo, validate_user_project, project_date_time)


class UpdateProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        project_date_time_validator = ProjectDateTimeValidatorFactory.create()
        return UpdateProjectInteractor(project_repo, validate_user_project, project_date_time_validator)


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


class GetAllTasksInteractorFactory(object):
    @staticmethod
    def create():
        create_task_repo = WorkTaskRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        create_project_repo = ProjectRepoFactory().create()
        return GetAllTasksInteractor(create_task_repo, create_project_repo, validate_user_project)



class CreateMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        rate_validator = RateValidatorFactory.create()
        return CreateMonthPaymentInteractor(month_payment_repo, project_repo, user_permission_validator, rate_validator)


class GetMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return GetMonthPaymentInteractor(month_payment_repo, user_permission_validator)


class UpdateMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        rate_validator = RateValidatorFactory.create()
        return UpdateMonthPaymentInteractor(month_payment_repo, project_repo, user_permission_validator, rate_validator)


class DeleteMonthPaymentInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return DeleteMonthPaymentInteractor(month_payment_repo, project_repo, user_permission_validator)


class GetAllMonthPaymentsInteractorFactory(object):
    @staticmethod
    def create():
        month_payment_repo = MonthPaymentRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return GetAllMonthPaymentsInteractor(month_payment_repo, user_permission_validator)



class CreateWorkedDayInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        date_validator = ProjectDateTimeValidatorFactory.create()
        return CreateWorkedDayInteractor(worked_day_repo, month_payment_repo, project_repo, user_permission_validator,
                                         date_validator)


class GetWorkedDayInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return GetWorkedDayInteractor(worked_day_repo, user_permission_validator)


class UpdateWorkedDayInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        date_validator = ProjectDateTimeValidatorFactory.create()
        return UpdateWorkedDayInteractor(worked_day_repo, month_payment_repo, project_repo, user_permission_validator,
                                         date_validator)


class DeleteWorkedDayInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        month_payment_repo = MonthPaymentRepoFactory.create()
        project_repo = ProjectRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return DeleteWorkedDayInteractor(worked_day_repo, month_payment_repo, project_repo, user_permission_validator)


class GetAllWorkedDaysInteractorFactory(object):
    @staticmethod
    def create():
        worked_day_repo = WorkedDayRepoFactory.create()
        month_payment_repo = MonthPaymentRepoFactory.create()
        user_permission_validator = UserPermissionsValidatorFactory.create()
        return GetAllWorkedDaysInteractor(worked_day_repo, month_payment_repo, user_permission_validator)




class CreateHourPaymentInteractorFactory():
    @staticmethod
    def create():
        create_hour_payment_repo = HourPaymentRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        create_project_repo = ProjectRepoFactory().create()
        return CreateHourPaymentInteractor(create_hour_payment_repo, create_project_repo, validate_user_project)



class GetHourPaymentInteractorFactory(object):
    @staticmethod
    def create():
        create_hour_payment_repo = HourPaymentRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return GetHourPaymentInteractor(create_hour_payment_repo, validate_user_project)


class GetAllHourPaymentInteractorFactory(object):
    @staticmethod
    def create():
        create_hour_payment_repo = HourPaymentRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        create_project_repo = ProjectRepoFactory().create()
        return GetAllHourPaymentInteractor(create_hour_payment_repo, create_project_repo, validate_user_project)


class UpdateHourPaymentInteractorFactory(object):
    @staticmethod
    def create():
        create_hour_payment_repo = HourPaymentRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        create_project_repo = ProjectRepoFactory().create()
        return UpdateHourPaymentInteractor(create_hour_payment_repo, create_project_repo, validate_user_project)


class DeleteHourPaymentInteractorFactory(object):
    @staticmethod
    def create():
        create_hour_payment_repo = HourPaymentRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory().create()
        create_project_repo = ProjectRepoFactory().create()
        return DeleteHourPaymentInteractor(create_hour_payment_repo, create_project_repo, validate_user_project)



class CreateWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        create_hour_payment_repo = WorkTimeRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory().create()
        create_project_repo = HourPaymentRepoFactory().create()
        project_date_time = ProjectDateTimeValidatorFactory.create()
        return CreateWorkTimeInteractor(create_hour_payment_repo, create_project_repo,
                                        validate_user_project, project_date_time)




class GetWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        create_hour_payment_repo = WorkTimeRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory().create()
        create_project_repo = HourPaymentRepoFactory().create()
        return GetWorkTimeInteractor(create_hour_payment_repo, create_project_repo,
                                     validate_user_project)



class UpdateWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        create_work_time_repo = WorkTimeRepoFactory().create()
        create_hour_payment_repo = HourPaymentRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory().create()
        create_project_repo = ProjectRepoFactory().create()
        project_date_time = ProjectDateTimeValidatorFactory.create()
        return UpdateWorkTimeInteractor(create_work_time_repo, create_project_repo, create_hour_payment_repo,
                                        validate_user_project, project_date_time)



class DeleteWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        create_work_time_repo = WorkTimeRepoFactory().create()
        create_hour_payment_repo = HourPaymentRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory().create()
        create_project_repo = ProjectRepoFactory().create()
        return DeleteWorkTimeInteractor(create_work_time_repo, create_hour_payment_repo, create_project_repo,
                                        validate_user_project)



class GetAllWorkTimeInteractorFactory(object):
    @staticmethod
    def create():
        create_hour_payment_repo = WorkTimeRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory().create()
        create_project_repo = HourPaymentRepoFactory().create()
        return GetAllWorkTimeInteractor(create_hour_payment_repo, create_project_repo,
                                        validate_user_project)




class GetTotalProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        user_repo = UserRepoFactory().create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        project_date_time = ProjectDateTimeValidatorFactory.create()
        return ProjectGetTotalInteractor(project_repo, user_repo, validate_user_project, project_date_time)