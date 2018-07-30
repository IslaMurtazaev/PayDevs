from PayDevs.interactors import Interactor
from project.entities import Project, WorkTask, HourPayment, WorkTime, MonthPayment, WorkedDay


# ------------------------ Project ---------------------------------------- #

class GetProjectInteractor(Interactor):
    def __init__(self, project_repo, permission_validator):
        self.project_repo = project_repo
        self.permission_validator = permission_validator

    def set_params(self, project_id, logged_id=None, **kwargs):
        self.logged_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.permission_validator.validate(self.logged_id)
        return self.project_repo.get(logged_id=self.logged_id, project_id=self.project_id)


class CreateProjectInteractor(Interactor):
    def __init__(self, project_repo, permission_validator, type_of_payment_validator, datetime_validator):
        self.project_repo = project_repo
        self.permission_validator = permission_validator
        self.type_of_payment_validator = type_of_payment_validator
        self.datetime_validator = datetime_validator

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
        self.permission_validator.validate(self.logged_id)
        self.type_of_payment_validator.validate(self.type_of_payment)
        start_date = self.datetime_validator.validate_datetime_format(self.start_date)
        end_date = self.datetime_validator.validate_datetime_format(self.end_date)

        project = Project(user_id=self.logged_id,
                          title=self.title,
                          description=self.description,
                          start_date=start_date,
                          end_date=end_date,
                          status=self.status,
                          type_of_payment=self.type_of_payment)
        return self.project_repo.create(project)


class UpdateProjectInteractor(Interactor):
    def __init__(self, project_repo, permission_validator, type_of_payment_validator, datetime_validator):
        self.project_repo = project_repo
        self.permission_validator = permission_validator
        self.type_of_payment_validator = type_of_payment_validator
        self.datetime_validator = datetime_validator

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
        self.permission_validator.validate(self.user_id, project.user_id)
        title = self.title if self.title is not None else project.title
        description = self.description if self.description is not None else project.description
        start_date = self.start_date if self.start_date is not None else project.start_date
        end_date = self.end_date if self.end_date is not None else project.end_date
        type_of_payment = self.type_of_payment if self.type_of_payment is not None else project.type_of_payment
        status = self.status if self.status else project.status
        self.type_of_payment_validator.validate(type_of_payment)
        if self.start_date is not None:
            start_date = self.datetime_validator.validate_datetime_format(start_date)
        if self.end_date:
            end_date = self.datetime_validator.validate_datetime_format(end_date)

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
    def __init__(self, project_repo, permission_validator):
        self.project_repo = project_repo
        self.permission_validator = permission_validator

    def set_params(self, logged_id, project_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self, *args, **kwargs):
        project = self.project_repo.get(project_id=self.project_id)
        self.permission_validator.validate(self.user_id, project.user_id)
        return self.project_repo.delete(project.id)


class GetAllProjectsInteractor(Interactor):
    def __init__(self, project_repo, permission_validator):
        self.project_repo = project_repo
        self.permission_validator = permission_validator

    def set_params(self, logged_id, **kwargs):
        self.user_id = logged_id
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        return self.project_repo.get_all(self.user_id)


class ProjectGetTotalInteractor(Interactor):
    def __init__(self, project_repo, user_repo, permission_validator, datetime_validator):
        self.project_repo = project_repo
        self.user_repo = user_repo
        self.permission_validator = permission_validator
        self.datetime_validator = datetime_validator

    def set_params(self, logged_id, project_id, end_date=None, paid=False, last_month=None, pay=True, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.last_month = last_month
        self.paid = paid
        self.end_date = end_date
        self.pay = pay
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(self.user_id, project.user_id)
        end_date = self.end_date if self.end_date is not None else self.datetime_validator.now_end_date_project(
            project.type_of_payment
        )
        # end_work = self.datetime_validator.validate_datetime_format(self.end_work)
        project = Project(
            id=project.id,
            title=project.title,
            description=project.description,
            start_date=project.start_date,
            end_date=end_date,
            status=project.status,
            type_of_payment=project.type_of_payment,
            user_id=project.user_id
        )
        self.project_repo.update(project)
        project_total = self.project_repo.get_total_project(self.project_id, paid=self.paid, pay=self.pay)
        if project_total.type_of_payment == 'T_P':
            project_total.count_task = len(project_total._entity_type_list)
        user = self.user_repo.get_user_by_id(self.user_id)
        project_total.user = user.username
        return project_total


# --------------------------- Work Task ----------------------------------------#



class GetTaskInteractor(Interactor):
    def __init__(self, work_task_repo, permission_validator):
        self.work_task_repo = work_task_repo
        self.permission_validator = permission_validator

    def set_params(self, logged_id, project_id, task_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.task_id = task_id
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        work_task = self.work_task_repo.get(self.task_id)
        self.permission_validator.validate(self.project_id, work_task.project_id)
        return work_task


class CreateTaskInteractor(Interactor):
    def __init__(self, work_task_repo, project_repo, permission_validator, type_of_payment_validator):
        self.work_task_repo = work_task_repo
        self.permission_validator = permission_validator
        self.project_repo = project_repo
        self.type_of_payment_validator = type_of_payment_validator

    def set_params(self, logged_id, project_id, title, description, price=0, paid=False, completed=False, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.price = price
        self.paid = paid
        self.completed = completed
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(self.user_id, project.user_id)
        self.type_of_payment_validator.validate_task_payment(project.type_of_payment)
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
    def __init__(self, work_task_repo, project_repo, permission_validator):
        self.work_task_repo = work_task_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator

    def set_params(self, logged_id, project_id, task_id, title=None, description=None,
                   price=None, completed=None, paid=None, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.task_id = task_id
        self.title = title
        self.description = description
        self.price = price
        self.completed = completed
        self.paid = paid
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        work_task = self.work_task_repo.get(self.task_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(project.user_id, self.user_id)
        self.permission_validator.validate(project.id, work_task.project_id)
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
    def __init__(self, work_task_repo, project_repo, permisssion_validator):
        self.work_task_repo = work_task_repo
        self.permission_validator = permisssion_validator
        self.project_repo = project_repo

    def set_params(self, logged_id, project_id, task_id, *args, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.task_id = task_id
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(self.user_id)
        work_task = self.work_task_repo.get(self.task_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(self.project_id, work_task.project_id)
        self.permission_validator.validate(self.user_id, project.user_id)
        return self.work_task_repo.delete(work_task.id)


class GetAllTasksInteractor(Interactor):
    def __init__(self, work_task_repo, project_repo, permission_validator, type_of_payment_validator):
        self.work_task_repo = work_task_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator
        self.type_of_payment_validator = type_of_payment_validator

    def set_params(self, logged_id, project_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.type_of_payment_validator.validate_task_payment(project.type_of_payment)
        return self.work_task_repo.get_all(self.project_id)


# ----------------------- Hour Payment ----------------------------------- #

class GetHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, permission_validator):
        self.hour_payment_repo = hour_payment_repo
        self.permission_validator = permission_validator

    def set_params(self, hour_payment_id, project_id, logged_id, **kwargs):
        self.hour_payment_id = hour_payment_id
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(logged_id=self.user_id)
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        self.permission_validator.validate(hour_payment.project_id, self.project_id)
        return hour_payment


class CreateHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, project_repo, permission_validator, type_of_payment_validator, rate_validator):
        self.hour_payment_repo = hour_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator
        self.type_of_payment_validator = type_of_payment_validator
        self.rate_validator = rate_validator

    def set_params(self, project_id, logged_id, rate=None, *args, **kwargs):
        self.project_id = project_id
        self.rate = rate
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(logged_id=self.user_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(self.user_id, project.user_id)
        self.type_of_payment_validator.validate_hour_payment(project.type_of_payment)
        self.rate_validator.validate(self.rate)

        hour_payment = HourPayment(
            project_id=project.id,
            rate=self.rate
        )
        return self.hour_payment_repo.create(hour_payment)


class UpdateHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, project_repo, permission_validator, rate_validator):
        self.hour_payment_repo = hour_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator
        self.rate_validator = rate_validator

    def set_params(self, hour_payment_id, rate, project_id, logged_id, **kwargs):
        self.hour_payment_id = hour_payment_id
        self.rate = rate
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self._validate(self.user_id)
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        self.permission_validator.validate(self.project_id, hour_payment.project_id)
        rate = self.rate if self.rate is not None else hour_payment.rate
        update_hour_payment = HourPayment(
            id=hour_payment.id,
            rate=rate,
            project_id=hour_payment.project_id
        )
        return self.hour_payment_repo.update(update_hour_payment)

    def _validate(self, logged_id):
        self.permission_validator.validate(logged_id=logged_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(project.user_id, self.user_id)
        self.rate_validator.validate(self.rate)


class DeleteHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, project_repo, permission_validator):
        self.hour_payment_repo = hour_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator

    def set_params(self, hour_payment_id, project_id, logged_id, *args, **kwargs):
        self.hour_payment_id = hour_payment_id
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self._validate(logged_id=self.user_id)
        return self.hour_payment_repo.delete(self.hour_payment_id)

    def _validate(self, logged_id):
        self.permission_validator.validate(logged_id=logged_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(project.user_id, self.user_id)


class GetAllHourPaymentInteractor(Interactor):
    def __init__(self, hour_payment_repo, project_repo, permission_validator):
        self.hour_payment_repo = hour_payment_repo
        self.permission_validator = permission_validator
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
        self.permission_validator.validate(logged_id=logged_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(project.user_id, logged_id)


# ---------------------------- Work Time ---------------------------------------- #

class GetWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, hour_payment_repo, permission_validator):
        self.work_time_repo = work_time_repo
        self.hour_payment_repo = hour_payment_repo
        self.permission_validator = permission_validator

    def set_params(self, work_time_id, hour_payment_id, project_id, logged_id=None, *args, **kwargs):
        self.work_time_id = work_time_id
        self.user_id = logged_id
        self.hour_payment_id = hour_payment_id
        self.project_id = project_id
        return self

    def execute(self, *args, **kwargs):
        work_time = self.work_time_repo.get(self.work_time_id)
        self.permission_validator.validate(logged_id=self.user_id)
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        self.permission_validator.validate(hour_payment.id, work_time.hour_payment_id)
        self.permission_validator.validate(hour_payment.project_id, self.project_id)
        return work_time


class CreateWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, hour_payment_repo, permission_validator, datetime_validator):
        self.work_time_repo = work_time_repo
        self.hour_payment_repo = hour_payment_repo
        self.permission_validator = permission_validator
        self.datetime_validator = datetime_validator

    def set_params(self, logged_id, project_id, hour_payment_id, start_work=None, end_work=None,
                   paid=False, *args, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.hour_payment_id = hour_payment_id
        self.start_work = start_work
        self.end_work = end_work
        self.paid = paid
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(logged_id=self.user_id)
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        self.permission_validator.validate(hour_payment.project_id, self.project_id)
        start_work = self.datetime_validator.validate_datetime_format(self.start_work)
        end_work = self.datetime_validator.validate_datetime_format(self.end_work)

        work_time = WorkTime(
            hour_payment_id=self.hour_payment_id,
            start_work=start_work,
            end_work=end_work,
            paid=self.paid
        )
        return self.work_time_repo.create(work_time)


class UpdateWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, project_repo, hour_payment_repo, permission_validator, datetime_validator):
        self.work_time_repo = work_time_repo
        self.permission_validator = permission_validator
        self.hour_payment_repo = hour_payment_repo
        self.datetime_validator = datetime_validator
        self.project_repo = project_repo

    def set_params(self, work_time_id, project_id, logged_id, hour_payment_id, paid=None,
                   start_work=None, end_work=None, **kwargs):
        self.work_time_id = work_time_id
        self.user_id = logged_id
        self.hour_payment_id = hour_payment_id
        self.paid = paid
        self.start_work = start_work
        self.end_work = end_work
        self.project_id = project_id
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(logged_id=self.user_id)
        work_time = self.work_time_repo.get(self.work_time_id)
        self._validate(work_time)
        start_work = self.start_work if self.start_work is not None else work_time.start_work
        end_work = self.end_work if self.end_work is not None else work_time.end_work
        paid = self.paid if self.paid is not None else work_time.paid
        if self.start_work is not None:
            start_work = self.datetime_validator.validate_datetime_format(start_work)
        if self.end_work is not None:
            end_work = self.datetime_validator.validate_datetime_format(end_work)

        work_time_update = WorkTime(
            id=work_time.id,
            start_work=start_work,
            end_work=end_work,
            paid=paid
        )
        return self.work_time_repo.update(work_time_update)


    def _validate(self, work_time):
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        project = self.project_repo.get(hour_payment.project_id)
        self.permission_validator.validate(work_time.hour_payment_id, self.hour_payment_id)
        self.permission_validator.validate(project.id, self.project_id)
        self.permission_validator.validate(project.user_id, self.user_id)


class DeleteWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, hour_payment_repo, project_repo, permission_validator):
        self.work_time_repo = work_time_repo
        self.hour_payment_repo = hour_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator

    def set_params(self, work_time_id, hour_payment_id, logged_id, *args, **kwargs):
        self.work_time_id = work_time_id
        self.hour_payment_id = hour_payment_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(logged_id=self.user_id)
        work_time = self.work_time_repo.get(self.work_time_id)
        self._validate(work_time)
        return self.work_time_repo.delete(work_time.id)

    def _validate(self, work_time):
        hour_payment = self.hour_payment_repo.get(work_time.hour_payment_id)
        project = self.project_repo.get(hour_payment.project_id)
        self.permission_validator.validate(self.hour_payment_id, hour_payment.id)
        self.permission_validator.validate(project.user_id, self.user_id)


class GetAllWorkTimeInteractor(Interactor):
    def __init__(self, work_time_repo, hour_payment_repo, permission_validator):
        self.work_time_repo = work_time_repo
        self.hour_payment_repo = hour_payment_repo
        self.permission_validator = permission_validator

    def set_params(self, hour_payment_id, logged_id=None, *args, **kwargs):
        self.user_id = logged_id
        self.hour_payment_id = hour_payment_id
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(logged_id=self.user_id)
        work_times = self.work_time_repo.get_all(self.hour_payment_id)
        return work_times


# --------------------------- Month Payment ---------------------------------------- #

class CreateMonthPaymentInteractor(Interactor):
    def __init__(self, month_payment_repo, project_repo, permission_validator, rate_validator):
        self.month_payment_repo = month_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator
        self.rate_validator = rate_validator

    def set_params(self, project_id, logged_id, rate=0, *args, **kwargs):
        self.project_id = project_id
        self.rate = rate
        self.user_id = logged_id
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(self.user_id, project.user_id)
        self.rate_validator.validate(self.rate)
        month_payment = MonthPayment(
            project_id=project.id,
            rate=self.rate
        )
        return self.month_payment_repo.create(month_payment)


class GetMonthPaymentInteractor(Interactor):
    def __init__(self, month_payment_repo, permission_validator):
        self.month_payment_repo = month_payment_repo
        self.permission_validator = permission_validator

    def set_params(self, month_payment_id, logged_id, *args, **kwargs):
        self.month_payment_id = month_payment_id
        self.user_id = logged_id
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        return month_payment


class UpdateMonthPaymentInteractor(Interactor):
    def __init__(self, month_payment_repo, project_repo, permission_validator, rate_validator):
        self.month_payment_repo = month_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator
        self.rate_validator = rate_validator

    def set_params(self, month_payment_id, project_id, rate, logged_id, *args, **kwargs):
        self.month_payment_id = month_payment_id
        self.project_id = project_id
        self.rate = rate
        self.user_id = logged_id
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(project.user_id, self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        self.permission_validator.validate(month_payment.project_id, self.project_id)
        self.rate_validator.validate(self.rate)

        month_payment.__setattr__('_rate', self.rate if self.rate is not None else month_payment.rate)

        return self.month_payment_repo.update(month_payment)


class DeleteMonthPaymentInteractor(Interactor):
    def __init__(self, month_payment_repo, project_repo, permission_validator):
        self.month_payment_repo = month_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator

    def set_params(self, month_payment_id, project_id, logged_id, *args, **kwargs):
        self.month_payment_id = month_payment_id
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(project.user_id, self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        self.permission_validator.validate(self.project_id, month_payment.project_id)
        return self.month_payment_repo.delete(month_payment.id)


class GetAllMonthPaymentsInteractor(Interactor):
    def __init__(self, month_payment_repo, permission_validator):
        self.month_payment_repo = month_payment_repo
        self.permission_validator = permission_validator

    def set_params(self, project_id, logged_id, *args, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        return self.month_payment_repo.get_all(self.project_id)


# ----------------------- Worked Day ----------------------------------- #

class CreateWorkedDayInteractor(Interactor):
    def __init__(self, worked_day_repo, month_payment_repo, project_repo, permission_validator, date_validator):
        self.worked_day_repo = worked_day_repo
        self.month_payment_repo = month_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator
        self.date_validator = date_validator

    def set_params(self, month_payment_id, project_id, day, paid, logged_id, *args, **kwargs):
        self.month_payment_id = month_payment_id
        self.project_id = project_id
        self.day = day
        self.paid = paid
        self.user_id = logged_id
        return self

    def execute(self):
        self.permission_validator.validate(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(project.user_id, self.user_id)
        self.date_validator.validate_date_format(self.day)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        self.permission_validator.validate(month_payment.project_id, self.project_id)

        worked_day = WorkedDay(
            month_payment_id=month_payment.id,
            day=self.day,
            paid=self.paid
        )
        return self.worked_day_repo.create(worked_day)


class GetWorkedDayInteractor(Interactor):
    def __init__(self, worked_day_repo, permission_validator):
        self.worked_day_repo = worked_day_repo
        self.permission_validator = permission_validator

    def set_params(self, worked_day_id, logged_id, **kwargs):
        self.worked_day_id = worked_day_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(logged_id=self.user_id)
        worked_day = self.worked_day_repo.get(self.worked_day_id)
        return worked_day


class UpdateWorkedDayInteractor(Interactor):
    def __init__(self, worked_day_repo, month_payment_repo, project_repo, permission_validator, date_validator):
        self.worked_day_repo = worked_day_repo
        self.month_payment_repo = month_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator
        self.date_validator = date_validator

    def set_params(self, worked_day_id, month_payment_id, project_id, logged_id, day=None, paid=None, *args, **kwargs):
        self.worked_day_id = worked_day_id
        self.month_payment_id = month_payment_id
        self.project_id = project_id
        self.user_id = logged_id
        self.day = day
        self.paid = paid
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(project.user_id, self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        self.permission_validator.validate(month_payment.project_id, self.project_id)
        worked_day = self.worked_day_repo.get(self.worked_day_id)
        self.permission_validator.validate(worked_day.month_payment_id, self.month_payment_id)

        if self.day is not None:
            self.day = self.date_validator.validate_date_format(self.day)

        modified_worked_day = WorkedDay(
            id=worked_day.id,
            day=self.day if self.day is not None else worked_day.day,
            paid=self.paid if self.paid is not None else worked_day.paid,
            month_payment_id=worked_day.month_payment_id
        )

        return self.worked_day_repo.update(modified_worked_day)


class DeleteWorkedDayInteractor(Interactor):
    def __init__(self, worked_day_repo, month_payment_repo, project_repo, permission_validator):
        self.worked_day_repo = worked_day_repo
        self.month_payment_repo = month_payment_repo
        self.project_repo = project_repo
        self.permission_validator = permission_validator

    def set_params(self, worked_day_id, month_payment_id, project_id, logged_id, *args, **kwargs):
        self.worked_day_id = worked_day_id
        self.month_payment_id = month_payment_id
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(self.user_id)
        project = self.project_repo.get(self.project_id)
        self.permission_validator.validate(project.user_id, self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        self.permission_validator.validate(month_payment.project_id, self.project_id)
        worked_day = self.worked_day_repo.get(self.worked_day_id)
        self.permission_validator.validate(worked_day.month_payment_id, self.month_payment_id)

        return self.worked_day_repo.delete(self.worked_day_id)


class GetAllWorkedDaysInteractor(Interactor):
    def __init__(self, worked_day_repo, month_payment_repo, permission_validator):
        self.worked_day_repo = worked_day_repo
        self.month_payment_repo = month_payment_repo
        self.permission_validator = permission_validator

    def set_params(self, month_payment_id, logged_id, *args, **kwargs):
        self.month_payment_id = month_payment_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.permission_validator.validate(self.user_id)
        month_payment = self.month_payment_repo.get(self.month_payment_id)
        return self.worked_day_repo.get_all(month_payment.id)
