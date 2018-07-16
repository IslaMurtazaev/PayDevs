from project.entities import Project, WorkTask
from project.models import ProjectORM, HourPaymentORM, MonthPaymentORM, WorkTaskORM
from PayDevs.exceptions import EntityDoesNotExistException, InvalidEntityException


#------------------------ Project --------------------------------------------#

class ProjectRepo(object):

    def get_project(self, user, id=None, title=None):
        try:
            if id:
                db_project = user.projectorm_set.get(id=id)
            else:
                db_project = user.projectorm_set.get(title=title)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_project(db_project)



    def create_project(self, user, title, description, type_of_payment, rate):
        try:
            db_project = ProjectORM(title=title, description=description, user=user,
                                    type_of_payment=type_of_payment)
            db_project.save()
            self._set_rate(db_project, type_of_payment, rate)
        except:
            raise InvalidEntityException(source='repositories', code='could not save',
                                         message="Unable to create such project")

        return self._decode_db_project(db_project)



    def get_all_projects(self, user):
        try:
            db_projects = user.projectorm_set.all()
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException
        else:
            projects = [self._decode_db_project(db_project) for db_project in db_projects]
            return projects



    def update_project(self, user, project_id, new_attrs):
        try:
            db_project = user.projectorm_set.get(id=project_id)
            print(new_attrs)
            for key in new_attrs.keys():
                if new_attrs[key] is not None:
                    db_project.__dict__[key] = new_attrs[key]
            db_project.save()
        except ProjectORM.DoesNotExist:
            raise InvalidEntityException(source='repositories', code='not allowed',
                                         message="Unable to update project with provided attrs")
        return self._decode_db_project(db_project)



    def get_total(self, user, title):
        try:
            db_project = ProjectORM.objects.get(user=user, title=title)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException

        if (db_project.type_of_payment.lower() == 'h_p'):
            raise NotImplementedError
        elif (db_project.type_of_payment.lower() == 'm_p'):
            raise NotImplementedError
        else:
            return self._get_tasks_total(db_project)



    def _get_tasks_total(self, db_project):
        try:
            tasks = db_project.worktaskorm_set.all()
            total = 0
            for task in tasks:
                if (task.completed and not task.paid):
                    total += task.price
        except:
            raise InvalidEntityException(source='repositories', code='could not sum total',
                                         message="'%s' task attribute is invalid" % task.title)
        return total



    def _decode_db_project(self, db_project):
        fileds = {
            'id': db_project.id,
            'user': str(db_project.user),
            'title': db_project.title,
            'description': db_project.description,
            'start_date': str(db_project.start_date),
            'end_date': str(db_project.end_date),
            'type_of_payment': db_project.type_of_payment,
            'status': db_project.status
        }

        return Project(**fileds)


    def _set_rate(self, db_project, type_of_payment, rate):
        if (db_project.type_of_payment.lower() == 'h_p'):
            HourPaymentORM(project=db_project, rate=rate).save()
        elif (db_project.type_of_payment.lower() == 'm_p'):
            MonthPaymentORM(project=db_project, rate=rate).save()


#-------------------------- Work Task ----------------------------------------#

class WorkTaskRepo(object):

    def create_work_task(self, project, title, description, price):
        try:
            db_work_task = WorkTaskORM(project=project, title=title, description=description, price=price)
            db_work_task.save()
        except:
            raise InvalidEntityException(source='repositories', code='could not save',
                                         message="Unable to create such task")
        else:
            return self._decode_db_work_task(db_work_task)



    def get_all_tasks(self, project):
        try:
            db_work_tasks = project.worktaskorm_set.all()
        except:
            raise InvalidEntityException(source='repositories', code='could not find',
                                         message="Unable to find tasks in specified project")
        else:
            return [self._decode_db_work_task(db_task) for db_task in db_work_tasks]



    def _decode_db_work_task(self, db_work_task):
        fields = {
            'id': db_work_task.id,
            'project': str(db_work_task.project),
            'title': db_work_task.title,
            'description': db_work_task.description,
            'price': db_work_task.price,
            'completed': db_work_task.completed,
            'paid': db_work_task.paid
        }

        return WorkTask(**fields)
