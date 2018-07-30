from PayDevs.exceptions import InvalidEntityException
from PayDevs.constants import TypesOfPayment

class Project(object):
    
    def __init__(self, id=None, title=None, description=None, start_date=None, end_date=None,\
                 user_id=None, type_of_payment=None, status=False,  is_mine=False, entity_type_list=None):
        self.id = id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id
        self.type_of_payment = type_of_payment
        self.status = status
        self._is_mine = is_mine
        self._entity_type_list = entity_type_list

        

    # @staticmethod
    # def get_timestamp(type_of_payment, worked):
    #     try:
    #         if (type_of_payment == 'H_P'):
    #             total = 0
    #             for worked_time in worked:
    #                 worked_hours = (worked_time.end_work - worked_time.start_work).seconds / 3600
    #                 total += worked_hours
    #             return {'hours': int(total)}
    #
    #         elif (type_of_payment == 'M_P'):
    #             return {'days': len(worked)}
    #
    #     except:
    #         raise InvalidEntityException(source='entities', code='invalid entity',
    #                                      message="Can't get a timestamp of project")

    @property
    def is_mine(self):
        return self._is_mine

    @property
    def total(self):
        result = 0
        if self.type_of_payment == TypesOfPayment.HOUR_PAYMENT:
            result = sum(hour_payment.total for hour_payment in self._entity_type_list)
        elif self.type_of_payment == TypesOfPayment.MONTH_PAYMENT:
            result = sum(month_payment.total for month_payment in self._entity_type_list)
        elif self.type_of_payment == TypesOfPayment.TASK_PAYMENT:
            result = sum(task.price for task in self._entity_type_list)
        return result



class HourPayment(object):

    def __init__(self, id=None, project_id=None, rate=None, work_times=None):
        self.id = id
        self.project_id = project_id
        self.rate = rate
        self._work_times = work_times


    @property
    def total(self):
        work_times = self._work_times
        val = 0
        for work_time in work_times:
            val += (work_time.end_work - work_time.start_work).seconds / 3600
        return val * self.rate


class WorkTime(object):

    def __init__(self, id=None, hour_payment_id=None, start_work=None, end_work=None, paid=False):
        self.id = id
        self.hour_payment_id = hour_payment_id
        self.start_work = start_work
        self.end_work = end_work
        self.paid = paid


   

class WorkTask(object):

    def __init__(self, id=None, project_id=None, title=None, description=None, price=0, completed=False, paid=False):
        self.id = id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.price = price
        self.completed = completed
        self.paid = paid


  

class MonthPayment(object):

    def __init__(self, id=None, project_id=None, rate=None, work_days=None):
        self.id = id
        self.project_id = project_id
        self.rate = rate
        self._work_days = work_days


 
    @property
    def total(self):
        worked_days = self._work_days
        count_worked_day = len(set([work_day.day for work_day
                                    in worked_days]))
        return self.rate * count_worked_day



class WorkedDay(object):

    def __init__(self, id=None, month_payment_id=None, day=None, paid=False):
        self.id = id
        self.month_payment_id = month_payment_id
        self.day = day
        self.paid = paid


   