from PayDevs.constants import DATE_TIME_FORMAT, DATE_FORMAT
from PayDevs.exceptions import NoLoggedException, NoPermissionException, InvalidEntityException
import datetime
from  django.utils import timezone


class PermissionValidator:

    def __init__(self, user_repo):
        self.user_repo = user_repo

    @staticmethod
    def validate(logged_id, user_id=None):
        if logged_id is None:
            raise NoLoggedException
        if user_id is not None and logged_id != user_id:
            raise NoPermissionException




class FieldValidator:

    @staticmethod
    def validate_type_of_payment(type_of_payment):
        if type_of_payment not in ('T_P', 'M_P', 'H_P'):
            raise InvalidEntityException(source='validator',  code='other_type_of_payment',
                                         message="The type of payment must be only one of T_P, H_P and M_P")


    def validate_task_payment(self, type_of_payment):
        self._validate_project_payment(type_of_payment, 'T_P')

    def validate_month_payment(self, type_of_payment):
        self._validate_project_payment(type_of_payment, 'M_P')

    def validate_hour_payment(self, type_of_payment):
        self._validate_project_payment(type_of_payment, 'H_P')



    def _validate_project_payment(self, type_of_payment, eq_type_of_payment):
        if type_of_payment != eq_type_of_payment:
            raise InvalidEntityException(source='validate', code='other_type_of_payment',
                                         message="The type of payment for the project must be %s" % eq_type_of_payment)





    @staticmethod
    def validate_datetime_format(date_string):
        if date_string is None:
            return None
        try:
            return datetime.datetime.strptime(date_string, DATE_TIME_FORMAT)
        except:
            raise InvalidEntityException(source='validator',  code='invalid_format', message="Invalid datetime format")

    @staticmethod
    def validate_date_format(date_string):
        if date_string is None:
            return None
        try:
            return datetime.datetime.strptime(date_string, DATE_FORMAT)
        except:
            raise InvalidEntityException(source='validator',  code='invalid_format', message="Invalid date format")

    @staticmethod
    def now_end_date_project(type_of_payment):
        if type_of_payment == 'M_P':
            return timezone.now().replace(day=1)
        elif type_of_payment == 'H_P':
            return timezone.now()
        else:
            return timezone.now()




    @staticmethod
    def validate_rate(rate):
        if rate is None:
            return None
        if not isinstance(rate, (int, float)):
            raise InvalidEntityException(source='validator', code='invalid_rate', message="Invalid type for rate")
        if rate < 0:
            raise InvalidEntityException(source='validator', code='invalid_rate', message="Negative rate")
