from PayDevs.interactors import Interactor
from project.entities import Project, WorkTask, HourPayment, WorkTime, MonthPayment, WorkedDay


# ------------------------ Project ---------------------------------------- #

class GetProjectInteractor(Interactor):
    def __init__(self, project_repo, user_permission_validator):
        self.project_repo = project_repo
        self.user_permission_validator = user_permission_validator

    def set_params(self, project_id, logged_id=None, **kwargs):
        self.logged_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.user_permission_validator.validate_permission(self.logged_id)
        return self.project_repo.get(logged_id=self.logged_id, project_id=self.project_id)


class CreateProjectInteractor(Interactor):
    def __init__(self, project_repo, user_permission_validator, project_date_validator):
        self.project_repo = project_repo
        self.user_permission_validator = user_permission_validator
        self.project_date_validator = project_date_validator

    def set_params(self, logged_id, title, description, type_of_payment, start_date,
                   end_date=None, status=True, **kwargs):
        self.logged_id = logged_id
        self.title = title
        self.description = description
        self.type_of_payment = type_of_payment
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        return self

    def execute(self):
        self.user_permission_validator.validate_permission(self.logged_id)
        self.user_permission_validator.validate_type_of_payment(self.type_of_payment)

        start_date = self.project_date_validator.date_time_format(self.start_date)
        end_date = self.project_date_validator.date_time_format(self.end_date)

        project = Project(user_id=self.logged_id,
                          title=self.title,
                          description=self.description,
                          start_date=start_date,
                          end_date=end_date,
                          status=self.status,
                          type_of_payment=self.type_of_payment)
        return self.project_repo.create(project)


class UpdateProjectInteractor(Interactor):
    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, title=None, description=None, start_date=None,
                   end_date=None, type_of_payment=None, status=None, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.type_of_payment = type_of_payment
        self.status = status
        return self

    def execute(self):
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_permission(self.user_id, project.user_id)
        title = self.title if self.title is not None else project.title
        description = self.description if self.description is not None else project.description
        start_date = self.start_date if self.start_date is not None else project.start_date
        end_date = self.end_date if self.end_date is not None else project.end_date
        type_of_payment = self.type_of_payment if self.type_of_payment is not None else project.type_of_payment
        status = self.status if self.status else project.status
        self.validate_user_project.validate_type_of_payment(type_of_payment)

        update_project = Project(
            id=project.id,
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            type_of_payment=type_of_payment,
            status=status
        )
        return self.project_repo.update(update_project)


class DeleteProjectInteractor(Interactor):
    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self, *args, **kwargs):
        project = self.project_repo.get(project_id=self.project_id)
        self.validate_user_project.validate_permission(self.user_id, project.user_id)
        return self.project_repo.delete(project.id)


class GetAllProjectsInteractor(Interactor):
    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, **kwargs):
        self.user_id = logged_id
        return self

    def execute(self):
        self.validate_user_project.validate_permission(self.user_id)
        return self.project_repo.get_all(self.user_id)


class ProjectGetTotalInteractor(Interactor):
    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, logged_id, project_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        project = self.project_repo.get(self.project_id)
        return project.total


# --------------------------- Work Task ----------------------------------------#

class GetTaskInteractor(Interactor):
    def __init__(self, work_task_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, task_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.task_id = task_id
        return self

    def execute(self):
        self.validate_user_project.validate_permission(self.user_id)
        work_task = self.work_task_repo.get(self.task_id)
        self.validate_user_project.validate_permission(self.project_id, work_task.project_id)
        return work_task


class CreateTaskInteractor(Interactor):
    def __init__(self, work_task_repo, project_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project
        self.project_repo = project_repo

    def set_params(self, logged_id, project_id, title, description, price, paid=False, completed=False, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.price = price
        self.paid = paid
        self.completed = completed
        return self

    def execute(self):
        self.validate_user_project.validate_permission(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_permission(self.user_id, project.user_id)
        self.validate_user_project.validate_task_payment(project.type_of_payment)
        work_task = WorkTask(
            project_id=project.id,
            title=self.title,
            description=self.description,
            price=self.price,
            paid=self.paid,
            completed=self.completed
        )

        return self.work_task_repo.create(work_task)


class UpdateTaskInteractor(Interactor):
    def __init__(self, work_task_repo, project_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project
        self.project_repo = project_repo

    def set_params(self, logged_id, project_id, task_id, title=None, description=None,
                   price=None, compledted=None, paid=None, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.task_id = task_id
        self.title = title
        self.description = description
        self.price = price
        self.completed = compledted
        self.paid = paid
        return self

    def execute(self):
        self.validate_user_project.validate_permission(self.user_id)
        work_task = self.work_task_repo.get(self.task_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_permission(project.user_id, self.user_id)
        self.validate_user_project.validate_permission(project.id, work_task.project_id)
        title = self.title if self.title is not None else work_task.title
        description = self.description if self.description is not None else work_task.description
        price = self.price if self.price is not None else work_task.price
        completed = self.completed if self.completed is not None else work_task.completed
        paid = self.paid if self.paid is not None else work_task.paid
        update_work_task = WorkTask(
            id=work_task.id,
            title=title,
            description=description,
            price=price,
            completed=completed,
            paid=paid
        )

        return self.work_task_repo.update(update_work_task)


class DeleteTaskInteractor(Interactor):
    def __init__(self, work_task_repo, project_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project
        self.project_repo = project_repo

    def set_params(self, logged_id, project_id, task_id, *args, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.task_id = task_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(self.user_id)
        work_task = self.work_task_repo.get(self.task_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_permission(self.project_id, work_task.project_id)
        self.validate_user_project.validate_permission(self.user_id, project.user_id)
        return self.work_task_repo.delete(work_task.id)


class GetAllTasksInteractor(Interactor):
    def __init__(self, work_task_repo, project_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project
        self.project_repo = project_repo

    def set_params(self, logged_id, project_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.validate_user_project.validate_permission(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_task_payment(project.type_of_payment)
        return self.work_task_repo.get_all(self.project_id)


# ----------------------- Hour Payment ----------------------------------- #

class GetHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, validate_user_project):
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project

    def set_params(self, hour_payment_id, project_id, logged_id, **kwargs):
        self.hour_payment_id = hour_payment_id
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(logged_id=self.user_id)
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        self.validate_user_project.validate_permission(hour_payment.project_id, self.project_id)
        return hour_payment


class CreateHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, project_repo, validate_user_project):
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project
        self.project_repo = project_repo

    def execute(self, project_id, rate, logged_id, *args, **kwargs):
        self.project_id = project_id
        self.rate = rate
        self.user_id = logged_id
        return self

    def set_params(self, *args, **kwargs):
        self.validate_user_project.validate_permission(logged_id=self.user_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_permission(self.user_id, project.user_id)
        hour_payment = HourPayment(
            project_id=project.id,
            rate=self.rate
        )
        return self.hour_payment_repo.create(hour_payment)


class UpdateHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, project_repo, validate_user_project):
        self.hour_payment_repo = hour_payment_repo
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, hour_payment_id, rate, project_id, logged_id, **kwargs):
        self.hour_payment_id = hour_payment_id
        self.rate = rate
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self._validate(self.user_id)
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        self.validate_user_project.validate_permission(self.project_id, hour_payment.project_id)
        rate = self.rate if self.rate is not None else hour_payment.rate
        update_hour_payment = HourPayment(
            id=hour_payment.id,
            rate=rate,
            project_id=hour_payment.project_id
        )
        return self.hour_payment_repo.update(update_hour_payment)

    def _validate(self, logged_id):
        self.validate_user_project.validate_permission(logged_id=logged_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_permission(project.user_id, self.user_id)


class DeleteHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, project_repo, validate_user_project):
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project
        self.project_repo = project_repo

    def set_params(self, hour_payment_id, project_id, logged_id, *args, **kwargs):
        self.hour_payment_id = hour_payment_id,
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self._validate(logged_id=self.user_id)
        return self.hour_payment_repo.delete(self.hour_payment_id)

    def _validate(self, logged_id):
        self.validate_user_project.validate_permission(logged_id=logged_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_permission(project.user_id, self.user_id)


class GetAllHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, project_repo, validate_user_project):
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project
        self.project_repo = project_repo

    def set_params(self, project_id, logged_id, *args, **kwargs):
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self._validate(self.user_id)
        hour_payments = self.hour_payment_repo.get_all(self.project_id)
        return hour_payments

    def _validate(self, logged_id):
        self.validate_user_project.validate_permission(logged_id=logged_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_permission(project.user_id, logged_id)


# ---------------------------- Work Time ---------------------------------------- #

class GetWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, hour_payment_repo, validate_user_project):
        self.work_time_repo = work_time_repo
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project

    def set_params(self, work_time_id, hour_payment_id, logged_id=None, *args, **kwargs):
        self.work_time_id = work_time_id
        self.user_id = logged_id
        self.hour_payment_id = hour_payment_id
        return self

    def execute(self, *args, **kwargs):
        work_time = self.work_time_repo.get(self.work_time_id)
        self.validate_user_project.validate_permission(logged_id=self.user_id)
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        self.validate_user_project.validate_permission(hour_payment.id, work_time.hour_payment_id)
        return work_time


class CreateWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, hour_payment_repo, validate_user_project):
        self.work_time_repo = work_time_repo
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, hour_payment_id, start_work, end_work, paid, *args, **kwargs):
        self.user_id = logged_id
        self.hour_payment_id = hour_payment_id
        self.start_work = start_work
        self.end_work = end_work
        self.paid = paid
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(logged_id=self.user_id)
        work_time = WorkTime(
            hour_payment_id=self.hour_payment_id,
            start_work=self.start_work,
            end_work=self.end_work,
            paid=self.paid
        )
        return self.work_time_repo.create(work_time)


class UpdateWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, validate_user_project):
        self.work_time_repo = work_time_repo
        self.validate_user_project = validate_user_project

    def set_params(self, work_time_id, logged_id, hour_payment_id, paid, start_work, end_work, *args, **kwargs):
        self.work_time_id = work_time_id
        self.user_id = logged_id
        self.hour_payment_id = hour_payment_id
        self.paid = paid
        self.start_work = start_work
        self.end_work = end_work
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(logged_id=self.user_id)
        work_time = self.work_time_repo.get(self.work_time_id)
        self.validate_user_project.validate_permission(work_time.hour_payment_id, self.hour_payment_id)

        start_work = self.start_work if self.start_work is not None else work_time.start_work
        end_work = self.end_work if self.end_work is not None else work_time.end_work
        paid = self.paid if self.paid is not None else work_time.paid

        work_time_update = WorkTime(
            id=work_time.id,
            start_work=start_work,
            end_work=end_work,
            paid=paid
        )
        return self.work_time_repo.update(work_time_update)


class DeleteWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, hour_payment_repo, validate_user_project):
        self.work_time_repo = work_time_repo
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project

    def set_params(self, work_time_id, hour_payment_id, logged_id, *args, **kwargs):
        self.work_time_id = work_time_id
        self.hour_payment_id = hour_payment_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(logged_id=self.user_id)
        work_time = self.work_time_repo.get(self.work_time_id)
        self.validate_user_project.validate_permission(self.hour_payment_id, work_time.hour_payment_id)

        return self.work_time_repo.delete(work_time.id)


class GetAllWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, hour_payment_repo, validate_user_project):
        self.work_time_repo = work_time_repo
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project

    def set_params(self, hour_payment_id, logged_id=None, *args, **kwargs):
        self.user_id = logged_id
        self.hour_payment_id = hour_payment_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(logged_id=self.user_id)
        work_times = self.work_time_repo.get_all(self.hour_payment_id)
        return work_times


# --------------------------- Month Payment ---------------------------------------- #

class GetMonthPaymentInteractor(Interactor):
    def __init__(self, month_payment_repo, user_permission_validator):
        self.month_payment_repo = month_payment_repo
        self.user_permission_validator = user_permission_validator

    def set_params(self, month_payment_id, project_id, logged_id, *args, **kwargs):
        self.month_payment_id = month_payment_id
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self):
        self.user_permission_validator.validate_permission(self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        self.user_permission_validator.validate_permission(self.project_id, month_payment.project_id)
        return month_payment


class CreateMonthPaymentInteractor(Interactor):
    def __init__(self, month_payment_repo, project_repo, user_permission_validator):
        self.month_payment_repo = month_payment_repo
        self.user_permission_validator = user_permission_validator
        self.project_repo = project_repo

    def set_params(self, project_id, rate, logged_id, *args, **kwargs):
        self.project_id = project_id
        self.rate = rate
        self.user_id = logged_id
        return self

    def execute(self):
        self.user_permission_validator.validate_permission(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.user_permission_validator.validate_permission(self.user_id, project.user_id)
        month_payment = MonthPayment(
            project_id=project.id,
            rate=self.rate
        )
        return self.month_payment_repo.create(month_payment)


class UpdateMonthPaymentInteractor(Interactor):
    def __init__(self, month_payment_repo, user_permission_validator):
        self.month_payment_repo = month_payment_repo
        self.user_permission_validator = user_permission_validator

    def set_params(self, month_payment_id, project_id, rate, logged_id, *args, **kwargs):
        self.month_payment_id = month_payment_id
        self.project_id = project_id
        self.rate = rate
        self.user_id = logged_id
        return self

    def execute(self):
        self.user_permission_validator.validate_permission(self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        self.user_permission_validator.validate_permission(month_payment.project_id, self.project_id)

        month_payment.__setattr__('_rate', self.rate if self.rate is not None else month_payment.rate)

        return self.month_payment_repo.update(month_payment)


class DeleteMonthPaymentInteractor(Interactor):
    def __init__(self, month_payment_repo, user_permission_validator):
        self.month_payment_repo = month_payment_repo
        self.user_permission_validator = user_permission_validator

    def set_params(self, month_payment_id, logged_id, project_id, *args, **kwargs):
        self.month_payment_id = month_payment_id
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.user_permission_validator.validate_permission(self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        self.user_permission_validator.validate_permission(self.project_id, month_payment.project_id)
        return self.month_payment_repo.delete(month_payment.id)


class GetAllMonthPaymentsInteractor(Interactor):
    def __init__(self, month_payment_repo, user_permission_validator):
        self.month_payment_repo = month_payment_repo
        self.user_permission_validator = user_permission_validator

    def set_params(self, project_id, logged_id, *args, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.user_permission_validator.validate_permission(self.user_id)
        return self.month_payment_repo.get_all(self.project_id)


# ----------------------- Worked Day ----------------------------------- #

class GetWorkedDayInteractor(Interactor):
    def __init__(self, work_day_repo, hour_payment_repo, validate_user_project):
        self.work_day_repo = work_day_repo
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project

    def set_params(self, worked_day_id, hour_payment_id, logged_id, **kwargs):
        self.worked_day_id = worked_day_id
        self.user_id = logged_id
        self.hour_payment_id = hour_payment_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(logged_id=self.user_id)
        worked_day = self.hour_payment_repo.get(self.worked_day_id)
        self.validate_user_project.validate_permission(worked_day.hour_paymnet_id, self.hour_payment_id)
        return worked_day


class CreateWorkedDayInteractor(Interactor):
    def __init__(self, work_day_repo, month_payment_repo, validate_user_project):
        self.work_day_repo = work_day_repo
        self.month_payment_repo = month_payment_repo
        self.validate_user_project = validate_user_project

    def set_params(self, month_payment_id, day, paid, logged_id,*args, **kwargs):
        self.month_paymnet_id = month_payment_id
        self.day = day
        self.paid = paid
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(self.user_id)
        month_paymnet = self.month_payment_repo.get(self.month_paymnet_id)
        worked_day = WorkedDay(
            month_payment_id=month_paymnet.id,
            day=self.day,
            paid=self.paid
        )
        return self.work_day_repo.create(worked_day)


class DeleteWorkedDayInteractor(Interactor):
    def __init__(self, work_day_repo, validate_user_project):
        self.work_day_repo = work_day_repo
        self.validate_user_project = validate_user_project

    def set_params(self, worked_day_id, logged_id, *args, **kwargs):
        self.worked_day_id = worked_day_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(self.user_id)
        return self.work_day_repo.delete(self.worked_day_id)


class GetAllWorkedDayInteractor(Interactor):
    def __init__(self, work_day_repo, month_payment_repo, validate_user_project):
        self.work_day_repo = work_day_repo
        self.validate_user_project = validate_user_project
        self.month_payment_repo = month_payment_repo

    def set_params(self, month_payment_id, logged_id, *args, **kwargs):
        self.month_payment_id = month_payment_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_permission(self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        return self.work_day_repo.get_all(month_payment.id)
