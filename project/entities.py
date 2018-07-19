class Project(object):
    
    def __init__(self, id=None, title=None, description=None, start_date=None, end_date=None,\
                 user=None, type_of_payment=None, status=False,  is_mine=False, _entity_type_list=None):
        self._id = id
        self._title = title
        self._description = description
        self._start_date = start_date
        self._end_date = end_date
        self._user = user
        self._type_of_payment = type_of_payment
        self._status = status
        self._is_mine = is_mine
        self._entity_type_list = _entity_type_list

        

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description
    
    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def user(self):
        return self._user

    @property
    def type_of_payment(self):
        return self._type_of_payment

    @property
    def status(self):
        return self._status

    @property
    def is_mine(self):
        return self._is_mine

    @property
    def total(self):
        result = 0
        if self._type_of_payment == 'H_P':
            result = sum(hour_payment.total for hour_payment in self._entity_type_list)
        elif self._type_of_payment == 'M_P':
            result = sum(month_payment.total for month_payment in self._entity_type_list)
        elif self._type_of_payment == 'T_P':
            result = sum(task.price for task in self._entity_type_list)
        return result



class HourPayment(object):


    def __init__(self, project_id=None, rate=None, work_times=None):
        self._project_id = project_id
        self._rate = rate
        self._work_times = work_times


    @property
    def project_id(self):
        return self._project_id


    @property
    def rate(self):
        return self._rate

    @property
    def total(self):
        work_times = self._work_times
        val = 0
        for work_time in work_times:
            if work_time.status:
                val += (work_time.end_work - work_time.start_work).seconds / 3600
        return val * self.rate


class WorkTime(object):

    def __init__(self, id=None, hour_payment_id=None, start_work=None, end_work=None, paid=False):
        self._id = id
        self._hour_payment_id = hour_payment_id
        self._start_work = start_work
        self._end_work = end_work
        self._paid = paid

    @property
    def id(self):
        return self._id

    @property
    def hour_payment(self):
        return self._hour_payment_id

    @property
    def start_work(self):
        return self._start_work

    @property
    def end_work(self):
        return self._end_work
    
    @property
    def paid(self):
        return self._paid






class WorkTask(object):

    def __init__(self, id=None, project_id=None, title=None, description=None, price=0, completed=False, paid=False):
        self._id = id
        self._project_id = project_id
        self._title = title
        self._description = description
        self._price = price
        self._completed = completed
        self._paid = paid


    @property
    def id(self):
        return self._id

    @property
    def project(self):
        return self._project_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @property
    def completed(self):
        return self._completed

    @property
    def paid(self):
        return self._paid



class MonthPayment(object):

    def __init__(self, id=None, project_id=None, rate=None, work_days=None):
        self.id = id
        self._project_id = project_id
        self._rate = rate
        self._work_days = work_days


    @property
    def project_id(self):
        return self._project_id

    @property
    def rate(self):
        return self._rate

    @property
    def total(self):
        worked_days = self._work_days
        count_worked_day = len(set([work_day for work_day in worked_days if work_day.paid]))
        return self.rate * count_worked_day



class WorkedDay(object):

    def __init__(self, id=None, month_payment_id=None, day=None, paid=False, work_days=None):
        self._id = id 
        self._month_payment_id = month_payment_id
        self._day = day
        self._paid = paid


    @property
    def id(self):
        return self._id

    @property
    def month_payment_id(self):
        return self._month_payment_id

    @property
    def day(self):
        return self._day

    @property
    def paid(self):
        return self._paid

