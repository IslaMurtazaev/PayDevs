from account.models import UserORM
from account.repositories import UserRepo
from project.entities import Project, WorkTask, MonthPayment, WorkedDay, HourPayment, WorkTime
from project.models import ProjectORM, HourPaymentORM, MonthPaymentORM, WorkTaskORM, WorkedDayORM, WorkTimeORM
from PayDevs.exceptions import EntityDoesNotExistException, NoPermissionException


# ------------------------------------------ Project --------------------------------------------#


class ProjectRepo(object):
    def _decode_db_project(self, db_project, is_mine=False, paid=None, last_month_days=None, boundary=None):
        fileds = {
            'id': db_project.id,
            'user_id': db_project.user.id,
            'title': db_project.title,
            'description': db_project.description,
            'start_date': db_project.start_date,
            'end_date': db_project.end_date,
            'type_of_payment': db_project.type_of_payment,
            'status': db_project.status,
            'is_mine': is_mine,
            'entity_type_list': self._get_entity_type_list(db_project.id,
                                                           paid=paid, last_month_days=last_month_days,
                                                           boundary=boundary)
        }

        return Project(**fileds)

    def get(self, project_id, logged_id=None, paid=None, last_month_days=None, boundary=None):
        try:
            db_project = ProjectORM.objects.select_related('user').get(id=project_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_project(db_project, is_mine=(logged_id == db_project.user.id),
                                       paid=paid, last_month_days=last_month_days, boundary=boundary)

    def create(self, project, paid=None, last_month_days=None, boundary=None):
        db_project = ProjectORM.objects.create(
            title=project.title,
            description=project.description,
            user_id=project.user_id,
            start_date=project.start_date,
            end_date=project.end_date,
            status=project.status,
            type_of_payment=project.type_of_payment,
        )

        return self._decode_db_project(db_project=db_project, is_mine=True,
                                       paid=paid, last_month_days=last_month_days, boundary=boundary)

    def delete(self, project_id):
        try:
            db_project = ProjectORM.objects.get(id=project_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        project = self._decode_db_project(db_project)
        db_project.delete()
        return project

    def get_all(self, user_id, paid=None, last_month_days=None, boundary=None):
        try:
            db_projects = ProjectORM.objects.filter(user_id=user_id)
        except ProjectORM.DoesNotExist:
            raise NoPermissionException(message="Invalid user id")

        projects = [self._decode_db_project(db_project, is_mine=True,
                                            paid=paid, last_month_days=last_month_days, boundary=boundary)
                    for db_project in db_projects]
        return projects

    def update(self, project, paid=None, last_month_days=None, boundary=None):
        try:
            db_project = ProjectORM.objects.get(id=project.id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException

        db_project.title = project.title
        db_project.description = project.description
        db_project.status = project.status
        db_project.type_of_payment = project.type_of_payment
        db_project.start_date = project.start_date
        db_project.end_date = project.end_date
        db_project.status = project.status

        db_project.save()

        return self._decode_db_project(db_project, paid=paid, last_month_days=last_month_days, boundary=boundary)

    def _get_entity_type_list(self, project_id, paid=None, last_month_days=None, boundary=None):
        entity_type_list = []
        try:
            db_project = ProjectORM.objects.select_related('user').get(id=project_id)
            if db_project.type_of_payment == 'H_P':
                db_hour_payments = db_project.hourpaymentorm_set.all()
                hour_payment_repo = HourPaymentRepo()
                for db_hour_payment in db_hour_payments:
                    entity_type_list.append(hour_payment_repo._decode_db_hour_payment(
                        db_hour_payment, work_time_paid=paid, work_time_boundary=boundary
                    ))
            elif db_project.type_of_payment == 'M_P':
                db_month_payments = db_project.monthpaymentorm_set.all()
                month_payment_repo = MonthPaymentRepo()
                for db_month_payment in db_month_payments:
                    entity_type_list.append(
                        month_payment_repo._decode_db_month_payment(db_month_payment,
                                                                    work_day_paid=paid,
                                                                    last_month_days=last_month_days))
            elif db_project.type_of_payment == 'T_P':
                if paid is None:
                    db_work_tasks = db_project.worktaskorm_set.filter(completed=True)
                else:
                    db_work_tasks = db_project.worktaskorm_set.filter(paid=paid, completed=True)
                for db_work_task in db_work_tasks:
                    entity_type_list.append(WorkTaskRepo()._decode_db_work_task(db_work_task))

            return entity_type_list
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException


# -------------------------- Work Task ----------------------------------------#



class WorkTaskRepo:
    def get(self, work_task_id):
        try:
            db_work_task = WorkTaskORM.objects.get(id=work_task_id)
        except WorkTaskORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_work_task(db_work_task)

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
        try:
            db_work_task = WorkTaskORM.objects.get(id=work_task.id)
        except WorkTaskORM.DoesNotExist:
            raise EntityDoesNotExistException

        db_work_task.title = work_task.title
        db_work_task.description = work_task.description
        db_work_task.completed = work_task.completed
        db_work_task.paid = work_task.paid
        db_work_task.price = work_task.price
        db_work_task.save()
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


# -------------------------- Month Payment ---------------------------------------- #


class MonthPaymentRepo:
    def _decode_db_month_payment(self, db_month_payment, work_day_paid=None, last_month_days=None):

        fileds = {
            'id': db_month_payment.id,
            'project_id': db_month_payment.project.id,
            'rate': db_month_payment.rate,
            'work_days': self._get_worked_days(db_month_payment.id,
                                               paid=work_day_paid, last_month_days=last_month_days)
        }

        return MonthPayment(**fileds)

    def get(self, month_payment_id, work_day_paid=None, last_month_days=None):
        try:
            db_month_payment = MonthPaymentORM.objects.select_related('project').get(id=month_payment_id)
        except MonthPaymentORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_month_payment(db_month_payment,
                                             work_day_paid=work_day_paid, last_month_days=last_month_days)

    def get_all(self, project_id, work_day_paid=None, last_month_days=None):
        try:
            db_month_payments = MonthPaymentORM.objects.select_related('project').filter(project_id=project_id)
        except MonthPaymentORM.DoesNotExist:
            raise EntityDoesNotExistException

        return [self._decode_db_month_payment(db_month_payment,
                                              work_day_paid=work_day_paid, last_month_days=last_month_days)
                for db_month_payment in db_month_payments]

    def create(self, month_payment, work_day_paid=None, last_month_days=None):
        db_month_payment = MonthPaymentORM.objects.create(
            project_id=month_payment.project_id,
            rate=month_payment.rate
        )
        return self._decode_db_month_payment(db_month_payment,
                                             work_day_paid=work_day_paid, last_month_days=last_month_days)

    def update(self, month_payment, work_day_paid=None, last_month_days=None):
        try:
            db_month_payment = MonthPaymentORM.objects.get(id=month_payment.id)
        except MonthPaymentORM.DoesNotExist:
            raise EntityDoesNotExistException
        db_month_payment.rate = month_payment.rate
        db_month_payment.save()
        return self._decode_db_month_payment(db_month_payment,
                                             work_day_paid=work_day_paid, last_month_days=last_month_days)

    def delete(self, month_payment_id, work_day_paid=None, last_month_days=None):
        try:
            db_month_payment = MonthPaymentORM.objects.get(id=month_payment_id)
        except MonthPaymentORM.DoesNotExist:
            raise EntityDoesNotExistException
        work_task = self._decode_db_month_payment(db_month_payment,
                                                  work_day_paid=work_day_paid, last_month_days=last_month_days)
        db_month_payment.delete()
        return work_task

    def _get_worked_days(self, month_payment_id, paid=None, last_month_days=None):
        worked_days = WorkedDayRepo().get_workdays(month_payment_id, paid=paid, last_month_days=last_month_days)
        return worked_days


class WorkedDayRepo:
    def create(self, worked_day):
        db_worked_day = WorkedDayORM.objects.create(
            month_payment_id=worked_day.month_payment_id,
            day=worked_day.day,
            paid=worked_day.paid
        )
        return self._decode_db_worked_day(db_worked_day)

    def update(self, worked_day):
        try:
            db_worked_day = WorkedDayORM.objects.get(id=worked_day.id)
        except WorkedDayORM.DoesNotExist:
            raise EntityDoesNotExistException

        db_worked_day.day = worked_day.day
        db_worked_day.paid = worked_day.paid
        db_worked_day.save()

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
        return self._decode_db_worked_day(db_wored_day=db_worked_day)

    def get_all(self, month_payment_id):
        try:
            db_worked_days = WorkedDayORM.objects.filter(month_payment_id=month_payment_id)
        except WorkedDayORM.DoesNotExist:
            raise EntityDoesNotExistException

        return [self._decode_db_worked_day(db_worked_day) for db_worked_day in db_worked_days]

    def get_workdays(self, month_payment_id, paid=None, last_month_days=None):
        worked_days = []
        if paid is None:
            if last_month_days is None:
                db_worked_days = WorkedDayORM.objects.filter(month_payment_id=month_payment_id)
            else:
                db_worked_days = WorkedDayORM.objects.filter(month_payment_id=month_payment_id, day__lt=last_month_days)
        else:
            if last_month_days is None:
                db_worked_days = WorkedDayORM.objects.filter(month_payment_id=month_payment_id, paid=paid)
            else:
                db_worked_days = WorkedDayORM.objects.filter(month_payment_id=month_payment_id,
                                                             paid=paid, day__lt=last_month_days)
        for db_worked_day in db_worked_days:
            worked_days.append(self._decode_db_worked_day(db_worked_day))
        return worked_days

    def _decode_db_worked_day(self, db_wored_day):

        fileds = {
            'id': db_wored_day.id,
            'month_payment_id': db_wored_day.month_payment.id,
            'day': db_wored_day.day,
            'paid': db_wored_day.paid
        }
        return WorkedDay(**fileds)


class HourPaymentRepo:
    def get(self, hour_payment_id, work_time_paid=None, work_time_boundary=None):
        try:
            db_hour_payment = HourPaymentORM.objects.select_related('project').get(id=hour_payment_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        return self._decode_db_hour_payment(db_hour_payment,
                                            work_time_paid=work_time_paid, work_time_boundary=work_time_boundary)

    def get_all(self, project_id, work_time_paid=None, work_time_boundary=None):
        try:
            db_hour_payments = HourPaymentORM.objects.filter(project_id=project_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        return [self._decode_db_hour_payment(db_hour_payment,
                                             work_time_paid=work_time_paid, work_time_boundary=work_time_boundary)
                for db_hour_payment in db_hour_payments]

    def create(self, hour_payment):
        db_hour_payment = HourPaymentORM.objects.create(
            project_id=hour_payment.project_id,
            rate=hour_payment.rate
        )
        return self._decode_db_hour_payment(db_hour_payment)

    def delete(self, hour_payment_id, work_time_paid=None, work_time_boundary=None):
        try:
            db_hour_payment = HourPaymentORM.objects.get(id=hour_payment_id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        hour_payment = self._decode_db_hour_payment(db_hour_payment,
                                                    work_time_paid=work_time_paid,
                                                    work_time_boundary=work_time_boundary)
        db_hour_payment.delete()
        return hour_payment

    def update(self, hour_payment, work_time_paid=None, work_time_boundery=None):
        try:
            db_hour_payment = HourPaymentORM.objects.get(id=hour_payment.id)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        db_hour_payment.rate = hour_payment.rate
        db_hour_payment.save()
        return self._decode_db_hour_payment(db_hour_payment, work_time_paid=work_time_paid,
                                            work_time_boundary=work_time_boundery)

    def _decode_db_hour_payment(self, db_hour_payment, work_time_paid=None, work_time_boundary=None):
        fileds = {
            'id': db_hour_payment.id,
            'project_id': db_hour_payment.project.id,
            'rate': db_hour_payment.rate,
            'work_times': self._get_worked_times(db_hour_payment.id, paid=work_time_paid, boundary=work_time_boundary)
        }

        return HourPayment(**fileds)

    def _get_worked_times(self, hour_payment_id, paid=None, boundary=None):
        return WorkTimeRepo().get_work_times(hour_payment_id, paid=paid, boundary=boundary)


class WorkTimeRepo:
    def create(self, work_time):
        db_work_time = WorkTimeORM.objects.create(
            hour_payment_id=work_time.hour_payment_id,
            start_work=work_time.start_work,
            end_work=work_time.end_work,
            paid=work_time.paid
        )
        return self._decode_db_work_time(db_work_time)

    def get_all(self, hour_payment_id):
        try:
            db_work_times = WorkTimeORM.objects.select_related('hour_payment').filter(hour_payment_id=hour_payment_id)
        except WorkTimeORM.DoesNotExist:
            raise EntityDoesNotExistException

        return [self._decode_db_work_time(db_work_time) for db_work_time in db_work_times]

    def get(self, work_time_id):
        try:
            db_work_time = WorkTimeORM.objects.select_related('hour_payment').get(id=work_time_id)
        except WorkTimeORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_work_time(db_work_time)

    def get_work_times(self, hour_payment_id, paid=None, boundary=None):
        worked_times = []

        if paid is None:
            if boundary is None:
                db_worked_times = WorkTimeORM.objects.filter(hour_payment_id=hour_payment_id)
            else:
                db_worked_times = WorkTimeORM.objects.filter(hour_payment_id=hour_payment_id,
                                                             start_work__gte=boundary[0],
                                                             end_work__lte=boundary[1])
        else:
            if boundary is None:
                db_worked_times = WorkTimeORM.objects.filter(hour_payment_id=hour_payment_id,
                                                             paid=paid)
            else:
                db_worked_times = WorkTimeORM.objects.filter(hour_payment_id=hour_payment_id,
                                                             start_work__gte=boundary[0],
                                                             end_work__lte=boundary[1], paid=paid)

        for db_worked_time in db_worked_times:
            worked_times.append(WorkTimeRepo()._decode_db_work_time(db_worked_time))
        return worked_times

    def update(self, work_time):
        try:
            db_work_time = WorkTimeORM.objects.select_related('hour_payment').get(id=work_time.id)
        except WorkTimeORM.DoesNotExist:
            raise EntityDoesNotExistException

        db_work_time.paid = work_time.paid
        db_work_time.start_work = work_time.start_work
        db_work_time.end_work = work_time.end_work

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
