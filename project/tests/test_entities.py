from datetime import datetime, timedelta

from django.test import TestCase

from project.entities import WorkedDay, MonthPayment, WorkTime


class MonthPaymentTotalTest(TestCase):
    def setUp(self):
        self.worked_days = []
        for i in range(10):
            worked_day = WorkedDay(
                month_payment_id=1,
                day=datetime.now() - timedelta(days=10 - i),
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
                day=datetime.now() - timedelta(days=1),
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

        for i in range(10):
            work_time = WorkTime()