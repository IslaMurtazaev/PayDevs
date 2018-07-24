from project.factories.repo_factories import ProjectRepoFactory
from project.factories.validate_factories import UserPermissionsValidatorFactory, ProjectDateTimeValidatorFactory
from project.interactors import CreateProjectInteractor, UpdateProjectInteractor, DeleteProjectInteractor, \
    GetProjectInteractor


class CreateProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        project_date_time = ProjectDateTimeValidatorFactory.create()
        return CreateProjectInteractor(project_repo, validate_user_project, project_date_time)


class UpdateProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return UpdateProjectInteractor(project_repo, validate_user_project)


class DeleteProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return DeleteProjectInteractor(project_repo, validate_user_project)



class GetProjectInteractorFactory(object):
    @staticmethod
    def create():
        project_repo = ProjectRepoFactory.create()
        validate_user_project = UserPermissionsValidatorFactory.create()
        return GetProjectInteractor(project_repo, validate_user_project)
