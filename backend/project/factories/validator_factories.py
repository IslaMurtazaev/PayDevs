from account.factories.repo_factories import UserRepoFactory
from project.validators import PermissionValidator, FieldValidator


class PermissionValidatorFactory:
    @staticmethod
    def create():
        user_repo = UserRepoFactory.create()
        return PermissionValidator(user_repo)


class FieldValidatorFactory:
    @staticmethod
    def create():
        return FieldValidator()


