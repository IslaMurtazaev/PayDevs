from datetime import timedelta
from django.db import models
from django.utils import timezone

from account.models import UserORM
from PayDevs.constants import TypesOfPayment


class ProjectORM(models.Model):
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
    
    TYPES_OF_PAYMENT = (
         (TypesOfPayment.HOUR_PAYMENT, 'Почасовая'),
         (TypesOfPayment.MONTH_PAYMENT, 'Помесячная'),
         (TypesOfPayment.TASK_PAYMENT, 'Позадачная')
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



class WorkedDayORM(models.Model):
    month_payment = models.ForeignKey(MonthPaymentORM, on_delete=models.CASCADE)
    day = models.DateField(default=current_date)
    paid = models.BooleanField(default=False)
