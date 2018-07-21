from PayDevs.interactors import Interactor
from project.entities import Project


# ------------------------ Project --------------------------------------------- #

class GetProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.title = kwargs.get('title')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self):
        return self.project_repo.get(user_id=self.user_id, title=self.title, project_id=self.project_id)



class CreateProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.type_of_payment = kwargs.get('type_of_payment')
        self.rate = kwargs.get('rate')
        return self

    def execute(self):
        return self.project_repo.create(user_id=self.user_id, title=self.title, description=self.description,
                                                type_of_payment=self.type_of_payment, rate=self.rate)




class UpdateProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')

        self.project_new_attrs = {
            'title': kwargs.get('title'),
            'description': kwargs.get('description'),
            'start_date': kwargs.get('start_date'),
            'end_date': kwargs.get('end_date'),
            'type_of_payment': kwargs.get('type_of_payment'),
            'status': kwargs.get('status')
        }
        return self

    def execute(self):
        return self.project_repo.update(user_id=self.user_id, project_id=self.project_id,
                                        new_attrs=self.project_new_attrs)



class DeleteProjectInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self, *args, **kwargs):
        return self.project_repo.delete(self.user_id, self.project_id)




class GetAllProjectsInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        return self

    def execute(self):
        return self.project_repo.get_all(self.user_id)




class GetTypeOfPaymentInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self):
        return self.project_repo.get_type_of_payment(self.user_id, self.project_id)



class GetWorkedInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, type_of_payment, **kwargs):
        self.project_id = kwargs.get('project_id')
        self.type_of_payment = type_of_payment
        self.start_date_boundary = kwargs.get('start_date')
        self.end_date_boundary = kwargs.get('end_date')
        return self

    def execute(self):
        return self.project_repo.get_worked(self.project_id, self.type_of_payment, self.start_date_boundary,
                                            self.end_date_boundary)



class GetTotalInteractor(Interactor):

    def set_params(self, type_of_payment, worked, **kwargs):
        self.type_of_payment = type_of_payment
        self.worked = worked
        return self

    def execute(self):
        return Project.get_total(self.type_of_payment, self.worked)


# --------------------------- Work Task ---------------------------------------- #


class GetTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.task_id = kwargs.get('task_id')
        self.title = kwargs.get('title')
        return self

    def execute(self):
        return self.work_task_repo.get(user_id=self.user_id, project_id=self.project_id,
                                       task_id=self.task_id, title=self.title)




class CreateTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.price = kwargs.get('price')
        return self

    def execute(self):
        return self.work_task_repo.create(user_id=self.user_id, project_id=self.project_id, title=self.title,
                                                    description=self.description, price=self.price)





class UpdateTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.task_id = kwargs.get('task_id')
        self.new_attrs = {
            'title': kwargs.get('title'),
            'description': kwargs.get('description'),
            'price': kwargs.get('price'),
            'completed': kwargs.get('completed'),
            'paid': kwargs.get('paid')
        }
        return self

    def execute(self):
        return self.work_task_repo.update(user_id=self.user_id, project_id=self.project_id, task_id=self.task_id,
                                          new_attrs=self.new_attrs)



class DeleteTaskInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.task_id = kwargs.get('task_id')
        return self

    def execute(self, *args, **kwargs):
        return self.work_task_repo.delete(user_id=self.user_id, project_id=self.project_id, task_id=self.task_id)



class GetAllTasksInteractor(Interactor):

    def __init__(self, work_task_repo):
        self.work_task_repo = work_task_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self):
        return self.work_task_repo.get_all(user_id=self.user_id, project_id=self.project_id)


# -------------------------- Work Day ------------------------------------ #

class GetWorkDayInteractor(Interactor):

    def __init__(self, work_day_repo):
        self.work_day_repo = work_day_repo

    def set_params(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.month_payment_id = kwargs.get('month_payment_id')
        self.work_day_id = kwargs.get('work_day_id')
        return self

    def execute(self):
        return self.work_day_repo.get(user_id=self.user_id, project_id=self.project_id,
                                      month_payment_id=self.month_payment_id, work_day_id=self.work_day_id)



class CreateWorkDayInteractor(Interactor):

    def __init__(self, work_day_repo):
        self.work_day_repo = work_day_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.month_payment_id = kwargs.get('month_payment_id')
        self.day = kwargs.get('day')
        return self

    def execute(self):
        return self.work_day_repo.create(user_id=self.user_id, project_id=self.project_id,
                                         month_payment_id=self.month_payment_id, day=self.day)



class UpdateWorkDayInteractor(Interactor):

    def __init__(self, work_day_repo):
        self.work_day_repo = work_day_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.month_payment_id = kwargs.get('month_payment_id')
        self.work_day_id = kwargs.get('work_day_id')
        self.new_attrs = {
            'day': kwargs.get('day'),
            'paid': kwargs.get('paid')
        }
        return self

    def execute(self):
        return self.work_day_repo.update(user_id=self.user_id, project_id=self.project_id, work_day_id=self.work_day_id,
                                         month_payment_id=self.month_payment_id, new_attrs=self.new_attrs)



class DeleteWorkDayInteractor(Interactor):

    def __init__(self, work_day_repo):
        self.work_day_repo = work_day_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.month_payment_id = kwargs.get('month_payment_id')
        self.work_day_id = kwargs.get('work_day_id')
        return self

    def execute(self):
        return self.work_day_repo.delete(user_id=self.user_id, project_id=self.project_id, work_day_id=self.work_day_id,
                                         month_payment_id=self.month_payment_id)



class GetAllWorkDaysInteractor(Interactor):

    def __init__(self, work_day_repo):
        self.work_day_repo = work_day_repo

    def set_params(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self):
        return self.work_day_repo.get_all(user_id=self.user_id, project_id=self.project_id)

# ------------------------------- Work Time ------------------------------------ #

class GetWorkTimeInteractor(Interactor):

    def __init__(self, work_time_repo):
        self.work_time_repo = work_time_repo

    def set_params(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.hour_payment_id = kwargs.get('hour_payment_id')
        self.work_time_id = kwargs.get('work_time_id')
        return self

    def execute(self):
        return self.work_time_repo.get(user_id=self.user_id, project_id=self.project_id,
                                       hour_payment_id=self.hour_payment_id, work_time_id=self.work_time_id)



class CreateWorkTimeInteractor(Interactor):

    def __init__(self, work_time_repo):
        self.work_time_repo = work_time_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.hour_payment_id = kwargs.get('hour_payment_id')
        self.start_work = kwargs.get('start_work')
        self.end_work = kwargs.get('end_work')
        return self

    def execute(self):
        return self.work_time_repo.create(user_id=self.user_id, project_id=self.project_id,
                                          hour_payment_id=self.hour_payment_id, start_work=self.start_work,
                                          end_work=self.end_work)



class UpdateWorkTimeInteractor(Interactor):

    def __init__(self, work_time_repo):
        self.work_time_repo = work_time_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.hour_payment_id = kwargs.get('hour_payment_id')
        self.work_time_id = kwargs.get('work_time_id')
        self.new_attrs = {
            'start_work': kwargs.get('start_work'),
            'end_work': kwargs.get('end_work'),
            'paid': kwargs.get('paid')
        }
        return self

    def execute(self):
        return self.work_time_repo.update(user_id=self.user_id, project_id=self.project_id, work_time_id=self.work_time_id,
                                          hour_payment_id=self.hour_payment_id, new_attrs=self.new_attrs)




class DeleteWorkTimeInteractor(Interactor):

    def __init__(self, work_time_repo):
        self.work_time_repo = work_time_repo

    def set_params(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        self.hour_payment_id = kwargs.get('hour_payment_id')
        self.work_time_id = kwargs.get('work_time_id')
        return self

    def execute(self):
        return self.work_time_repo.delete(user_id=self.user_id, project_id=self.project_id, work_time_id=self.work_time_id,
                                          hour_payment_id=self.hour_payment_id)




class GetWorkTimeListInteractor(Interactor):

    def __init__(self, work_time_repo):
        self.work_time_repo = work_time_repo

    def set_params(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.project_id = kwargs.get('project_id')
        return self

    def execute(self):
        return self.work_time_repo.get_all(user_id=self.user_id, project_id=self.project_id)
