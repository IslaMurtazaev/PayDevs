from PayDevs.interactors import Interactor


#------------------------ Project ---------------------------------------------#
from project.entities import Project, WorkTask, HourPayment


class GetProjectInteractor(Interactor):

    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, project_id, logged_id=None, **kwargs):
        self.logged_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.validate_user_project.validate_pemission(self.logged_id)
        return self.project_repo.get(logged_id=self.logged_id, project_id=self.project_id)



class CreateProjectInteractor(Interactor):

    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, title, description, type_of_payment, rate, **kwargs):
        self.logged_id = logged_id
        self.title = title
        self.description = description
        self.type_of_payment = type_of_payment
        self.rate = rate
        return self
    
    def execute(self):
        self.validate_user_project.validate_pemission(self.logged_id)
        project = Project(user_id=self.logged_id, title=self.title,
                          description=self.description,
                          type_of_payment=self.type_of_payment)
        return self.project_repo.create(project)




class UpdateProjectInteractor(Interactor):

    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, title, description, start_date,
                   end_date, type_of_payment, status, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.type_of_payment = type_of_payment
        self.status = status
        return self

    def execute(self):
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_pemission(self.user_id, project.user_id)
        title = self.title if self.title is not None else project.title
        description = self.description if self.description is not None else project.description
        start_date = self.start_date if self.start_date is not None else project.start_date
        end_date = self.end_date if self.end_date is not None else project.end_date
        type_of_payment = self.type_of_payment if self.type_of_payment is not None else project.type_of_payment
        status = self.status if self.status else project.status
        update_project = Project(
            id=project.id,
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            type_of_payment=type_of_payment,
            status=status
        )
        return self.project_repo.update(update_project)



class DeleteProjectInteractor(Interactor):

    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self, *args, **kwargs):
        project = self.project_repo.get(project_id=self.project_repo)
        self.validate_user_project.validate_pemission(self.user_id, project.user_id)
        return self.project_repo.delete(project.id)




class GetAllProjectsInteractor(Interactor):

    def __init__(self, project_repo, validate_user_project):
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, **kwargs):
        self.user_id = logged_id
        return self

    def execute(self):
        self.validate_user_project.validate_pemission(self.user_id)
        return self.project_repo.get_all(self.user_id)



class ProjectGetTotalInteractor(Interactor):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def set_params(self, logged_id, project_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        project = self.project_repo.get(self.project_id)
        return project.total



#--------------------------- Work Task ----------------------------------------#



class GetTaskInteractor(Interactor):

    def __init__(self, work_task_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, task_id,  **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.task_id = task_id
        return self

    def execute(self):
        self.validate_user_project.validate_pemission(self.user_id)
        work_task = self.work_task_repo.get(self.task_id)
        self.validate_user_project.validate_pemission(self.project_id, work_task.project_id)
        return work_task




class CreateTaskInteractor(Interactor):

    def __init__(self, work_task_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, title, description, price, paid, completed,**kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.price = price
        self.paid = paid
        self.completed = completed
        return self

    def execute(self):
        self.validate_user_project.validate_pemission(self.user_id)
        work_task = WorkTask(
            project_id=self.project_id,
            title=self.title,
            description=self.description,
            price=self.price,
            paid=self.paid,
            completed=self.completed
        )

        return self.work_task_repo.create(work_task)





class UpdateTaskInteractor(Interactor):

    def __init__(self, work_task_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, task_id, title, description, price, compledted, paid, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.task_id = task_id
        self.title = title
        self.description = description
        self.price = price
        self.completed = compledted
        self.paid = paid
        return self

    def execute(self):
        self.validate_user_project.validate_pemission(self.user_id)
        work_task = self.work_task_repo.get(self.task_id)
        self.validate_user_project.validate_pemission(self.project_id, work_task.project_id)
        title = self.title if self.title is not None else work_task.title
        description = self.description if self.description is not None else work_task.description
        price = self.price if self.price is not None else work_task.price
        completed = self.completed if self.completed is not None else work_task.completed
        paid = self.paid if self.paid is not None else work_task.paid
        update_work_task = WorkTask(
            title=title,
            description=description,
            price=price,
            completed=completed,
            paid=paid
        )

        return self.work_task_repo.update(update_work_task)



class DeleteTaskInteractor(Interactor):

    def __init__(self, work_task_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, task_id,*args, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        self.task_id = task_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_pemission(self.user_id)
        work_task = self.work_task_repo.get(self.task_id)
        self.validate_user_project.validate_pemission(self.project_id, work_task.project_id)
        return self.work_task_repo.delete(work_task.id)



class GetAllTasksInteractor(Interactor):

    def __init__(self, work_task_repo, validate_user_project):
        self.work_task_repo = work_task_repo
        self.validate_user_project = validate_user_project

    def set_params(self, logged_id, project_id, **kwargs):
        self.user_id = logged_id
        self.project_id = project_id
        return self

    def execute(self):
        self.validate_user_project.validate_pemission(self.user_id)
        return self.work_task_repo.get_all(self.project_id)



class GetHourPaymentInteractor(Interactor):


    def __init__(self, hour_payment_repo, validate_user_project):
        self.hour_payment_repo = hour_payment_repo
        self.hour_payment_repo = self.validate_user_project = validate_user_project



    def set_params(self, hour_payment_id, project_id, logged_id, **kwargs):
        self.hour_payment_id = hour_payment_id
        self.project_id = project_id
        self.user_id = logged_id
        return self

    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_pemission(logged_id=self.user_id)
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        self.validate_user_project.validate_pemission(hour_payment.project_id, self.project_id)
        return hour_payment



class CreateHourPaymentInteractor(Interactor):

    def __init__(self, hour_payment_repo, validate_user_project):
        self.hour_payment_repo = hour_payment_repo
        self.hour_payment_repo = self.validate_user_project = validate_user_project



    def execute(self, project_id, rate, logged_id, *args, **kwargs):
        self.project_id = project_id
        self.rate = rate
        self.user_id = logged_id
        return self

    def set_params(self, *args, **kwargs):
        self.validate_user_project.validate_pemission(logged_id=self.user_id)
        hour_payment = HourPayment(
            project_id=self.project_id,
            rate=self.rate
        )
        return self.hour_payment_repo.create(hour_payment)



class UpdateHourPaymentInteractor(Interactor):

    def __init__(self, hour_payment_repo, project_repo, validate_user_project):
        self.hour_payment_repo = hour_payment_repo
        self.project_repo = project_repo
        self.validate_user_project = validate_user_project


    def set_params(self, hour_payment_id, rate, project_id, logged_id, **kwargs):
        self.hour_payment_id = hour_payment_id
        self.rate = rate
        self.project_id = project_id
        self.user_id = logged_id
        return self


    def execute(self, *args, **kwargs):

        self._validate(self.user_id)
        hour_payment = self.hour_payment_repo.get(self.hour_payment_id)
        self.validate_user_project.validate_pemission(self.project_id, hour_payment.project_id)
        rate = self.rate if self.rate is not None else hour_payment.rate
        update_hour_payment = HourPayment(
            id=hour_payment.id,
            rate=rate,
            project_id=hour_payment.project_id
        )
        return self.hour_payment_repo.update(update_hour_payment)


    def _validate(self, logged_id):
        self.validate_user_project.validate_pemission(logged_id=logged_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_pemission(project.user_id, self.user_id)



class DeleteHourPaymentInteractor(Interactor):

    def __init__(self, hour_payment_repo, project_repo, validate_user_project):
        self.hour_payment_repo = hour_payment_repo
        self.validate_user_project = validate_user_project
        self.project_repo = project_repo


    def set_params(self, hour_payment_id, project_id, logged_id, *args, **kwargs):
        self.hour_payment_id = hour_payment_id,
        self.project_id = project_id
        self.user_id = logged_id
        return self


    def execute(self, *args, **kwargs):
        self.validate_user_project.validate_pemission(logged_id=self.user_id)
        project = self.project_repo.get(self.project_id)
        self.validate_user_project.validate_pemission(project.user_id, self.user_id)
