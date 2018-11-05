from datetime import datetime, timedelta
from django.test import TestCase
from project.entities import WorkedDay, MonthPayment, WorkTime, HourPayment, WorkTask, Project


class MonthPaymentTotalTest(TestCase):
    def setUp(self):
        self.worked_days = []
        for i in range(10):
            worked_day = WorkedDay(
                month_payment_id=1,
                day=datetime.now().date() - timedelta(days=10 - i),
                paid=False
            )
            self.worked_days.append(worked_day)


    def test_total_month_payment(self):
        month_payment = MonthPayment(
            project_id=1,
            rate=500,
            work_days=self.worked_days
        )

        self.assertEqual(month_payment.total, 5000)
        self.worked_days.append(
            WorkedDay(
                month_payment_id=1,
                day=datetime.now().date() - timedelta(days=1),
                paid=False
            )
        )
        month_payment = MonthPayment(
            project_id=1,
            rate=500,
            work_days=self.worked_days
        )
        self.assertEqual(month_payment.total, 5000)



class HourPaymentTotalTest(TestCase):

    def setUp(self):
        self.work_times = []

        for i in range(25):
            work_time = WorkTime(
                id=i,
                hour_payment_id=1,
                start_work=datetime.now().replace(hour=10, minute=0, second=0) - timedelta(days=10 - i),
                end_work=datetime.now().replace(hour=19, minute=00, second=0) - timedelta(days=10 - i),
                paid=False
            )
            self.work_times.append(work_time)


    def test_total_hour_paymnet(self):
        hour_payment = HourPayment(
            id=1,
            project_id=1,
            rate=200,
            work_times=self.work_times
        )
        self.assertEqual(hour_payment.total, 45000)



class ProjectTotalTest(TestCase):
    def setUp(self):
        self.worked_days = []
        self.work_times = []
        for i in range(10):
            worked_day = WorkedDay(
                month_payment_id=i,
                day=datetime.now().date() - timedelta(days=10 - i),
                paid=False
            )
            self.worked_days.append(worked_day)
        for i in range(10):
            work_time = WorkTime(
                id=i,
                hour_payment_id=1,
                start_work=datetime.now().replace(hour=10, minute=0, second=0) - timedelta(days=10 - i),
                end_work=datetime.now().replace(hour=19, minute=0, second=0) - timedelta(days=10 - i),
                paid=False
            )
            self.work_times.append(work_time)

        self.tasks = []
        for i in range(10):
            task = WorkTask(
                id=i,
                project_id=1,
                price=(i+1)*100,
            )
            self.tasks.append(task)


    def test_project_total_task_payment(self):
        project = Project(
            title="Test Project",
            description="Testing project",
            type_of_payment='T_P',
            entity_type_list=self.tasks
        )

        self.assertEqual(project.total, 5500)


    def test_project_total_hour_payment(self):
        hour_payments = []
        for i in range(5):
            hour_payment = HourPayment(
                id=i,
                project_id=1,
                rate=200,
                work_times=self.work_times
            )
            hour_payments.append(hour_payment)

        project = Project(
            title="Test Project",
            description="Testing project",
            type_of_payment='H_P',
            entity_type_list=hour_payments
        )
        self.assertEqual(project.total, 90000)

    def test_project_total_month_payment(self):
        month_payments = []
        for i in range(5):
            month_payment = MonthPayment(
                id=i,
                project_id=1,
                rate=1000,
                work_days=self.worked_days
            )
            month_payments.append(month_payment)

        project = Project(
            title="Test Project",
            description="Testing project",
            type_of_payment='M_P',
            entity_type_list=month_payments
        )
        self.assertEqual(project.total, 50000)
