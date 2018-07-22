import datetime

from django.test import TestCase
from account.models import UserORM
from project.models import ProjectORM, HourPaymentORM, WorkTimeORM, WorkTaskORM, MonthPaymentORM, WorkedDayORM
from project.entities import Project, WorkTask, WorkedDay, MonthPayment, HourPayment, WorkTime
from project.repositories import ProjectRepo, WorkTaskRepo, WorkedDayRepo, MonthPaymentRepo, HourPaymentRepo, \
    WorkTimeRepo
from project.interactors import GetProjectInteractor, CreateProjectInteractor
from PayDevs.exceptions import *
from project.validators import *


# -------------------------- Project_Tests ------------------------------------- #


class WorkTaskRepoMethodsTest(TestCase):

    def setUp(self):
        self.user = UserORM.objects.create(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )
        self.project = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user=self.user

        )


    def test_method_create(self):
        work_task_repo = WorkTaskRepo()
        work_task = WorkTask(
            title='Test Work Task',
            description='Test method create',
            paid=False,
            price=100,
            project_id=self.project.id,
            completed=True,
        )
        work_task_create = work_task_repo.create(work_task)
        self.assertEqual(work_task_create.title, 'Test Work Task')
        self.assertEqual(work_task_create.description, 'Test method create')
        self.assertEqual(work_task_create.paid, False)
        self.assertEqual(work_task_create.completed, True)

        db_work_task = WorkTaskORM.objects.get(id=work_task_create.id)

        self.assertEqual(db_work_task.title, work_task_create.title)
        self.assertEqual(db_work_task.description, work_task_create.description)
        self.assertEqual(db_work_task.paid, work_task_create.paid)
        self.assertEqual(db_work_task.completed, work_task_create.completed)
        self.assertEqual(db_work_task.project_id, work_task_create.project_id)
        self.assertEqual(db_work_task.price, work_task_create.price)


    def test_method_get(self):
        work_task_repo = WorkTaskRepo()
        work_task = WorkTask(
            title='Test Work Task',
            description='Test method create',
            paid=False,
            price=100,
            project_id=self.project.id,
            completed=True,
        )
        work_task_create = work_task_repo.create(work_task)
        work_task_get = work_task_repo.get(work_task_create.id)
        self.assertEqual(work_task_get.title, work_task_create.title)
        self.assertEqual(work_task_get.description, work_task_create.description)
        self.assertEqual(work_task_get.paid, work_task_create.paid)
        self.assertEqual(work_task_get.completed, work_task_create.completed)
        self.assertEqual(work_task_get.project_id, work_task_create.project_id)
        self.assertEqual(work_task_get.price, work_task_create.price)
        with self.assertRaises(EntityDoesNotExistException):
            work_task_repo.get(work_task_create.id + 56165156)

    def test_method_update(self):
        work_task_repo = WorkTaskRepo()
        work_task = WorkTask(
            title='Test Work Task',
            description='Test method create',
            paid=True,
            price=100,
            project_id=self.project.id,
            completed=True,
        )

        work_task_create = work_task_repo.create(work_task)

        work_task_update_1 = WorkTask(
            id=work_task_create.id,
            title='Test Work Task Update',
            description='Test method create update',
            price=150,
            paid=False,
            project_id=25616,   # не дожен изменятся
            completed=work_task_create.completed,
        )

        work_task_update = work_task_repo.update(work_task_update_1)

        self.assertEqual(work_task_update.title, 'Test Work Task Update')
        self.assertEqual(work_task_update.description, 'Test method create update')
        self.assertEqual(work_task_update.paid, False)
        self.assertEqual(work_task_update.completed, True)
        self.assertEqual(work_task_update.project_id, work_task_create.project_id)
        self.assertEqual(work_task_update.price, 150)



    def test_method_delete(self):
        work_task_repo = WorkTaskRepo()
        work_task = WorkTask(
            title='Test Work Task',
            description='Test method create',
            paid=False,
            price=100,
            project_id=self.project.id,
            completed=True,
        )
        work_task_create = work_task_repo.create(work_task)
        self.assertIsNotNone(work_task_repo.get(work_task_create.id))
        self.assertIsNotNone(WorkTaskORM.objects.get(id=work_task_create.id))

        work_task_delete = work_task_repo.delete(work_task_create.id)

        with self.assertRaises(EntityDoesNotExistException):
            work_task_repo.get(work_task_create.id)

        with self.assertRaises(WorkTaskORM.DoesNotExist):
            WorkTaskORM.objects.get(id=work_task_create.id)

        self.assertEqual(work_task_delete.title, 'Test Work Task')
        self.assertEqual(work_task_delete.description, 'Test method create')
        self.assertEqual(work_task_delete.paid, False)
        self.assertEqual(work_task_delete.completed, True)
        self.assertEqual(work_task_delete.project_id, self.project.id)
        self.assertEqual(work_task_delete.price, 100)


    def test_method__decode_db_work_task(self):
        work_task_repo = WorkTaskRepo()
        db_work_task = WorkTaskORM.objects.create(
            title='Test Work Task',
            description='Test method create',
            paid=False,
            price=100,
            project_id=self.project.id,
            completed=True,
        )
        work_task = work_task_repo._decode_db_work_task(db_work_task)
        self.assertEqual(work_task.id, db_work_task.id)
        self.assertEqual(work_task.title, db_work_task.title)
        self.assertEqual(work_task.description, db_work_task.description)
        self.assertEqual(work_task.paid, db_work_task.paid)
        self.assertEqual(work_task.completed, db_work_task.completed)
        self.assertEqual(work_task.project_id, db_work_task.project_id)
        self.assertEqual(work_task.price, db_work_task.price)


    def test_method_get_all(self):
        work_task_repo = WorkTaskRepo()
        for i in range(10):
            db_work_task = WorkTaskORM.objects.create(
                title='Test Work Task',
                description='Test method create',
                paid=False,
                price=100,
                project_id=self.project.id,
                completed=True,
            )
            work_task_repo._decode_db_work_task(db_work_task)

        work_tasks = work_task_repo.get_all(self.project.id)
        self.assertEqual(type(work_tasks), list)
        self.assertEqual(len(work_tasks), 10)


class WorkedDayRepoMethodTest(TestCase):

    def setUp(self):
        self.user = UserORM.objects.create(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )
        self.project = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user=self.user

        )

        self.month_payment = MonthPaymentORM.objects.create(
            project_id=self.project.id,
            rate=50,
        )

        self.worked_day_repo = WorkedDayRepo()



    def test_method__decode_db_worked_day(self):
        db_worked_day = WorkedDayORM.objects.create(
            month_payment_id=self.month_payment.id,
            paid=False,
            day=datetime.datetime.now().date()

        )
        worked_day = self.worked_day_repo._decode_db_worked_day(db_worked_day)
        self.assertEqual(worked_day.id, db_worked_day.id)
        self.assertEqual(worked_day.paid, db_worked_day.paid)
        self.assertEqual(worked_day.month_payment_id, db_worked_day.month_payment.id)
        self.assertEqual(worked_day.day, db_worked_day.day)


    def test_method_create(self):
        worked_day = WorkedDay(
            month_payment_id=self.month_payment.id,
            paid=False,
            day=datetime.datetime.now().date()
        )

        worked_day_create = self.worked_day_repo.create(worked_day)
        db_worked_day = WorkedDayORM.objects.get(id=worked_day_create.id)
        self.assertEqual(worked_day_create.id, db_worked_day.id)
        self.assertEqual(worked_day_create.paid, db_worked_day.paid)
        self.assertEqual(worked_day_create.month_payment_id, db_worked_day.month_payment.id)
        self.assertEqual(worked_day_create.day, db_worked_day.day)


    def test_method_get(self):

        worked_day = WorkedDay(
            month_payment_id=self.month_payment.id,
            paid=False,
            day=datetime.datetime.now().date()
        )

        worked_day_create = self.worked_day_repo.create(worked_day)
        worked_day_get = self.worked_day_repo.get(worked_day_create.id)

        self.assertEqual(worked_day_get.id, worked_day_create.id)
        self.assertEqual(worked_day_get.month_payment_id, worked_day_create.month_payment_id)
        self.assertEqual(worked_day_get.day, worked_day_create.day)
        self.assertEqual(worked_day_get.paid, worked_day_create.paid)

        with self.assertRaises(EntityDoesNotExistException):
            self.worked_day_repo.get(worked_day_create.id + 56156)


    def test_method_update(self):
        worked_day = WorkedDay(
            month_payment_id=self.month_payment.id,
            paid=False,
            day=datetime.datetime.now().date()
        )

        worked_day_create = self.worked_day_repo.create(worked_day)

        worked_day_update_1 = WorkedDay(
            id=worked_day_create.id,
            paid=True,
            day=datetime.datetime.now().date() + timedelta(days=2)
        )

        worked_day_update = self.worked_day_repo.update(worked_day_update_1)

        self.assertEqual(worked_day_update.id, worked_day_create.id)
        self.assertEqual(worked_day_update.month_payment_id, worked_day_create.month_payment_id)
        self.assertEqual(worked_day_update.day, datetime.datetime.now().date() + timedelta(days=2))
        self.assertEqual(worked_day_update.paid, True)


    def test_method_delete(self):
        worked_day = WorkedDay(
            month_payment_id=self.month_payment.id,
            paid=False,
            day=datetime.datetime.now().date()
        )

        worked_day_create = self.worked_day_repo.create(worked_day)
        self.assertIsNotNone(self.worked_day_repo.get(worked_day_create.id))
        self.assertIsNotNone(WorkedDayORM.objects.get(id=worked_day_create.id))
        self.worked_day_repo.delete(worked_day_create.id)

        with self.assertRaises(EntityDoesNotExistException):
            self.worked_day_repo.get(worked_day_create.id)

        with self.assertRaises(WorkedDayORM.DoesNotExist):
            WorkedDayORM.objects.get(id=worked_day_create.id)


    def test_method_gat_all(self):
        COUNT_WORK_DAY = 10
        for i in range(COUNT_WORK_DAY):
            worked_day = WorkedDay(
                month_payment_id=self.month_payment.id,
                paid=False,
                day=datetime.datetime.now().date() + timedelta(days=i)
            )

            self.worked_day_repo.create(worked_day)

        worked_days = self.worked_day_repo.get_all(self.month_payment.id)
        self.assertEqual(type(worked_days), list)
        self.assertEqual(len(worked_days), COUNT_WORK_DAY)




class MonthPaymentTest(TestCase):

    COUNT_WORK_DAY = 10

    def setUp(self):
        self.user = UserORM.objects.create(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )
        self.project = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user=self.user

        )

        self.month_payment_repo = MonthPaymentRepo()
        self.worked_day_repo = WorkedDayRepo()




    def test_method_create(self):
        month_payment = MonthPayment(
            project_id=self.project.id,
            rate=100,

        )


        month_payment_create = self.month_payment_repo.create(month_payment)
        db_month_payment = MonthPaymentORM.objects.get(id=month_payment_create.id)

        self.assertEqual(month_payment_create.id, db_month_payment.id)
        self.assertEqual(month_payment_create.project_id, db_month_payment.project.id)
        self.assertEqual(month_payment_create.rate, db_month_payment.rate)


    def test_method_get(self):
        month_payment = MonthPayment(
            project_id=self.project.id,
            rate=100,

        )
        month_payment_create = self.month_payment_repo.create(month_payment)
        month_payment_get = self.month_payment_repo.get(month_payment_id=month_payment_create.id)

        with self.assertRaises(EntityDoesNotExistException):
            self.month_payment_repo.get(month_payment_id=month_payment_create.id+5665)

        self.assertEqual(month_payment_create.id, month_payment_get.id)
        self.assertEqual(month_payment_create.project_id, month_payment_get.project_id)
        self.assertEqual(month_payment_create.rate, month_payment_get.rate)



    def test_method_update(self):
        month_payment = MonthPayment(
            project_id=self.project.id,
            rate=100,

        )
        month_payment_create = self.month_payment_repo.create(month_payment)
        month_payment_update_1 = MonthPayment(
            id=month_payment_create.id,
            rate=500
        )
        month_payment_update = self.month_payment_repo.update(month_payment_update_1)
        self.assertEqual(month_payment_update.id, month_payment_create.id)
        self.assertEqual(month_payment_update.rate, 500)
        self.assertEqual(month_payment_update.project_id, month_payment_create.project_id)


    def test_method_delete(self):
        month_payment = MonthPayment(
            project_id=self.project.id,
            rate=100,

        )
        month_payment_create = self.month_payment_repo.create(month_payment)
        id = month_payment_create.id
        self.assertIsNotNone(self.month_payment_repo.get(id))
        self.assertIsNotNone(MonthPaymentORM.objects.get(id=id))
        month_payment_delete = self.month_payment_repo.delete(id)
        with self.assertRaises(EntityDoesNotExistException):
            self.month_payment_repo.get(id)

        with self.assertRaises(MonthPaymentORM.DoesNotExist):
            MonthPaymentORM.objects.get(id=id)

        self.assertEqual(month_payment_delete.id, id)


    def test_get_all(self):
        for i in range(10):
            month_payment = MonthPayment(
                project_id=self.project.id,
                rate=100,

            )
            self.month_payment_repo.create(month_payment)


        month_payments = self.month_payment_repo.get_all(project_id=self.project.id)
        self.assertEqual(type(month_payments), list)
        self.assertEqual(len(month_payments), 10)
        for month_payment in month_payments:
            self.assertEqual(month_payment.project_id, self.project.id)
            self.assertEqual(month_payment.rate, 100)



    def test_method__decode_db_month_payment(self):
        db_month_payment = MonthPaymentORM.objects.create(
            project_id=self.project.id,
            rate=100,

        )
        month_payment = self.month_payment_repo._decode_db_month_payment(db_month_payment)

        self.assertEqual(db_month_payment.id, month_payment.id)
        self.assertEqual(db_month_payment.project.id, month_payment.project_id)
        self.assertEqual(db_month_payment.rate, month_payment.rate)



    def test_method__get_worked_days(self):
        month_payment = MonthPayment(
            rate=100,
            project_id=self.project.id,
        )

        month_payment = self.month_payment_repo.create(month_payment)
        for i in range(self.COUNT_WORK_DAY):
            worked_day = WorkedDay(
                month_payment_id=month_payment.id,
                paid=False,
                day=datetime.datetime.now().date() + timedelta(days=i)
            )

            self.worked_day_repo.create(worked_day)

        worked_days = self.month_payment_repo._get_worked_days(month_payment.id)
        self.assertEqual(type(worked_days), list)
        self.assertEqual(len(worked_days), self.COUNT_WORK_DAY)
        # month_payment = self.month_payment_repo.get(month_payment.id)
        # self.assertEqual(type(month_payment._work_days), list)
        # self.assertEqual(len(month_payment._work_days), self.COUNT_WORK_DAY)
        # self.assertEqual(month_payment.total, 100 * self.COUNT_WORK_DAY)


    def test_method__get_worked_days_filter_paid(self):
        month_payment = MonthPayment(
            rate=100,
            project_id=self.project.id,
        )

        month_payment = self.month_payment_repo.create(month_payment)
        for i in range(self.COUNT_WORK_DAY):
            worked_day = WorkedDay(
                month_payment_id=month_payment.id,
                paid=i % 2 == 0,
                day=datetime.datetime.now().date() + timedelta(days=i)
            )

            self.worked_day_repo.create(worked_day)

        worked_days = self.month_payment_repo._get_worked_days(month_payment.id, paid=True)
        self.assertEqual(type(worked_days), list)
        self.assertEqual(len(worked_days), 5)
        for worked_day in worked_days:
            self.assertEqual(worked_day.paid, True)

        worked_days = self.month_payment_repo._get_worked_days(month_payment.id, paid=False)
        self.assertEqual(type(worked_days), list)
        self.assertEqual(len(worked_days), 5)
        for worked_day in worked_days:
            self.assertEqual(worked_day.paid, False)


    def test_method__get_worked_days_filter_last_month_days(self):
        month_payment = MonthPayment(
            rate=100,
            project_id=self.project.id,
        )

        month_payment = self.month_payment_repo.create(month_payment)
        for i in range(20):
            worked_day = WorkedDay(
                month_payment_id=month_payment.id,
                paid=i % 2 == 0,
                day=datetime.datetime.now().date() - timedelta(days=(datetime.datetime.now().day - 10) - i + 30)
            )

            self.worked_day_repo.create(worked_day)

        worked_days = self.month_payment_repo._get_worked_days(month_payment.id,
                                                               last_month_days=timezone.now().replace(day=1).date())
        self.assertEqual(type(worked_days), list)
        self.assertEqual(len(worked_days), 20)

        month_payment2 = self.month_payment_repo.create(month_payment)
        for i in range(20):
            worked_day = WorkedDay(
                month_payment_id=month_payment2.id,
                paid=i % 2 == 0,
                day=datetime.datetime.now().replace(day=1).date() + timedelta(days=i)
            )


            self.worked_day_repo.create(worked_day)

        worked_days = self.month_payment_repo._get_worked_days(month_payment2.id,
                                                               last_month_days=timezone.now().replace(day=1).date())
        self.assertEqual(type(worked_days), list)
        self.assertEqual(len(worked_days), 0)

        worked_days = self.month_payment_repo._get_worked_days(month_payment2.id,
                                                               last_month_days=timezone.now().date())
        self.assertEqual(type(worked_days), list)
        self.assertEqual(len(worked_days), 20)



class WorkTimeTest(TestCase):


    def setUp(self):
        self.user = UserORM.objects.create(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )
        self.project = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user=self.user

        )

        self.hour_payment = HourPaymentORM.objects.create(
            project=self.project,
            rate=500
        )


        self.work_time_repo = WorkTimeRepo()


    def test_method_create(self):
        work_time = WorkTime(
            hour_payment_id=self.hour_payment.id,
            start_work=datetime.datetime.now() - timedelta(hours=1),
            end_work=datetime.datetime.now(),
            paid=False
        )

        work_time_crate = self.work_time_repo.create(work_time)
        db_work_time = WorkTimeORM.objects.get(id=work_time_crate.id)

        self.assertEqual(work_time_crate.id, db_work_time.id)
        self.assertEqual(work_time_crate.hour_payment_id, db_work_time.hour_payment.id)
        self.assertEqual(work_time_crate.paid, db_work_time.paid)
        # self.assertEqual(work_time_crate.start_work, db_work_time.start_work. + timedelta(hours=6))
        # self.assertEqual(work_time_crate.end_work, db_work_time.end_work + timedelta(hours=6))


    def test_method_get(self):
        work_time = WorkTime(
            hour_payment_id=self.hour_payment.id,
            start_work=datetime.datetime.now() - timedelta(hours=1),
            end_work=datetime.datetime.now(),
            paid=False
        )

        work_time_crate = self.work_time_repo.create(work_time)
        work_time_get = self.work_time_repo.get(work_time_crate.id)
        with self.assertRaises(EntityDoesNotExistException):
            self.work_time_repo.get(work_time_crate.id + 23423423423)

        self.assertEqual(work_time_get.id, work_time_crate.id)
        self.assertEqual(work_time_get.hour_payment_id, work_time_crate.hour_payment_id)
        self.assertEqual(work_time_get.paid, work_time_crate.paid)
        # self.assertEqual(work_time_get.start_work, work_time_crate.start_work)
        # self.assertEqual(work_time_get.end_work, work_time_crate.end_work)


    def test_method_update(self):
        work_time = WorkTime(
            hour_payment_id=self.hour_payment.id,
            start_work=datetime.datetime.now() - timedelta(hours=1),
            end_work=datetime.datetime.now(),
            paid=False
        )

        work_time_crate = self.work_time_repo.create(work_time)

        work_time_update_1 = WorkTime(
            id=work_time_crate.id,
            start_work=datetime.datetime.now() - timedelta(hours=3),
            end_work=work_time_crate.end_work,
            paid=True
        )
        work_time_update = self.work_time_repo.update(work_time_update_1)

        self.assertEqual(work_time_update.hour_payment_id, work_time_crate.hour_payment_id)
        self.assertEqual(work_time_update.paid, True)
        self.assertEqual(work_time_update.id, work_time_crate.id)
        # self.assertEqual(work_time_update.start_work, datetime.datetime.now() - timedelta(hours=3))


    def test_method_delete(self):
        work_time = WorkTime(
            hour_payment_id=self.hour_payment.id,
            start_work=datetime.datetime.now() - timedelta(hours=1),
            end_work=datetime.datetime.now(),
            paid=False
        )

        work_time_crate = self.work_time_repo.create(work_time)

        self.assertIsNotNone(self.work_time_repo.get(work_time_crate.id))
        self.assertIsNotNone(WorkTimeORM.objects.get(id=work_time_crate.id))

        work_time_delete = self.work_time_repo.delete(work_time_crate.id)

        with self.assertRaises(EntityDoesNotExistException):
            self.work_time_repo.get(work_time_crate.id)

        with self.assertRaises(WorkTimeORM.DoesNotExist):
            WorkTimeORM.objects.get(id=work_time_crate.id)


    def test_method_get_all(self):
        COUNT_WORK_TIME = 10
        for i in range(COUNT_WORK_TIME):
            work_time = WorkTime(
                hour_payment_id=self.hour_payment.id,
                start_work=datetime.datetime.now() - timedelta(hours=1),
                end_work=datetime.datetime.now(),
                paid=False
            )

            self.work_time_repo.create(work_time)

        work_times = self.work_time_repo.get_all(hour_payment_id=self.hour_payment.id)
        self.assertEqual(type(work_times), list)
        self.assertEqual(len(work_times), COUNT_WORK_TIME)
        for i in work_times:
            self.assertEqual(i.hour_payment_id, self.hour_payment.id)
            self.assertEqual(i.paid, False)


    def test_method__decode_db_work_time(self):
        db_work_time = WorkTimeORM.objects.create(
            hour_payment_id=self.hour_payment.id,
            paid=False,
            start_work=datetime.datetime.now() - timedelta(hours=1),
            end_work=datetime.datetime.now()
        )

        work_time = self.work_time_repo._decode_db_work_time(db_work_time)

        self.assertIsNotNone(work_time.id)
        self.assertEqual(type(work_time.id), int)
        self.assertEqual(work_time.hour_payment_id, db_work_time.hour_payment_id)
        self.assertEqual(work_time.paid, db_work_time.paid)




class HouPaymentMethodTest(TestCase):

    def setUp(self):
        self.user = UserORM.objects.create(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )
        self.project = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user=self.user

        )

        self.hour_payment_repo = HourPaymentRepo()


    def test_method__decode_db_hour_payment(self):

        db_hour_payment = HourPaymentORM.objects.create(
            project=self.project,
            rate=500,
        )

        hour_payment = self.hour_payment_repo._decode_db_hour_payment(db_hour_payment)
        self.assertIsNotNone(hour_payment.id)
        self.assertEqual(type(hour_payment.id), int)
        self.assertEqual(hour_payment.project_id, db_hour_payment.project.id)
        self.assertEqual(hour_payment.rate, db_hour_payment.rate)


    def test_method_create(self):
        hour_payment = HourPayment(
            project_id=self.project.id,
            rate=500
        )

        hour_payment_create = self.hour_payment_repo.create(hour_payment)
        db_hour_payment = HourPaymentORM.objects.get(id=hour_payment_create.id)
        self.assertEqual(hour_payment_create.id, db_hour_payment.id)
        self.assertEqual(hour_payment_create.rate, db_hour_payment.rate)
        self.assertEqual(hour_payment_create.project_id, db_hour_payment.project.id)

    def test_method_get(self):
        hour_payment = HourPayment(
            project_id=self.project.id,
            rate=500
        )

        hour_payment_create = self.hour_payment_repo.create(hour_payment)
        hour_payment_get = self.hour_payment_repo.get(hour_payment_create.id)

        self.assertEqual(hour_payment_get.id, hour_payment_create.id)
        self.assertEqual(hour_payment_get.rate, hour_payment_create.rate)
        self.assertEqual(hour_payment_get.project_id, hour_payment_create.project_id)


    def test_method_update(self):
        hour_payment = HourPayment(
            project_id=self.project.id,
            rate=500
        )

        hour_payment_create = self.hour_payment_repo.create(hour_payment)

        hour_payment_update_1 = HourPayment(
            id=hour_payment_create.id,
            rate=1000
        )
        hour_payment_update = self.hour_payment_repo.update(hour_payment_update_1)
        self.assertEqual(hour_payment_update.id, hour_payment_create.id)
        self.assertEqual(hour_payment_update.rate, 1000)


    def delete(self):
        hour_payment = HourPayment(
            project_id=self.project.id,
            rate=500
        )

        hour_payment_create = self.hour_payment_repo.create(hour_payment)
        self.assertIsNotNone(self.hour_payment_repo.get(hour_payment_id=hour_payment_create.id))
        self.assertIsNotNone(HourPaymentORM.objects.get(id=hour_payment_create.id))
        hour_payment_delete = self.hour_payment_repo.delete(hour_payment_create.id)

        with self.assertRaises(EntityDoesNotExistException):
            self.hour_payment_repo.get(hour_payment_create.id)

        with self.assertRaises(HourPaymentORM.DoesNotExist):
            HourPaymentORM.objects.get(id=hour_payment_create.id)

        self.assertIsNotNone(hour_payment_delete)


    def test_method_get_worked_times_paid(self):
        hour_payment = HourPayment(
            project_id=self.project.id,
            rate=500
        )
        hour_payment_create = self.hour_payment_repo.create(hour_payment)
        work_time_repo = WorkTimeRepo()
        for i in range(10):
            work_time = WorkTime(
                hour_payment_id=hour_payment_create.id,
                start_work=datetime.datetime.now() - timedelta(hours=1),
                end_work=datetime.datetime.now(),
                paid=i % 2 == 0
            )
            work_time_repo.create(work_time)


        work_times = self.hour_payment_repo._get_worked_times(hour_payment_create.id)
        self.assertEqual(type(work_times), list)
        self.assertEqual(len(work_times), 10)
        work_times = self.hour_payment_repo._get_worked_times(hour_payment_create.id, paid=False)
        self.assertEqual(type(work_times), list)
        self.assertEqual(len(work_times), 5)
        for work_time in work_times:
            self.assertEqual(work_time.paid, False)
        work_times = self.hour_payment_repo._get_worked_times(hour_payment_create.id, paid=True)
        self.assertEqual(type(work_times), list)
        self.assertEqual(len(work_times), 5)
        for work_time in work_times:
            self.assertEqual(work_time.paid, True)


    def test_method_get_worked_times_boundary(self):
        hour_payment = HourPayment(
            project_id=self.project.id,
            rate=500
        )
        hour_payment_create = self.hour_payment_repo.create(hour_payment)
        work_time_repo = WorkTimeRepo()
        for i in range(10):
            work_time = WorkTime(
                hour_payment_id=hour_payment_create.id,
                start_work=datetime.datetime.now() - timedelta(days=10-i, hours=1),
                end_work=datetime.datetime.now() - timedelta(days=10-i),
                paid=i % 2 == 0
            )
            work_time_repo.create(work_time)


        boundary = (datetime.datetime.now() - timedelta(days=5, hours=6), datetime.datetime.now()-timedelta(hours=6))
        work_times = self.hour_payment_repo._get_worked_times(hour_payment_create.id)
        self.assertEqual(type(work_times), list)
        self.assertEqual(len(work_times), 10)
        work_times = self.hour_payment_repo._get_worked_times(hour_payment_create.id, boundary=boundary)
        self.assertEqual(type(work_times), list)
        self.assertEqual(len(work_times), 5)

        boundary = (datetime.datetime.now() - timedelta(days=5, hours=6), datetime.datetime.now() -
                    timedelta(hours=6, days=1))
        work_times = self.hour_payment_repo._get_worked_times(hour_payment_create.id, boundary=boundary)
        self.assertEqual(type(work_times), list)
        self.assertEqual(len(work_times), 4)

        work_times = self.hour_payment_repo._get_worked_times(hour_payment_create.id, boundary=boundary, paid=True)
        self.assertEqual(type(work_times), list)
        self.assertEqual(len(work_times), 2)



    def test_method_get_all(self):
        COUNT_HOUR_PAYMENT = 10
        for i in range(COUNT_HOUR_PAYMENT):
            hour_payment = HourPayment(
                project_id=self.project.id,
                rate=500
            )

            self.hour_payment_repo.create(hour_payment)

        hour_payments = self.hour_payment_repo.get_all(project_id=self.project.id)

        self.assertEqual(type(hour_payments), list)
        self.assertEqual(len(hour_payments), COUNT_HOUR_PAYMENT)

        for hour_payment in hour_payments:
            self.assertEqual(hour_payment.rate, 500),
            self.assertEqual(hour_payment.project_id, self.project.id)





class MonthPaymentTotalAndRepoTest(TestCase):

    def setUp(self):
        self.COUNT_WORK_DAY = 10
        self.user = UserORM.objects.create(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )
        self.project = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user=self.user

        )

        self.month_payment_repo = MonthPaymentRepo()
        self.worked_day_repo = WorkedDayRepo()

    def test_total_month_payment_filter_paid(self):
        month_payment = MonthPayment(
            rate=100,
            project_id=self.project.id,
        )

        month_payment = self.month_payment_repo.create(month_payment)
        for i in range(self.COUNT_WORK_DAY):
            worked_day = WorkedDay(
                month_payment_id=month_payment.id,
                paid=i % 3 == 0,
                day=datetime.datetime.now().date() + timedelta(days=i)
            )
            self.worked_day_repo.create(worked_day)

        month_payment_get = self.month_payment_repo.get(month_payment.id, work_day_paid=True)
        total_paid_true = month_payment_get.total
        self.assertEqual(total_paid_true, 4 * month_payment_get.rate)

        month_payment_get = self.month_payment_repo.get(month_payment.id, work_day_paid=False)
        total_paid_false = month_payment_get.total
        self.assertEqual(total_paid_false, 6 * month_payment_get.rate)

        month_payment_get = self.month_payment_repo.get(month_payment.id)
        self.assertEqual(month_payment_get.total, self.COUNT_WORK_DAY * month_payment_get.rate)
        self.assertEqual(month_payment_get.total, total_paid_false + total_paid_true)



    def test_total_month_payment_filter_boundary(self):
        month_payment = MonthPayment(
            rate=100,
            project_id=self.project.id,
        )

        month_payment = self.month_payment_repo.create(month_payment)
        for i in range(self.COUNT_WORK_DAY):
            worked_day = WorkedDay(
                month_payment_id=month_payment.id,
                paid=i % 3 == 0,
                day=timezone.now().replace(day=1).date() - timedelta(days=i + 1)
            )

            self.worked_day_repo.create(worked_day)

        month_payment_get = self.month_payment_repo.get(month_payment.id,
                                                        last_month_days=timezone.now().replace(day=1).date())

        self.assertEqual(month_payment_get.total, self.COUNT_WORK_DAY * month_payment_get.rate)

        month_payment_get = self.month_payment_repo.get(month_payment.id,
                                                        last_month_days=
                                                        timezone.now().replace(day=1).date() - timedelta(days=5))

        self.assertEqual(month_payment_get.total, 5 * month_payment_get.rate)

        month_payment_get = self.month_payment_repo.get(month_payment.id,
                                                        last_month_days=
                                                        timezone.now().replace(day=1).date() - timedelta(days=5),
                                                        work_day_paid=False)
        self.assertEqual(month_payment_get.total, 3 * month_payment_get.rate)

        month_payment_get = self.month_payment_repo.get(month_payment.id,
                                                        last_month_days=
                                                        timezone.now().replace(day=1).date() - timedelta(days=5),
                                                        work_day_paid=True)
        self.assertEqual(month_payment_get.total, 2 * month_payment_get.rate)



class HourPaymentTotalAndRepoTest(TestCase):
    def setUp(self):
        self.user = UserORM.objects.create(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )
        self.project = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user=self.user

        )

        self.hour_payment_repo = HourPaymentRepo()


    def test_total_hour_payment_filter_paid(self):
        hour_payment = HourPayment(
            project_id=self.project.id,
            rate=500
        )
        hour_payment_create = self.hour_payment_repo.create(hour_payment)
        work_time_repo = WorkTimeRepo()
        for i in range(10):
            work_time = WorkTime(
                hour_payment_id=hour_payment_create.id,
                start_work=datetime.datetime.now() - timedelta(days=10 - i, hours=1),
                end_work=datetime.datetime.now() - timedelta(days=10 - i),
                paid=i % 2 == 0
            )
            work_time_repo.create(work_time)

        hour_payment_get = self.hour_payment_repo.get(hour_payment_create.id)
        hour_payment_total = hour_payment_get.total
        self.assertEqual(hour_payment_total, 5000)

        hour_payment_get = self.hour_payment_repo.get(hour_payment_create.id, work_time_paid=False)
        hour_payment_total_false = hour_payment_get.total
        self.assertEqual(hour_payment_total_false, 2500)

        hour_payment_get = self.hour_payment_repo.get(hour_payment_create.id, work_time_paid=True)
        hour_payment_total_true = hour_payment_get.total
        self.assertEqual(hour_payment_total_true, 2500)

        self.assertEqual(hour_payment_total, hour_payment_total_false + hour_payment_total_true)



    def test_total_hour_payment_filter_boundary(self):
        hour_payment = HourPayment(
            project_id=self.project.id,
            rate=500
        )
        hour_payment_create = self.hour_payment_repo.create(hour_payment)
        work_time_repo = WorkTimeRepo()
        for i in range(10):
            work_time = WorkTime(
                hour_payment_id=hour_payment_create.id,
                start_work=datetime.datetime.now() - timedelta(days=10 - i, hours=1),
                end_work=datetime.datetime.now() - timedelta(days=10 - i),
                paid=i % 2 == 0
            )
            work_time_repo.create(work_time)
        boundary = (datetime.datetime.now() - timedelta(days=5, hours=6), datetime.datetime.now() - timedelta(hours=6))
        hour_payment_get = self.hour_payment_repo.get(hour_payment_create.id, work_time_boundary=boundary)
        hour_payment_total = hour_payment_get.total
        self.assertEqual(hour_payment_total, 5 * hour_payment_get.rate)

        boundary = (datetime.datetime.now() - timedelta(days=6, hours=6), datetime.datetime.now() - timedelta(hours=6))
        hour_payment_get = self.hour_payment_repo.get(hour_payment_create.id, work_time_boundary=boundary)
        hour_payment_total = hour_payment_get.total
        self.assertEqual(hour_payment_total, 6 * hour_payment_get.rate)

        boundary = (datetime.datetime.now() - timedelta(days=6, hours=6), datetime.datetime.now() - timedelta(hours=6))
        hour_payment_get = self.hour_payment_repo.get(hour_payment_create.id, work_time_boundary=boundary,
                                                      work_time_paid=True)
        hour_payment_total = hour_payment_get.total
        self.assertEqual(hour_payment_total, 3 * hour_payment_get.rate)

        hour_payment_get = self.hour_payment_repo.get(hour_payment_create.id, work_time_boundary=boundary,
                                                      work_time_paid=False)
        hour_payment_total = hour_payment_get.total
        self.assertEqual(hour_payment_total, 3 * hour_payment_get.rate)



class ProjectRepoTest(TestCase):
    def setUp(self):
        self.user = UserORM.objects.create(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )

        self.project_repo = ProjectRepo()



    def test_method__decode_db_project(self):

        db_project = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user=self.user

        )
        project = self.project_repo._decode_db_project(db_project)

        self.assertEqual(project.id, db_project.id)
        self.assertEqual(project.title, db_project.title)
        self.assertEqual(project.description, db_project.description)
        self.assertEqual(project.type_of_payment, db_project.type_of_payment)
        self.assertEqual(project.user_id, db_project.user.id)


    def test_method_create(self):
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        project_create = self.project_repo.create(project)
        db_project = ProjectORM.objects.get(id=project_create.id)
        self.assertEqual(project_create.id, db_project.id)
        self.assertEqual(project_create.title, db_project.title)
        self.assertEqual(project_create.description, db_project.description)
        self.assertEqual(project_create.type_of_payment, db_project.type_of_payment)
        self.assertEqual(project_create.user_id, db_project.user.id)



    def test_method_update(self):
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        project_create = self.project_repo.create(project)

        update_project = Project(
            id=project_create.id,
            title='Test Project Update',
            description=project_create.description,
            start_date=project_create.start_date,
            end_date=datetime.datetime.now() + timedelta(hours=1)
        )

        project_update = self.project_repo.update(update_project)

        self.assertEqual(project_update.id, project_create.id)
        self.assertEqual(project_update.start_date, project_create.start_date)
        self.assertEqual(project_update.type_of_payment, project_create.type_of_payment)
        self.assertEqual(project_update.title, 'Test Project Update')
        self.assertEqual(project_update.description, 'My Test project')



    def test_method_get(self):
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        project_create = self.project_repo.create(project)

        project_get = self.project_repo.get(project_id=project_create.id)

        self.assertEqual(project_get.id, project_create.id)
        self.assertEqual(project_get.title, project_create.title)
        self.assertEqual(project_get.description, project_create.description)
        self.assertEqual(project_get.type_of_payment, project_create.type_of_payment)
        # self.assertEqual(project_get.start_date, project_create.start_date)
        # self.assertEqual(project_get.end_date, project_create.end_date)
        self.assertEqual(project_get.user_id, project_create.user_id)


    def test_method_get_all(self):
        COUNT_PROJECT = 10
        for i in range(COUNT_PROJECT):
            project = Project(
                title='Test Project',
                description='My Test project',
                type_of_payment='M_P',
                start_date=datetime.datetime.now(),
                user_id=self.user.id
            )

            self.project_repo.create(project)


        projects = self.project_repo.get_all(user_id=self.user.id)
        self.assertEqual(type(projects), list)
        self.assertEqual(len((projects)), COUNT_PROJECT)
        for project in projects:
            self.assertEqual(project.user_id, self.user.id)
            self.assertEqual(project.type_of_payment, 'M_P')
            self.assertEqual(project.title, 'Test Project')
            self.assertEqual(project.description, 'My Test project')


    def test_method_delete(self):
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        project_create = self.project_repo.create(project)

        self.assertIsNotNone(self.project_repo.get(project_create.id))
        self.assertIsNotNone(ProjectORM.objects.get(id=project_create.id))

        project_delete = self.project_repo.delete(project_create.id)

        with self.assertRaises(EntityDoesNotExistException):
            self.project_repo.get(project_create.id)

        with self.assertRaises(ProjectORM.DoesNotExist):
            ProjectORM.objects.get(id=project_create.id)



    def test_method___get_entity_type_list_task_of_payment(self):
        COUNT_TASK = 10
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        project_create = self.project_repo.create(project)
        work_task_repo = WorkTaskRepo()

        for i in range(COUNT_TASK):
            work_task = WorkTask(
                title='Test Work Task',
                description='Test method create',
                paid=False,
                price=100,
                project_id=project_create.id,
                completed=True,
            )

            work_task_repo.create(work_task)

        work_tasks = self.project_repo._get_entity_type_list(project_create.id)
        self.assertEqual(type(work_tasks), list)
        self.assertEqual(len(work_tasks), COUNT_TASK)
        self.assertEqual(type(work_tasks.pop()), WorkTask)
        self.assertNotEqual(type(work_tasks.pop()), HourPayment)
        self.assertNotEqual(type(work_tasks.pop()), MonthPayment)


    def test_method___get_entity_type_list_hour_of_payment(self):
        COUNT_HOUR_PAYMENT = 5
        COUNT_WORK_TIME = 10
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment=''
                            'H_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        project_create = self.project_repo.create(project)
        hour_payment_repo = HourPaymentRepo()


        for i in range(COUNT_HOUR_PAYMENT):
            hour_payment = HourPayment(
                project_id=project_create.id,
                rate=500
            )

            hour_payment_create = hour_payment_repo.create(hour_payment)
            for j in range(COUNT_WORK_TIME):
                work_time = WorkTime(
                    hour_payment_id=hour_payment_create.id,
                    start_work=datetime.datetime.now() - timedelta(days=10 - i, hours=1),
                    end_work=datetime.datetime.now() - timedelta(days=10 - i),
                    paid=False
                )

                WorkTimeRepo().create(work_time)

        hour_payments = self.project_repo._get_entity_type_list(project_create.id)

        self.assertEqual(type(hour_payments), list)
        self.assertEqual(len(hour_payments), COUNT_HOUR_PAYMENT)
        self.assertEqual(type(hour_payments.pop()), HourPayment)
        self.assertEqual(type(hour_payments.pop()._work_times), list)
        self.assertEqual(len(hour_payments.pop()._work_times), COUNT_WORK_TIME)
        self.assertEqual(type(hour_payments.pop()._work_times.pop()), WorkTime)



    def test_method___get_entity_type_list_month_of_payment(self):
        COUNT_MONTH_PAYMENT = 5
        COUNT_WORKED_DAY = 10
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment=''
                            'M_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        project_create = self.project_repo.create(project)
        month_payment_repo = MonthPaymentRepo()
        for i in range(COUNT_MONTH_PAYMENT):
            month_payment = MonthPayment(
                project_id=project_create.id,
                rate=100,

            )

            month_payment = month_payment_repo.create(month_payment)
            for j in range(COUNT_WORKED_DAY):
                worked_day = WorkedDay(
                    month_payment_id=month_payment.id,
                    paid=False,
                    day=datetime.datetime.now().date()-timedelta(days=i)
                )
                WorkedDayRepo().create(worked_day)

        month_payments = self.project_repo._get_entity_type_list(project_id=project_create.id)

        self.assertEqual(type(month_payments), list)
        self.assertEqual(len(month_payments), COUNT_MONTH_PAYMENT)
        self.assertEqual(type(month_payments.pop()), MonthPayment)
        self.assertEqual(type(month_payments.pop()._work_days), list)
        self.assertEqual(len(month_payments.pop()._work_days), COUNT_WORKED_DAY)
        self.assertEqual(type(month_payments.pop()._work_days.pop()), WorkedDay)





class ProjectTotalAndRepoTest(TestCase):
    def setUp(self):
        self.user = UserORM.objects.create(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )

        self.project_repo = ProjectRepo()

    def test_method___get_entity_type_list_task_of_payment_paid(self):
        COUNT_TASK = 10
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        project_create = self.project_repo.create(project)
        work_task_repo = WorkTaskRepo()

        for i in range(COUNT_TASK):
            work_task = WorkTask(
                title='Test Work Task',
                description='Test method create',
                paid=i % 2 == 0,
                price=100 * (i + 1),
                project_id=project_create.id,
                completed=True,
            )

            work_task_repo.create(work_task)

        project = self.project_repo.get(project_create.id)
        self.assertEqual(project.total, 5500.0)

        project = self.project_repo.get(project_create.id, paid=True)
        self.assertEqual(project.total, 2500.0)

        project = self.project_repo.get(project_create.id, paid=False)
        self.assertEqual(project.total, 3000.0)

    def test_method_get_worked_times_paid(self):
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment='H_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )
        project_create = self.project_repo.create(project)
        hour_payment = HourPayment(
            project_id=project_create.id,
            rate=500
        )
        hour_payment_create = HourPaymentRepo().create(hour_payment)

        for i in range(10):
            work_time = WorkTime(
                hour_payment_id=hour_payment_create.id,
                start_work=datetime.datetime.now() - timedelta(hours=1),
                end_work=datetime.datetime.now(),
                paid=i % 2 == 0
            )
            WorkTimeRepo().create(work_time)


        project = self.project_repo.get(project_create.id)
        self.assertEqual(type(project.total), float)
        self.assertEqual(project.total, 5000.0)

        project = self.project_repo.get(project_create.id, paid=True)
        self.assertEqual(type(project.total), float)
        self.assertEqual(project.total, 2500.0)

        project = self.project_repo.get(project_create.id, paid=False)
        self.assertEqual(type(project.total), float)
        self.assertEqual(project.total, 2500.0)


    def test_total_hour_payment_filter_boundary(self):
        COUNT_HOUR_PAYMENT = 5
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment='H_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )
        project_create = self.project_repo.create(project)
        for j in range(COUNT_HOUR_PAYMENT):
            hour_payment = HourPayment(
                project_id=project_create.id,
                rate=500
            )
            hour_payment_create = HourPaymentRepo().create(hour_payment)
            work_time_repo = WorkTimeRepo()
            for i in range(10):
                work_time = WorkTime(
                    hour_payment_id=hour_payment_create.id,
                    start_work=datetime.datetime.now() - timedelta(days=10 - i, hours=1) - timedelta(days=30*j),
                    end_work=datetime.datetime.now() - timedelta(days=10 - i) - timedelta(days=30*j),
                    paid=i % 2 == 0
                )
                work_time_repo.create(work_time)
        boundary = (datetime.datetime.now() - timedelta(days=5, hours=6), datetime.datetime.now() - timedelta(hours=6))
        project = self.project_repo.get(project_create.id, boundary=boundary)
        project_total = project.total
        self.assertEqual(project_total, 5 * 500)

        boundary = (datetime.datetime.now() - timedelta(days=6, hours=6), datetime.datetime.now() - timedelta(hours=6))
        project = self.project_repo.get(project_create.id, boundary=boundary)
        project_total = project.total
        self.assertEqual(project_total, 6 * 500)

        boundary = (datetime.datetime.now() - timedelta(days=6, hours=6), datetime.datetime.now() - timedelta(hours=6))
        project = self.project_repo.get(project_create.id, boundary=boundary,
                                                      paid=True)
        project_total = project.total
        self.assertEqual(project_total, 3 * 500)

        project = self.project_repo.get(project_create.id, boundary=boundary,
                                                      paid=False)
        project_total = project.total
        self.assertEqual(project_total, 3 * 500)
        boundary = (datetime.datetime.now() - timedelta(days=365, hours=6),
                    datetime.datetime.now() - timedelta(hours=6))
        project = self.project_repo.get(project_create.id, boundary=boundary)
        project_total = project.total
        self.assertEqual(project_total, 50 * 500)

        boundary = (datetime.datetime.now() - timedelta(days=60, hours=6),
                    datetime.datetime.now() - timedelta(hours=6))
        project = self.project_repo.get(project_create.id, boundary=boundary)
        project_total = project.total
        self.assertEqual(project_total, 20 * 500)


    def test_total_month_payment(self):
        COUNT_MONTH_PAYMENT = 5
        COUNT_WORKED_DAY = 10
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment=''
                            'M_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        project_create = self.project_repo.create(project)
        month_payment_repo = MonthPaymentRepo()
        for i in range(COUNT_MONTH_PAYMENT):
            month_payment = MonthPayment(
                project_id=project_create.id,
                rate=100 * (i + 1),

            )

            month_payment = month_payment_repo.create(month_payment)
            for j in range(COUNT_WORKED_DAY):
                worked_day = WorkedDay(
                    month_payment_id=month_payment.id,
                    paid=j % 2 == 0,
                    day=datetime.datetime.now().date() - timedelta(days=j) - timedelta(days=30*i)
                )
                WorkedDayRepo().create(worked_day)

        project = self.project_repo.get(project_id=project_create.id)
        self.assertEqual(project.total, 100*10 + 200 * 10 + 300 * 10 + 400 * 10 + 500 * 10)

        project = self.project_repo.get(project_id=project_create.id, paid=False)
        self.assertEqual(project.total, 7500)

        project = self.project_repo.get(project_id=project_create.id, paid=True)
        self.assertEqual(project.total, 7500)

        project = self.project_repo.get(project_id=project_create.id, last_month_days=
        timezone.now().replace(day=1).date())
        self.assertEqual(project.total, 14000)

        project = self.project_repo.get(project_id=project_create.id, last_month_days=
        timezone.now().replace(day=1).date() - timedelta(days=30) )
        self.assertEqual(project.total, 12000)

        project = self.project_repo.get(project_id=project_create.id, last_month_days=
        timezone.now().replace(day=1).date(), paid=True)
        self.assertEqual(project.total, 7000)

        project = self.project_repo.get(project_id=project_create.id, last_month_days=
        timezone.now().replace(day=1).date(), paid=False)
        self.assertEqual(project.total, 7000)







