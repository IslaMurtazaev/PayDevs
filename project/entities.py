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

    @staticmethod
    def get_total(type_of_payment, worked):
        if (type_of_payment == 'H_P'):
            total = 0
            for worked_time in worked:
                worked_hours = (worked_time.end_work - worked_time.start_work).seconds / 3600
                total += worked_hours * worked_time.rate
            return total

        elif (type_of_payment == 'M_P'):
            return sum([worked_day.rate for worked_day in worked])

        else:
            return sum([worked_task.price for worked_task in worked])



class WorkTime(object):

    def __init__(self, id=None, start_work=None, end_work=None, paid=False, rate=0):
        self._id = id
        self._start_work = start_work
        self._end_work = end_work
        self._paid = paid
        self._rate = rate

    @property
    def id(self):
        return self._id

    @property
    def start_work(self):
        return self._start_work

    @property
    def end_work(self):
        return self._end_work
    
    @property
    def paid(self):
        return self._paid

    @property
    def rate(self):
        return self._rate



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




class WorkedDay(object):

    def __init__(self, id=None, day=None, paid=False, rate=0):
        self._id = id 
        self._day = day
        self._paid = paid
        self._rate = rate


    @property
    def id(self):
        return self._id

    @property
    def day(self):
        return self._day

    @property
    def paid(self):
        return self._paid

    @property
    def rate(self):
        return self._rate
