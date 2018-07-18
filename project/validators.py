from PayDevs.exceptions import InvalidEntityException, NoPermissionException


import re
from datetime import timedelta
from django.utils import timezone

#######################Title Validator####################################

def get_title_validators():
		validators = [
									TitleMinLengthValidator(),
									TitleMaxLengthValidator(),
									TitleRegex()] 
		return validators


def validate_title(title, project=None):
		validate(title, project, get_title_validators())



class TitleMinLengthValidator(object):
	def __init__(self, min_len=3):
			self.min_len = min_len


	def validate(self, title, project=None):
			if self.min_len > len(title):
					raise InvalidEntityException(source='title', code='not_allowed', message=
						"Your project title must contain at least %d character." % self.min_len)

class TitleMaxLengthValidator(object):
	def __init__(self, max_len=30):
			self.max_len=max_len


	def validate(self, title, project=None):
		if self.max_len<len(title):
			raise InvalidEntityException(source='title', code='not_allowed', message=
						"Your project title must contain at most %d character." % self.max_len)



class TitleRegex(object):
		def __init__(self):
				self.title_regex = "[a-zA-Z\\d][a-zA-Z-'_,\\d\\.\\t ]+[a-zA-Z'_\\d]+?$"

		def validate(self, title, project=None):
				if not re.match(self.title_regex, title):
						raise InvalidEntityException(source='title', code='not_allowed', message='Title not allowed')



################################Rate Validator#########################################################


def get_rate_validators():
		validators = [PositiveRateValidator(),
		RateTypeValidator()] 
		return validators


def validate_rate(rate, project=None):
		validate(rate, project, get_rate_validators())


class PositiveRateValidator(object):
	def validate(self, rate, project=None):
		if rate <0:
			raise InvalidEntityException(source='rate', code='not_allowed', message="Rate must be positive number.")



class RateTypeValidator(object):
	def validate(self, rate, project=None):
		if not isinstance(rate, (float,int)):
			raise InvalidEntityException(source='rate', code='not_allowed', message="Invalid rate type.")




#########################DateTime Validators#########################################################

def get_date_validator():
	validators=[NoRangeValidator(),
	StartBeforeEndValidator()
	]
	return validators

def validatedate():
	validate(end_date,start_date, project, get_date_validator())

    


class NoRangeValidator(object):

	def validate(self, start_date, end_date, project=None):
		if start_date == end_date:
			raise InvalidEntityException(source='end_date', code='not_allowed', message="No time spent for project.")
	

class StartBeforeEndValidator(object):


	def validate(self, start_date, end_date, project=None):
		if start_date > end_date:
			raise InvalidEntityException(source='end_date', code='not_allowed', message="Set up end_date correctly.")
	


########################Permission Validator###############################################

		




