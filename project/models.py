from datetime import timedelta
from django.db import models
from django.utils import timezone

from account.models import UserORM


class ProjectORM(models.Model):
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    TYPES_OF_PAYMENT = (
        ('H_P', 'Почасовая'),
        ('M_P', 'Помесячная'),
        ('T_P', 'Позадачная')
    )

    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    start_date = models.DateTimeField(null=True, default=timezone.now)
    end_date = models.DateTimeField(null=True)
    user = models.ForeignKey(UserORM, on_delete=models.CASCADE)
    type_of_payment = models.CharField(max_length=3, choices=TYPES_OF_PAYMENT)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title




class HourPaymentORM(models.Model):
    project = models.ForeignKey(ProjectORM, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)



class WorkTimeORM(models.Model):
    hour_payment = models.ForeignKey(HourPaymentORM, on_delete=models.CASCADE)
    start_work = models.DateTimeField(default=timezone.now)
    end_work = models.DateTimeField(null=True)
    paid = models.BooleanField(default=False)


    # def total(self):
    #     work_times = self.worktime_set.filter(start_work__gte=self.start_rout_date, start_work__lte=self.end_rout_date)
    #     val = 0
    #     for work_time in work_times:
    #         if work_time.is_completed():
    #             val += (work_time.end_work - work_time.start_work).seconds/3600
    #     return val * self.rate




class WorkTaskORM(models.Model):
    project = models.ForeignKey(ProjectORM, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True)
    price = models.FloatField(default=0)
    completed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)


    def __str__(self):
        return self.title    




def current_date():
    return timezone.now().date()


class MonthPaymentORM(models.Model):
    project = models.ForeignKey(ProjectORM, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)


class WorkDayORM(models.Model):
    month_payment = models.ForeignKey(MonthPaymentORM, on_delete=models.CASCADE)
    day = models.DateField(default=current_date)
    paid = models.BooleanField(default=False)
