import datetime
from django.utils import timezone
from django.test import TestCase
from account.models import UserORM
from project.models import ProjectORM
from project.entities import Project, WorkTask, WorkedDay, MonthPayment, HourPayment, WorkTime
from project.repositories import ProjectRepo, WorkTaskRepo, WorkedDayRepo, MonthPaymentRepo, HourPaymentRepo, \
    WorkTimeRepo
from datetime import timedelta


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