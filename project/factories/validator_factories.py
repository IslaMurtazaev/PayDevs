from account.factories.repo_factories import UserRepoFactory
from project.validators import PermissionValidator, TypeOfPaymentValidator, DateTimeValidator, RateValidator


class PermissionValidatorFactory:
    @staticmethod
    def create():
        user_repo = UserRepoFactory.create()
        return PermissionValidator(user_repo)


class TypeOfPaymentValidatorFactory:
    @staticmethod
    def create():
        return TypeOfPaymentValidator()


class DateTimeValidatorFactory:
    @staticmethod
    def create():
        return DateTimeValidator()


class RateValidatorFactory:
    @staticmethod
    def create():
        return RateValidator
