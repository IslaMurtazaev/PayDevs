from project.factories.interactor_factories import GetProjectInteractorFactory, CreateProjectInteractorFactory, \
    UpdateProjectInteractorFactory, DeleteProjectInteractorFactory, GetAllProjectsInteractorFactory, \
    GetBillInteractorFactory, GetTypeOfPaymentInteractorFactory, GetWorkedInteractorFactory, \
    GetTimestampInteractorFactory, GetTotalInteractorFactory, GetTaskInteractorFactory, CreateTaskInteractorFactory, \
    UpdateTaskInteractorFactory, DeleteTaskInteractorFactory, GetAllTasksInteractorFactory, GetWorkDayInteractorFactory, \
    CreateWorkDayInteractorFactory, UpdateWorkDayInteractorFactory, DeleteWorkDayInteractorFactory, \
    GetAllWorkDaysInteractorFactory, GetWorkTimeInteractorFactory, CreateWorkTimeInteractorFactory, \
    UpdateWorkTimeInteractorFactory, DeleteWorkTimeInteractorFactory, GetWorkTimeListInteractorFactory
from project.views import ProjectView, CreateProjectView, GetAllProjectsView, TotalView, CreateTaskView, \
            GetAllTasksView, UpdateProjectView, GetTaskView, UpdateTaskView, DeleteProjectView, DeleteTaskView, \
            CreateWorkDayView, CreateWorkTimeView, GetWorkDayView, GetWorkTimeView, UpdateWorkDayView, UpdateWorkTimeView, \
            DeleteWorkDayView, DeleteWorkTimeView, GetAllWorkDaysView, GetWorkTimeListView


# ------------------------ Project --------------------------------------------- #

def get_project_factory():
    get_project_interactor = GetProjectInteractorFactory.create()
    return ProjectView(get_project_interactor)


def create_project_factory():
    create_project_interactor = CreateProjectInteractorFactory.create()
    return CreateProjectView(create_project_interactor)


def update_project_factory():
    update_project_interactor = UpdateProjectInteractorFactory.create()
    return UpdateProjectView(update_project_interactor)


def delete_project_factory():
    delete_project_interactor = DeleteProjectInteractorFactory.create()
    return DeleteProjectView(delete_project_interactor)


def get_all_projects_factory():
    get_all_projects_interactor = GetAllProjectsInteractorFactory.create()
    return GetAllProjectsView(get_all_projects_interactor)


def get_total_factory(): # TODO change to one interactor
    get_type_of_payment_interactor = GetTypeOfPaymentInteractorFactory.create()
    get_timestampt_interactor = GetTimestampInteractorFactory.create()
    get_worked_interactor = GetWorkedInteractorFactory.create()
    get_total_interactor = GetTotalInteractorFactory.create()
    get_bill_interactor = GetBillInteractorFactory.create()
    return TotalView(get_type_of_payment_interactor, get_timestampt_interactor, get_worked_interactor, get_total_interactor, get_bill_interactor)


# --------------------------- Work Task ---------------------------------------- #

def get_task_factory():
    get_task_interactor = GetTaskInteractorFactory.create()
    return GetTaskView(get_task_interactor)


def create_task_factory():
    create_task_interactor = CreateTaskInteractorFactory.create()
    return CreateTaskView(create_task_interactor)


def update_task_factory():
    update_task_interactor = UpdateTaskInteractorFactory.create()
    return UpdateTaskView(update_task_interactor)


def delete_task_factory():
    delete_task_interactor = DeleteTaskInteractorFactory.create()
    return DeleteTaskView(delete_task_interactor)


def get_all_tasks_factory():
    get_all_tasks_interactor = GetAllTasksInteractorFactory.create()
    return GetAllTasksView(get_all_tasks_interactor)


# -------------------------- Work Day -------------------------------------------- #

def get_work_day_factory():
    get_work_day_interactor = GetWorkDayInteractorFactory.create()
    return GetWorkDayView(get_work_day_interactor)


def create_work_day_factory():
    create_work_day_interactor = CreateWorkDayInteractorFactory.create()
    return CreateWorkDayView(create_work_day_interactor)


def update_work_day_factory():
    update_work_day_interactor = UpdateWorkDayInteractorFactory.create()
    return UpdateWorkDayView(update_work_day_interactor)


def delete_work_day_factory():
    delete_work_day_interactor = DeleteWorkDayInteractorFactory.create()
    return DeleteWorkDayView(delete_work_day_interactor)


def get_all_work_days_factory():
    get_all_work_days_interactor = GetAllWorkDaysInteractorFactory.create()
    return GetAllWorkDaysView(get_all_work_days_interactor)


# ------------------------ Work Time ------------------------------------- #

def get_work_time_factory():
    get_work_time_interactor = GetWorkTimeInteractorFactory.create()
    return GetWorkTimeView(get_work_time_interactor)


def create_work_time_factory():
    create_work_time_interactor = CreateWorkTimeInteractorFactory.create()
    return CreateWorkTimeView(create_work_time_interactor)


def update_work_time_factory():
    update_work_time_interactor = UpdateWorkTimeInteractorFactory.create()
    return UpdateWorkTimeView(update_work_time_interactor)


def delete_work_time_factory():
    delete_work_time_interactor = DeleteWorkTimeInteractorFactory.create()
    return DeleteWorkTimeView(delete_work_time_interactor)


def get_work_time_list_factory():
    get_work_time_list_interactor = GetWorkTimeListInteractorFactory.create()
    return GetWorkTimeListView(get_work_time_list_interactor)
