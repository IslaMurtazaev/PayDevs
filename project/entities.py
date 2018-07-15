class Project(object):
    
    def __init__(self, id=None, title=None, description=None, start_date=None, end_date=None,\
                 user=None, type_of_payment=None, status=False):
        self._id = id
        self._title = title
        self._description = description
        self._start_date = start_date
        self._end_date = end_date
        self._user = user
        self._type_of_payment = type_of_payment
        self._status = status
        

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



class HourPayment(object):

    def __init__(self, id=None, project=None, rate=0, start_rout_date=None, end_rout_date=None):
        self._id = id
        self._project = project
        self._rate = rate
        # self._start_rout_date = start_rout_date
        # self._end_rout_date = end_rout_date


    @property
    def id(self):
        return self._id

    @property
    def project(self):
        return self._project

    @property
    def rate(self):
        return self._rate

    # @property
    # def start_rout_date(self):
    #     return self._start_rout_date
    
    # @property
    # def end_rout_date(self):
    #     return self._end_rout_date



class WorkTime(object):

    def __init__(self, id=None, hour_payment=None, start_work=None, end_work=None, paid=False):
        self._id = id
        self._hour_payment = hour_payment
        self._start_work = start_work
        self._end_work = end_work
        self._paid = paid
        

    @property
    def id(self):
        return self._id

    @property
    def hour_payment(self):
        return self._hour_payment

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

    def __init__(self, id=None, project=None, title=None, description=None, price=0, completed=False, paid=False):
        self._id = id
        self._project = project
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
        return self._project

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

    def __init__(self, id=None, project=None, rate=None):
        self._id = id 
        self._project = project
        self._rate = rate


    @property
    def id(self):
        return self._id

    @property
    def project(self):
        return self._project

    @property
    def rate(self):
        return self._rate



class WorkedDay(object):

    def __init__(self, id=None, month_payment=None, day=None, paid=False):
        self._id = id 
        self._month_payment = month_payment
        self._day = day
        self._paid = paid


    @property
    def id(self):
        return self._id

    @property
    def month_payment(self):
        return self._month_payment

    @property
    def day(self):
        return self._day

    @property
    def paid(self):
        return self._paid
