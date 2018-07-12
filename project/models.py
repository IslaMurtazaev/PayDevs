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



class HourPaymentORM(models.Model):
    project = models.ForeignKey(ProjectORM, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    start_rout_date = models.DateTimeField(default=timezone.now)
    end_rout_date = models.DateTimeField(null=True)

    # def total(self):
    #     work_times = self.worktime_set.filter(start_work__gte=self.start_rout_date, start_work__lte=self.end_rout_date)
    #     val = 0
    #     for work_time in work_times:
    #         if work_time.is_completed():
    #             val += (work_time.end_work - work_time.start_work).seconds/3600
    #     return val * self.rate

    # def is_range(self):
    #     if self.project.start_date <= self.start_rout_date < self.end_rout_date:
    #         result = True
    #     else:
    #         result = False

    #     return result


# class WorkTimeORM(models.Model):
#     rate = models.ForeignKey(HourPaymentORM, on_delete=None)
#     start_work = models.DateTimeField(default=timezone.now())
#     end_work = models.DateTimeField(default=timezone.now() + timedelta(days=30))

#     def is_completed(self):
#         if timezone.now() >= self.end_work:
#             result = True
#         else:
#             result = False
#         return result

#     def is_range(self):
#         if self.rate.start_rout_date <= self.start_work < self.end_work:
#             result = True
#         else:
#             result = False

#         return result




class TaskPaymentORM(models.Model):
    project = models.ForeignKey(ProjectORM, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True)
    price = models.FloatField(default=0)
    completed = models.BooleanField(default=False)




def current_date():
    return timezone.now().date()


class MonthPaymentORM(models.Model):
    project = models.ForeignKey(ProjectORM, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    day = models.DateField(default=current_date)

    # def total(self):
    #     worked_days = self.workday_set.filter(have_worked=True)
    #     count_worked_day = len([i for i in worked_days if i.is_completed()])
    #     return self.rate * count_worked_day


# class WorkDay(models.Model):
#     month_payment = models.ForeignKey(MonthPayment, on_delete=None)
#     day = models.DateField(default=timezone.now().date())
#     have_worked = models.BooleanField(default=False)

#     def is_completed(self):
#         if self.day < timezone.now().date():
#             return True
#         else:
#             return False

#     def is_range(self):
#         start_date = self.month_payment.project.start_date.date()
#         end_date = self.month_payment.project.end_date.date()

#         if start_date <= self.day:
#             return True
#         else:
#             return False
