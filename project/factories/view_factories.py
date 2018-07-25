from project.factories.interactor_factories import CreateProjectInteractorFactory, GetProjectInteractorFactory, \
    DeleteProjectInteractorFactory, UpdateProjectInteractorFactory, GetAllProjectsInteractorFactory, \
    CreateTaskInteractorFactory, GetTaskInteractorFactory, UpdateTaskInteractorFactory, DeleteTaskInteractorFactory, \
    GetAllTasksInteractorFactory, GetAllMonthPaymentsInteractorFactory, CreateMonthPaymentInteractorFactory, \
    GetMonthPaymentInteractorFactory, UpdateMonthPaymentInteractorFactory, DeleteMonthPaymentInteractorFactory, \
    CreateHourPaymentInteractorFactory, GetHourPaymentInteractorFactory, UpdateHourPaymentInteractorFactory, \
    DeleteHourPaymentInteractorFactory, GetAllHourPaymentInteractorFactory, CreateWorkTimeInteractorFactory, \
    GetWorkTimeInteractorFactory, UpdateWorkTimeInteractorFactory, DeleteWorkTimeInteractorFactory, \
    GetAllWorkTimeInteractorFactory, CreateWorkedDayInteractorFactory, GetWorkedDayInteractorFactory, \
    UpdateWorkedDayInteractorFactory, DeleteWorkedDayInteractorFactory, GetAllWorkedDaysInteractorFactory
from project.views import ProjectView, GetAllProjectsView, TaskView, GetAllTasksView, MonthPaymentView, \
    GetAllMonthPaymentsView, HourPaymentView, GetAllHourPaymentView, WorkTimeView, GetWorkTimeListView, WorkedDayView, \
    GetAllWorkedDaysView


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
    get_all_tasks_interactor = GetAllTasksInteractorFactory.create()
    return GetAllTasksView(get_all_tasks_interactor)



def create_month_payment_factory():
    create_month_payment_interactor = CreateMonthPaymentInteractorFactory.create()
    return MonthPaymentView(create_month_payment_interactor)


def get_month_payment_factory():
    get_month_payment_interactor = GetMonthPaymentInteractorFactory.create()
    return MonthPaymentView(get_month_payment_interactor)


def update_month_payment_factory():
    update_month_payment_interactor = UpdateMonthPaymentInteractorFactory.create()
    return MonthPaymentView(update_month_payment_interactor)


def delete_month_payment_factory():
    delete_month_payment_interactor = DeleteMonthPaymentInteractorFactory.create()
    return MonthPaymentView(delete_month_payment_interactor)


def get_all_month_payments_factory():
    get_all_month_payments_interactor = GetAllMonthPaymentsInteractorFactory.create()
    return GetAllMonthPaymentsView(get_all_month_payments_interactor)



def create_worked_day_factory():
    create_worked_day_interactor = CreateWorkedDayInteractorFactory.create()
    return WorkedDayView(create_worked_day_interactor)


def get_worked_day_factory():
    get_worked_day_interactor = GetWorkedDayInteractorFactory.create()
    return WorkedDayView(get_worked_day_interactor)


def update_worked_day_factory():
    update_worked_day_interactor = UpdateWorkedDayInteractorFactory.create()
    return WorkedDayView(update_worked_day_interactor)


def delete_worked_day_factory():
    delete_worked_day_interactor = DeleteWorkedDayInteractorFactory.create()
    return WorkedDayView(delete_worked_day_interactor)


def get_all_worked_days_factory():
    get_all_worked_days_interactor = GetAllWorkedDaysInteractorFactory.create()
    return GetAllWorkedDaysView(get_all_worked_days_interactor)




def create_hour_payment_factory():
    get_hour_payment_interactor = CreateHourPaymentInteractorFactory().create()
    return HourPaymentView(get_hour_payment_interactor)


def get_hour_payment_factory():
    get_hour_payment_interactor = GetHourPaymentInteractorFactory().create()
    return HourPaymentView(get_hour_payment_interactor)


def update_hour_payment_factory():
    get_hour_payment_interactor = UpdateHourPaymentInteractorFactory().create()
    return HourPaymentView(get_hour_payment_interactor)


def delete_hour_payment_factory():
    get_hour_payment_interactor = DeleteHourPaymentInteractorFactory().create()
    return HourPaymentView(get_hour_payment_interactor)



def get_all_hour_payment_factory():
    get_hour_payment_interactor = GetAllHourPaymentInteractorFactory().create()
    return GetAllHourPaymentView(get_hour_payment_interactor)



def create_work_time_factory():
    get_work_time_interactor = CreateWorkTimeInteractorFactory().create()
    return WorkTimeView(get_work_time_interactor)


def get_work_time_factory():
    get_work_time_interactor = GetWorkTimeInteractorFactory().create()
    return WorkTimeView(get_work_time_interactor)


def update_work_time_factory():
    get_work_time_interactor = UpdateWorkTimeInteractorFactory().create()
    return WorkTimeView(get_work_time_interactor)


def get_all_work_time_factory():
    get_work_time_interactor = GetAllWorkTimeInteractorFactory().create()
    return GetWorkTimeListView(get_work_time_interactor)


def delete_work_time_factory():
    get_work_time_interactor = DeleteWorkTimeInteractorFactory().create()
    return WorkTimeView(get_work_time_interactor)
