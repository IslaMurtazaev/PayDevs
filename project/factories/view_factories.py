from project.factories.interactor_factories import CreateProjectInteractorFactory, GetProjectInteractorFactory, \
    DeleteProjectInteractorFactory, UpdateProjectInteractorFactory
from project.views import ProjectView


def create_project_factory():
    create_project_interactor = CreateProjectInteractorFactory.create()
    return ProjectView(create_project_interactor)


def get_project_factory():
    get_project_interactor = GetProjectInteractorFactory.create()
    return ProjectView(get_project_interactor)


def delete_project_factory():
    delete_project_interactor = DeleteProjectInteractorFactory.create()
    return ProjectView(delete_project_interactor)


def update_project_factory():
    update_project_interactor = UpdateProjectInteractorFactory.create()
    return ProjectView(update_project_interactor)
