from account.factories.repo_factories import UserRepoFactory
from project.validators import UserPermissionValidator, ProjectDateTimeValidator


class UserPermissionsValidatorFactory:
    @staticmethod
    def create():
        user_repo = UserRepoFactory.create()
        return UserPermissionValidator(user_repo)



class ProjectDateTimeValidatorFactory:
    @staticmethod
    def create():
        return ProjectDateTimeValidator()
