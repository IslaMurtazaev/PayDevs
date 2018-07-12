from datetime import timedelta

from account.models import UserORM
from django.db import models

# Create your models here.
from django.utils import timezone


class ProjectModel(models.Model):
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    TYPE_OF_PAYMENT = (
        ('H_P', 'Часовой'),
        ('M_P', 'По месяцом'),
        ('T_P', 'По задачам')
    )

    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    start_date = models.DateTimeField(null=True, default=timezone.now())
    end_date = models.DateTimeField(null=True, default=timezone.now() + timedelta(days=30))
    user = models.ForeignKey(UserORM, on_delete=None)
    type_of_payment = models.CharField(max_length=4, choices=TYPE_OF_PAYMENT)
    status = models.BooleanField(default=False)

    def total(self):
        total = 0

        if self.type_of_payment == 'H_P':

            hour_payment = self.hourpaymentmodel_set.all()
            total = sum([i.total() for i in hour_payment])

        elif self.type_of_payment == 'T_P':

            tasks = self.taskpayment_set.all()
            total = sum([task.cost for task in tasks])

        elif self.type_of_payment == 'M_P':

            month_payment = self.monthpayment_set.all()
            total = sum([i.total() for i in month_payment])
        return total



class HourPaymentModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=None)
    rate = models.FloatField(default=0)
    start_rout_date = models.DateTimeField(default=timezone.now())
    end_rout_date = models.DateTimeField(default=timezone.now() + timedelta(days=30))

    def total(self):
        work_times = self.worktime_set.filter(start_work__gte=self.start_rout_date, start_work__lte=self.end_rout_date)
        val = 0
        for work_time in work_times:
            if work_time.is_completed():
                val += (work_time.end_work - work_time.start_work).seconds/3600
        return val * self.rate

    def is_range(self):
        if self.project.start_date <= self.start_rout_date < self.end_rout_date:
            result = True
        else:
            result = False

        return result


class WorkTime(models.Model):
    rate = models.ForeignKey(HourPaymentModel, on_delete=None)
    start_work = models.DateTimeField(default=timezone.now())
    end_work = models.DateTimeField(default=timezone.now() + timedelta(days=30))

    def is_completed(self):
        if timezone.now() >= self.end_work:
            result = True
        else:
            result = False
        return result

    def is_range(self):
        if self.rate.start_rout_date <= self.start_work < self.end_work:
            result = True
        else:
            result = False

        return result




class TaskPayment(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=None)
    name = models.CharField(max_length=500)
    description = models.TextField(null=True)
    cost = models.FloatField(default=0)
    status = models.BooleanField()



class MonthPayment(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=None)
    rate = models.FloatField(default=0)

    def total(self):
        worked_days = self.workday_set.filter(have_worked=True)
        count_worked_day = len([i for i in worked_days if i.is_completed()])
        return self.rate * count_worked_day


class WorkDay(models.Model):
    month_payment = models.ForeignKey(MonthPayment, on_delete=None)
    day = models.DateField(default=timezone.now().date())
    have_worked = models.BooleanField(default=False)

    def is_completed(self):
        if self.day < timezone.now().date():
            return True
        else:
            return False

    def is_range(self):
        start_date = self.month_payment.project.start_date.date()
        end_date = self.month_payment.project.end_date.date()

        if start_date <= self.day:
            return True
        else:
            return False



