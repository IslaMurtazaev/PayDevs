import datetime

from django.test import TestCase

from account.entities import User
from account.repositories import UserRepo
from project.entities import Project
from project.interactors import GetProjectInteractor, CreateProjectInteractor
from project.repositories import ProjectRepo
from project.validators import UserPermissionValidator
from PayDevs.exceptions import NoLoggedException, NoPermissionException


class GetProjectInteractorTest(TestCase):

    def setUp(self):
        user = User(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'

        )
        self.user = UserRepo().create_user(user)
        project = Project(
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now(),
            user_id=self.user.id
        )

        self.project = ProjectRepo().create(project)


    def test_method_set_params_exclude(self):
        project = GetProjectInteractor(project_repo=ProjectRepo(),
                                       user_permission_validator=UserPermissionValidator(UserRepo())).set_params(
            project_id=self.project.id, logged_id=self.user.id).execute()

        self.assertEqual(project.id, self.project.id)
        self.assertEqual(project.title, self.project.title)
        self.assertEqual(project.description, self.project.description)
        self.assertEqual(project.type_of_payment, self.project.type_of_payment)
        self.assertEqual(project.user_id, self.project.user_id)


    def test_method_set_params_excude_exceptions(self):
        with self.assertRaises(NoLoggedException):
            GetProjectInteractor(project_repo=ProjectRepo(),
                                 user_permission_validator=UserPermissionValidator(UserRepo())).set_params(
                project_id=self.project.id).execute()



class CreateProjectInteractorTest(TestCase):

    def setUp(self):
        user = User(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'

        )
        self.user = UserRepo().create_user(user)

    # def test_method_set_params_exclude(self):
    #     project = CreateProjectInteractor(project_repo=ProjectRepo(),
    #                                    validate_user_project=UserPermissionsValidator(UserRepo())).set_params(
    #         logged_id=self.user.id,
    #         title="Test",
    #         description="Description testr",
    #         type_of_payment='T_P',
    #         rate=500).execute()

# class GetProjectInteractorTest(TestCase):
#
#     def setUp(self):
#         user = User(
#             username='testUser',
#             email='test_user@mail.com',
#             password='qwert12345'
#
#         )
#         self.user = UserRepo().create_user(user)
#         project = Project(
#             title='Test Project',
#             description='My Test project',
#             type_of_payment='M_P',
#             start_date=datetime.datetime.now(),
#             user_id=self.user.id
#         )
#
#         self.project = ProjectRepo().create(project)
#
#
#     def test_method_set_params_exclude(self):
#         project = GetProjectInteractor(project_repo=ProjectRepo(),
#                                        validate_user_project=UserPermissionsValidator(UserRepo())).set_params(
#             project_id=self.project.id, logged_id=self.user.id).execute()
#
#         self.assertEqual(project.id, self.project.id)
#         self.assertEqual(project.title, self.project.title)
#         self.assertEqual(project.description, self.project.description)
#         self.assertEqual(project.type_of_payment, self.project.type_of_payment)
#         self.assertEqual(project.user_id, self.project.user_id)
#
#
#     def test_method_set_params_excude_exceptions(self):
#         with self.assertRaises(NoLoggedException):
#             GetProjectInteractor(project_repo=ProjectRepo(),
#                                            validate_user_project=UserPermissionsValidator(UserRepo())).set_params(
#                 project_id=self.project.id).execute()
#
#
#
# class CreateProjectInteractorTest(TestCase):
#
#     def setUp(self):
#         user = User(
#             username='testUser',
#             email='test_user@mail.com',
#             password='qwert12345'
#
#         )
#         self.user = UserRepo().create_user(user)
#
#     def test_method_set_params_exclude(self):
#         project = CreateProjectInteractor(project_repo=ProjectRepo(),
#                                        validate_user_project=UserPermissionsValidator(UserRepo())).set_params(
#             logged_id=self.user.id,
#             title="Test",
#             description="Description testr",
#             type_of_payment='T_P',
#             rate=500).execute()

