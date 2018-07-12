from project.models import ProjectORM
from project.entities import Project
from PayDevs.exceptions import EntityDoesNotExistException, InvalidEntityException


class ProjectRepo(object):
    
    def get_project(self, id=None, title=None):
        try:
            if id:
                db_project = ProjectORM.objects.get(id=id)
            else:
                db_project = ProjectORM.objects.get(title=title)
        except ProjectORM.DoesNotExist:
            raise EntityDoesNotExistException

        return self._decode_db_project(db_project)


    def create_project(self, title, description, user, type_of_payment):
        try:
            db_project = ProjectORM(title=title, description=description, user=user,\
                                    type_of_payment=type_of_payment)
            db_project.save()
        except:
            raise InvalidEntityException(source='repositories', code='could not save',\
                                          message="Unable to create such project")

        return self._decode_db_project(db_project)
        

        
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

    