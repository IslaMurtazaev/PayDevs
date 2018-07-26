import datetime

from django.test import TestCase

from account.entities import User
from account.models import UserORM
from account.repositories import UserRepo
from project.entities import Project
from project.interactors import GetProjectInteractor, CreateProjectInteractor, UpdateProjectInteractor
from project.models import ProjectORM
from project.repositories import ProjectRepo
from project.validators import UserPermissionValidator, ProjectDateTimeValidator
from PayDevs.exceptions import NoLoggedException, NoPermissionException, InvalidEntityException


class GetProjectInteractorTest(TestCase):
    def setUp(self):
        self.user = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'

        )
        self.project_orm = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        self.project_repo = ProjectRepo()
        self.user_permission_validator = UserPermissionValidator(UserRepo())

    def test_method_set_params_exclude(self):
        project_interactor = GetProjectInteractor(self.project_repo, self.user_permission_validator)

        project = project_interactor.set_params(
            project_id=self.project_orm.id, logged_id=self.user.id).execute()

        self.assertEqual(project.id, self.project_orm.id)
        self.assertEqual(project.title, self.project_orm.title)
        self.assertEqual(project.description, self.project_orm.description)
        self.assertEqual(project.type_of_payment, self.project_orm.type_of_payment)
        self.assertEqual(project.user_id, self.project_orm.user_id)

    def test_method_set_params_excude_exceptions(self):
        with self.assertRaises(NoLoggedException):
            GetProjectInteractor(self.project_repo, self.user_permission_validator).set_params(
                project_id=self.project_orm.id).execute()


class CreateProjectInteractorTest(TestCase):
    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'

        )
        self.project_orm = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_repo = ProjectRepo()
        self.user_permission_validator = UserPermissionValidator(UserRepo())
        self.project_date_validator = ProjectDateTimeValidator()
        self.project_interactor = CreateProjectInteractor(self.project_repo, self.user_permission_validator,
                                                     self.project_date_validator)

    def test_create_project_set_params_execute(self):
        project = self.project_interactor.set_params(logged_id=self.user_orm.id,
                                                title='Test Project',
                                                description='Description',
                                                type_of_payment='T_P',
                                                start_date='2018-12-20T12:30:00.000000Z+0600',
                                                status=True
                                                ).execute()
        project_orm = ProjectORM.objects.get(id=project.id)
        self.assertEqual(type(project), Project)
        self.assertEqual(project.title, project_orm.title)
        self.assertEqual(project.status, project_orm.status)
        self.assertEqual(project.type_of_payment, project_orm.type_of_payment)
        self.assertEqual(project.description, project_orm.description)
        self.assertEqual(project.start_date, project_orm.start_date)
        self.assertEqual(project.end_date, project_orm.end_date)

    def test_create_project_validate_interactors_type_of_payment(self):

        with self.assertRaises(InvalidEntityException):
            self.project_interactor.set_params(logged_id=self.user_orm.id,
                                          title='Test Project',
                                          description='Description',
                                          type_of_payment='HDDSASD',
                                          start_date='2018-12-20T12:30:00.000000Z+0600',
                                          status=True
                                          ).execute()


        try:
            self.project_interactor.set_params(logged_id=self.user_orm.id,
                                          title='Test Project',
                                          description='Description',
                                          type_of_payment='HDDSASD',
                                          start_date='2018-12-20T12:30:00.000000Z+0600',
                                          status=True
                                          ).execute()

        except InvalidEntityException as e:
            self.assertRegex(str(e), 'The type of payment must be only one of T_P, H_P and M_P')



    def test_create_project_validate_interactors_date_time(self):
        try:
            self.project_interactor.set_params(logged_id=self.user_orm.id,
                                          title='Test Project',
                                          description='Description',
                                          type_of_payment='H_P',
                                          start_date='2018-12-20T12:30:00',
                                          status=True
                                          ).execute()

        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Invalid datetime format')


    def test_create_project_validate_interactors_no_logged(self):

        with self.assertRaises(NoLoggedException):
            self.project_interactor.set_params(logged_id=None,
                                               title='Test Project',
                                               description='Description',
                                               type_of_payment='H_P',
                                               start_date='2018-12-20T12:30:00.000000Z+0600',
                                               status=True
                                               ).execute()

        try:
            self.project_interactor.set_params(logged_id=None,
                                          title='Test Project',
                                          description='Description',
                                          type_of_payment='H_P',
                                          start_date='2018-12-20T12:30:00.000000Z+0600',
                                          status=True
                                          ).execute()

        except NoLoggedException as e:
            print(e)
            self.assertRegex(str(e), 'Authentication required')




class UpdateProjectInteractorTest(TestCase):
    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'

        )
        self.project_orm = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_repo = ProjectRepo()
        self.user_permission_validator = UserPermissionValidator(UserRepo())
        self.project_date_validator = ProjectDateTimeValidator()
        self.project_update_interactor = UpdateProjectInteractor(self.project_repo,
                                                                 self.user_permission_validator,
                                                                 self.project_date_validator)


