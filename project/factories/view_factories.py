from project.factories.interactor_factories import CreateProjectInteractorFactory, GetProjectInteractorFactory, \
    DeleteProjectInteractorFactory, UpdateProjectInteractorFactory, GetAllProjectsInteractorFactory, \
    CreateTaskInteractorFactory, GetTaskInteractorFactory, UpdateTaskInteractorFactory, DeleteTaskInteractorFactory, \
    GetAllaskInteractorFactory
from project.views import ProjectView, GetAllProjectsView, TaskView, GetAllTasksView


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


def get_projects_all_factory():
    get_all_project_interactor = GetAllProjectsInteractorFactory().create()
    return GetAllProjectsView(get_all_project_interactor)


def create_task_factory():
    create_task_interactor = CreateTaskInteractorFactory().create()
    return TaskView(create_task_interactor)


def get_task_factory():
    get_task_interactor = GetTaskInteractorFactory().create()
    return TaskView(get_task_interactor)


def update_task_factory():
    get_task_interactor = UpdateTaskInteractorFactory().create()
    return TaskView(get_task_interactor)


def delete_task_factory():
    get_task_interactor = DeleteTaskInteractorFactory().create()
    return TaskView(get_task_interactor)

def get_all_tasks_factory():
    get_task_interactor = GetAllaskInteractorFactory().create()
    return GetAllTasksView(get_task_interactor)