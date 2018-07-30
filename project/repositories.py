from project.entities import Project, WorkTask, MonthPayment, WorkedDay, HourPayment, WorkTime
from project.models import ProjectORM, HourPaymentORM, MonthPaymentORM, WorkTaskORM, WorkedDayORM, WorkTimeORM
from PayDevs.exceptions import EntityDoesNotExistException, InvalidEntityException



class ProjectRepo(object):
    def __init__(self):
        self.mont_payment = MonthPaymentRepo()
        self.hour_payment = HourPaymentRepo()
        self.task_repo = WorkTaskRepo()

    def _decode_db_project(self, db_project, is_mine=False):
        fileds = {
            'id': db_project.id,
            'user_id': db_project.user.id,
            'title': db_project.title,
            'description': db_project.description,
            'start_date': db_project.start_date,
            'end_date': db_project.end_date,
            'type_of_payment': db_project.type_of_payment,
            'status': db_project.status,
            'is_mine': is_mine
        }

        return Project(**fileds)

    def get(self, project_id, logged_id=None):
        try:
            db_project = ProjectORM.objects.select_related('user').get(id=project_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_project(db_project, is_mine=(logged_id == db_project.user.id))

    def get_total_project(self, project_id, paid=None, last_month_days=None, boundary=None, pay=False):
        try:
            db_project = ProjectORM.objects.select_related('user').get(id=project_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        project = self._decode_db_project(db_project)
        project._entity_type_list = self._get_entity_type_list(db_project.id, paid=paid,
                                                               last_month_days=last_month_days,
                                                               boundary=boundary, pay=pay)
        return project

    def create(self, project):
        db_project = ProjectORM.objects.create(
            title=project.title,
            description=project.description,
            user_id=project.user_id,
            start_date=project.start_date,
            end_date=project.end_date,
            status=project.status,
            type_of_payment=project.type_of_payment,
        )

        return self._decode_db_project(db_project=db_project, is_mine=True)

    def delete(self, project_id):
        try:
            db_project = ProjectORM.objects.get(id=project_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        project = self._decode_db_project(db_project)
        db_project.delete()
        return project

    def get_all(self, user_id):
        db_projects = ProjectORM.objects.filter(user_id=user_id)
        projects = [self._decode_db_project(db_project, is_mine=True)
                    for db_project in db_projects]
        return projects

    def update(self, project):

        db_project_filter = ProjectORM.objects.filter(id=project.id)
        db_project_filter .update(
                title=project.title,
                description=project.description,
                status=project.status,
                type_of_payment=project.type_of_payment,
                start_date=project.start_date,
                end_date=project.end_date,
        )
        db_project = db_project_filter .get(id=project.id)
        return self._decode_db_project(db_project)

    def update_payment_attrs(self, project_id, last_month_days=None, boundary=None, pay=False):
        try:
            db_project = ProjectORM.objects.select_related('user').get(id=project_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        if db_project.type_of_payment == 'H_P':
            pass
        elif db_project.type_of_payment == 'M_P':
            pass
        elif db_project.type_of_payment == 'T_P':
            self.task_repo.update_taks(project_id, pay=pay)

    def _get_entity_type_list(self, project_id, paid=False, last_month_days=None, boundary=None, pay=False):
        entity_type_list = []
        try:
            db_project = ProjectORM.objects.select_related('user').get(id=project_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        if db_project.type_of_payment == 'H_P':
            entity_type_list = self.hour_payment.get_total_hour_payments(project_id=project_id, work_time_paid=paid,
                                                                         work_time_boundary=boundary, pay=pay)
        elif db_project.type_of_payment == 'M_P':
            entity_type_list = self.mont_payment.get_month_payments_by_project_id(project_id=project_id,
                                                                                  paid=paid,
                                                                                  last_month_days=last_month_days,
                                                                                  pay=pay)
        elif db_project.type_of_payment == 'T_P':
            entity_type_list = self.task_repo.get_work_tasks(project_id=db_project.id, paid=paid, pay=pay)

        return entity_type_list





class WorkTaskRepo:
    def get(self, work_task_id):
        try:
            db_work_task = WorkTaskORM.objects.get(id=work_task_id)
        except WorkTaskORM.DoesNotExist:
            raise EntityDoesNotExistException
        return self._decode_db_work_task(db_work_task)

    def get_work_tasks(self, project_id, paid=False, pay=False):
        work_tasks = []
        db_work_tasks = WorkTaskORM.objects.filter(project_id=project_id, paid=paid, completed=True)
        for db_work_task in db_work_tasks:
            work_tasks.append(self._decode_db_work_task(db_work_task))
        return work_tasks

    def update_taks(self, project_id, **kwargs):
        WorkTaskORM.objects.filter(project_id=project_id, completed=True).update(**kwargs)


    def get_all(self, project_id):
        tasks = []
        db_work_tasks = WorkTaskORM.objects.filter(project_id=project_id)
        for db_work_task in db_work_tasks:
            tasks.append(self._decode_db_work_task(db_work_task))
        return tasks

    def create(self, work_task):

        db_work_task = WorkTaskORM.objects.create(
            project_id=work_task.project_id,
            title=work_task.title,
            description=work_task.description,
            price=work_task.price,
            completed=work_task.completed,
            paid=work_task.paid
        )
        return self._decode_db_work_task(db_work_task)

    def update(self, work_task):

        db_work_task_filter = WorkTaskORM.objects.filter(id=work_task.id)

        db_work_task_filter.update(
            title=work_task.title,
            description=work_task.description,
            completed=work_task.completed,
            paid=work_task.paid,
            price=work_task.price,
        )
        db_work_task = db_work_task_filter.get(id=work_task.id)
        return self._decode_db_work_task(db_work_task)

    def delete(self, work_task_id):
        try:
            db_work_task = WorkTaskORM.objects.get(id=work_task_id)
        except WorkTaskORM.DoesNotExist:
            raise EntityDoesNotExistException
        work_task = self._decode_db_work_task(db_work_task)
        db_work_task.delete()
        return work_task

    def _decode_db_work_task(self, db_work_task):
        fields = {
            'id': db_work_task.id,
            'project_id': db_work_task.project.id,
            'title': db_work_task.title,
            'description': db_work_task.description,
            'price': db_work_task.price,
            'completed': db_work_task.completed,
            'paid': db_work_task.paid
        }

        return WorkTask(**fields)



class MonthPaymentRepo:
    def __init__(self):
        self.worked_day_repo = WorkedDayRepo()

    def _decode_db_month_payment(self, db_month_payment):

        fileds = {
            'id': db_month_payment.id,
            'project_id': db_month_payment.project.id,
            'rate': db_month_payment.rate,

        }

        return MonthPayment(**fileds)

    def get(self, month_payment_id):
        try:
            db_month_payment = MonthPaymentORM.objects.select_related('project').get(id=month_payment_id)
        except MonthPaymentORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_month_payment(db_month_payment)

    def _get_total_month_payment(self, db_month_payment, paid=None, last_month_days=None, pay=False):
        month_payment = self._decode_db_month_payment(db_month_payment)
        month_payment._work_days = self.worked_day_repo.get_workdays(db_month_payment.id, paid=paid,
                                                                     last_month_days=last_month_days,
                                                                     pay=pay)
        return month_payment

    def get_month_payments_by_project_id(self, project_id, paid=None, last_month_days=None, pay=False):
        db_month_payments = MonthPaymentORM.objects.select_related('project').filter(project_id=project_id)
        return [self._get_total_month_payment(db_month_payment, paid=paid, last_month_days=last_month_days, pay=pay)
                for db_month_payment in db_month_payments]

    def create(self, month_payment):
        db_month_payment = MonthPaymentORM.objects.create(
            project_id=month_payment.project_id,
            rate=month_payment.rate
        )

        return self._decode_db_month_payment(db_month_payment)

    def update(self, month_payment):
        db_month_payments = MonthPaymentORM.objects.filter(id=month_payment.id)
        db_month_payments.update(
            rate=month_payment.rate
        )
        db_month_payment = db_month_payments.get(id=month_payment.id)
        return self._decode_db_month_payment(db_month_payment)

    def delete(self, month_payment_id):
        try:
            db_month_payment = MonthPaymentORM.objects.get(id=month_payment_id)
        except MonthPaymentORM.DoesNotExist:
            raise EntityDoesNotExistException
        month_payment = self._decode_db_month_payment(db_month_payment)
        db_month_payment.delete()
        return month_payment

    def get_all(self, project_id):
        db_month_payments = MonthPaymentORM.objects.select_related('project').filter(project_id=project_id)
        return [self._decode_db_month_payment(db_month_payment)
                for db_month_payment in db_month_payments]

    def _get_worked_days(self, month_payment_id, paid=False, last_month_days=None, pay=False):
        worked_days = self.worked_day_repo.get_workdays(month_payment_id, paid=paid,
                                                        last_month_days=last_month_days, pay=pay)
        return worked_days


class WorkedDayRepo:
    def _decode_db_worked_day(self, db_worked_day):

        fileds = {
            'id': db_worked_day.id,
            'month_payment_id': db_worked_day.month_payment.id,
            'day': db_worked_day.day,
            'paid': db_worked_day.paid
        }
        return WorkedDay(**fileds)

    def create(self, worked_day):
        db_worked_day = WorkedDayORM.objects.create(
            month_payment_id=worked_day.month_payment_id,
            day=worked_day.day,
            paid=worked_day.paid
        )
        return self._decode_db_worked_day(db_worked_day)

    def update(self, worked_day):

        db_worked_days = WorkedDayORM.objects.filter(id=worked_day.id)
        db_worked_days.update(
            day=worked_day.day,
            paid=worked_day.paid
        )
        db_worked_day = db_worked_days.get(id=worked_day.id)
        return self._decode_db_worked_day(db_worked_day)

    def delete(self, worked_day_id):
        try:
            db_worked_day = WorkedDayORM.objects.get(id=worked_day_id)
        except WorkedDayORM.DoesNotExist:
            raise EntityDoesNotExistException
        worked_day = self._decode_db_worked_day(db_worked_day)
        db_worked_day.delete()
        return worked_day

    def get(self, worked_day_id):
        try:
            db_worked_day = WorkedDayORM.objects.get(id=worked_day_id)
        except WorkedDayORM.DoesNotExist:
            raise EntityDoesNotExistException
        return self._decode_db_worked_day(db_worked_day)

    def get_all(self, month_payment_id):
        db_worked_days = WorkedDayORM.objects.filter(month_payment_id=month_payment_id)
        return [self._decode_db_worked_day(db_worked_day) for db_worked_day in db_worked_days]

    def get_workdays(self, month_payment_id, paid=False, last_month_days=None, pay=False):
        worked_days = []
        if last_month_days is None:
            db_worked_days = WorkedDayORM.objects.filter(month_payment_id=month_payment_id, paid=paid)
        else:
            db_worked_days = WorkedDayORM.objects.filter(month_payment_id=month_payment_id,
                                                         paid=paid, day__lt=last_month_days)
        for db_worked_day in db_worked_days:
            worked_days.append(self._decode_db_worked_day(db_worked_day))
        return worked_days


    def update_attrs(self, month_payment_id, paid=False, last_month_days=None, **kwargs):
        if last_month_days is None:
            WorkedDayORM.objects.filter(month_payment_id=month_payment_id, paid=paid).update(**kwargs)
        else:
            WorkedDayORM.objects.filter(month_payment_id=month_payment_id,
                                        paid=paid, day__lt=last_month_days).update(**kwargs)

class HourPaymentRepo:
    def __init__(self):
        self.work_time_repo = WorkTimeRepo()

    def get(self, hour_payment_id):
        try:
            db_hour_payment = HourPaymentORM.objects.select_related('project').get(id=hour_payment_id)
        except HourPaymentORM.DoesNotExist:
            raise EntityDoesNotExistException
        return self._decode_db_hour_payment(db_hour_payment)

    def _get_total_hour_payment(self, db_hour_payment, work_time_paid=None, work_time_boundary=None, pay=False):
        hour_payment = self._decode_db_hour_payment(db_hour_payment)
        hour_payment._work_times = self.work_time_repo.get_work_times(db_hour_payment.id,
                                                                      paid=work_time_paid,
                                                                      boundary=work_time_boundary, pay=pay)
        return hour_payment

    def get_total_hour_payments(self, project_id, work_time_paid=None, work_time_boundary=None, pay=False):
        db_hour_payments = HourPaymentORM.objects.filter(project_id=project_id)
        return [self._get_total_hour_payment(db_hour_payment,
                                             work_time_paid=work_time_paid,
                                             work_time_boundary=work_time_boundary, pay=pay)
                for db_hour_payment in db_hour_payments]

    def get_all(self, project_id):
        db_hour_payments = HourPaymentORM.objects.filter(project_id=project_id)
        return [self._decode_db_hour_payment(db_hour_payment)
                for db_hour_payment in db_hour_payments]

    def create(self, hour_payment):
        try:
            db_hour_payment = HourPaymentORM.objects.create(
                project_id=hour_payment.project_id,
                rate=hour_payment.rate
            )
        except Exception as e:
            raise InvalidEntityException(source='entity', code='not_null', message=str(e))
        return self._decode_db_hour_payment(db_hour_payment)

    def delete(self, hour_payment_id):
        try:
            db_hour_payment = HourPaymentORM.objects.get(id=hour_payment_id)
        except HourPaymentORM.DoesNotExist:
            raise EntityDoesNotExistException
        hour_payment = self._decode_db_hour_payment(db_hour_payment)
        db_hour_payment.delete()
        return hour_payment

    def update(self, hour_payment):
        db_hour_payments = HourPaymentORM.objects.filter(id=hour_payment.id)
        db_hour_payments.update(
            rate=hour_payment.rate
        )
        db_hour_payment = db_hour_payments.get(id=hour_payment.id)
        return self._decode_db_hour_payment(db_hour_payment)

    def _decode_db_hour_payment(self, db_hour_payment):
        fileds = {
            'id': db_hour_payment.id,
            'project_id': db_hour_payment.project.id,
            'rate': db_hour_payment.rate
        }

        return HourPayment(**fileds)

    def _get_worked_times(self, hour_payment_id, paid=False, boundary=None):
        return self.work_time_repo.get_work_times(hour_payment_id, paid=paid, boundary=boundary)


class WorkTimeRepo:
    def create(self, work_time):
        try:
            db_work_time = WorkTimeORM.objects.create(
                hour_payment_id=work_time.hour_payment_id,
                start_work=work_time.start_work,
                end_work=work_time.end_work,
                paid=work_time.paid
            )
            return self._decode_db_work_time(db_work_time)
        except Exception as e:
            raise InvalidEntityException(source='entity', code='not_null', message=str(e))

    def get_all(self, hour_payment_id):
        db_work_times = WorkTimeORM.objects.select_related('hour_payment').filter(hour_payment_id=hour_payment_id)
        return [self._decode_db_work_time(db_work_time) for db_work_time in db_work_times]

    def get(self, work_time_id):
        try:
            db_work_time = WorkTimeORM.objects.select_related('hour_payment').get(id=work_time_id)
        except WorkTimeORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_work_time(db_work_time)

    def get_work_times(self, hour_payment_id, paid=False, boundary=None, pay=False):
        worked_times = []

        if boundary is None:
            db_worked_times = WorkTimeORM.objects.filter(hour_payment_id=hour_payment_id,
                                                         paid=paid)
        else:
            db_worked_times = WorkTimeORM.objects.filter(hour_payment_id=hour_payment_id,
                                                         start_work__gte=boundary[0],
                                                         end_work__lte=boundary[1], paid=paid)

        for db_worked_time in db_worked_times:
            worked_times.append(self._decode_db_work_time(db_worked_time))
        return worked_times

    def update(self, work_time):
        db_work_times = WorkTimeORM.objects.select_related('hour_payment').filter(id=work_time.id)
        db_work_times.update(
            paid=work_time.paid,
            start_work=work_time.start_work,
            end_work=work_time.end_work,
        )
        db_work_time = db_work_times.get(id=work_time.id)
        return self._decode_db_work_time(db_work_time)

    def delete(self, work_time_id):
        try:
            db_work_time = WorkTimeORM.objects.select_related('hour_payment').get(id=work_time_id)
        except WorkTimeORM.DoesNotExist:
            raise EntityDoesNotExistException
        work_time = self._decode_db_work_time(db_work_time)
        db_work_time.delete()
        return work_time

    def _decode_db_work_time(self, db_work_time):
        fileds = {
            'id': db_work_time.id,
            'hour_payment_id': db_work_time.hour_payment.id,
            'start_work': db_work_time.start_work,
            'end_work': db_work_time.end_work,
            'paid': db_work_time.paid
        }

        return WorkTime(**fileds)
