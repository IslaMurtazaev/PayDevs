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
        print(worked_day_create.month_payment_id)
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
        print(month_payments)
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



