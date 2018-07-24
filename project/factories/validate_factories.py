from account.factories.repo_factories import UserRepoFactory
from project.validators import UserPermissionsValidator, ProjectDateTimeValidator


class UserPermissionsValidatorFactory():
    @staticmethod
    def create():
        create_user_repo = UserRepoFactory.create()
        return UserPermissionsValidator(create_user_repo)



class ProjectDateTimeValidatorFactory:
    @staticmethod
    def create():
        return ProjectDateTimeValidator()