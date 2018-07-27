import datetime

from django.test import TestCase

from PayDevs.constants import DATE_TIME_FORMAT
from account.models import UserORM
from account.repositories import UserRepo
from project.entities import Project
from project.interactors import GetProjectInteractor, CreateProjectInteractor, UpdateProjectInteractor, \
    DeleteProjectInteractor, GetAllProjectsInteractor, CreateMonthPaymentInteractor, GetMonthPaymentInteractor, \
    UpdateMonthPaymentInteractor, DeleteMonthPaymentInteractor, GetAllMonthPaymentsInteractor, GetWorkedDayInteractor, \
    CreateWorkedDayInteractor, UpdateWorkedDayInteractor, DeleteWorkedDayInteractor, GetAllWorkedDaysInteractor
from project.models import ProjectORM, MonthPaymentORM, WorkedDayORM
from project.repositories import ProjectRepo, MonthPaymentRepo, WorkedDayRepo
from project.validators import UserPermissionValidator, ProjectDateTimeValidator, RateValidator
from PayDevs.exceptions import NoLoggedException, NoPermissionException, InvalidEntityException, \
    EntityDoesNotExistException


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

    def test_method_set_params_exclude_exceptions(self):
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

        self.user_orm_2 = UserORM.objects.create_user(
            username='testUser2',
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

    def test_set_param_execute(self):
        project = self.project_update_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id,
            title="Update test",
            description="Test update project interactor",
            end_date="2018-12-20T12:30:00.000000Z+0600"
        ).execute()
        project_orm = ProjectORM.objects.get(id=self.project_orm.id)
        self.assertEquals(project.id, project_orm.id)
        self.assertEquals(project.type_of_payment, project_orm.type_of_payment)
        self.assertEquals(project.title, project_orm.title)
        self.assertEquals(project.description, project_orm.description)
        self.assertEquals(project.status, project_orm.status)
        self.assertEquals(project.end_date, project_orm.end_date)

        self.assertEquals(project_orm.title, "Update test")
        self.assertEquals(project_orm.description, "Test update project interactor")
        self.assertEquals(project_orm.end_date, datetime.datetime.strptime("2018-12-20T12:30:00.000000Z+0600",
                                                                           DATE_TIME_FORMAT))

    def test_set_param_execute_no_logged_exception(self):
        with self.assertRaises(NoLoggedException):
            self.project_update_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id,
                title="Update test",
                description="Test update project interactor",
                end_date="2018-12-20T12:30:00.000000Z+0600"
            ).execute()

    def test_set_param_execute_permission_exception(self):
        with self.assertRaises(NoPermissionException):
            self.project_update_interactor.set_params(
                logged_id=self.user_orm_2.id,
                project_id=self.project_orm.id,
                title="Update test",
                description="Test update project interactor",
                end_date="2018-12-20T12:30:00.000000Z+0600"
            ).execute()

    def test_set_param_execute_no_project_exception(self):
        with self.assertRaises(EntityDoesNotExistException):
            self.project_update_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=None,
                title="Update test",
                description="Test update project interactor",
                end_date="2018-12-20T12:30:00.000000Z+0600"
            ).execute()


class DeleteProjectInteractorTest(TestCase):
    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'

        )

        self.user_orm_2 = UserORM.objects.create_user(
            username='testUser2',
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
        self.project_update_interactor = DeleteProjectInteractor(self.project_repo,
                                                                 self.user_permission_validator)

    def test_set_params_execute(self):
        deleted_project = self.project_update_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id
        ).execute()

        with self.assertRaises(ProjectORM.DoesNotExist):
            ProjectORM.objects.get(id=self.project_orm.id)

    def test_delete_project_no_permission_exception(self):
        with self.assertRaises(NoPermissionException):
            deleted_project = self.project_update_interactor.set_params(
                logged_id=self.user_orm_2.id,
                project_id=self.project_orm.id
            ).execute()

    def test_delete_project_no_logged_exception(self):
        with self.assertRaises(NoLoggedException):
            deleted_project = self.project_update_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id
            ).execute()

    def test_delete_project_entity_not_found_exception(self):
        with self.assertRaises(EntityDoesNotExistException):
            deleted_project = self.project_update_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=None
            ).execute()


class GetAllProjectsInteractorTest(TestCase):
    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'

        )

        for i in range(10):
            ProjectORM.objects.create(
                title='Test Project',
                description='My Test project',
                type_of_payment='M_P',
                start_date=datetime.datetime.now() - datetime.timedelta(days=30),
                end_date=datetime.datetime.now(),
                user_id=self.user_orm.id
            )

        # self.project_orm = ProjectORM.objects.create(
        #     title='Test Project',
        #     description='My Test project',
        #     type_of_payment='M_P',
        #     start_date=datetime.datetime.now() - datetime.timedelta(days=30),
        #     end_date=datetime.datetime.now(),
        #     user_id=self.user_orm.id
        # )

        self.project_repo = ProjectRepo()
        self.user_permission_validator = UserPermissionValidator(UserRepo())
        self.project_update_interactor = GetAllProjectsInteractor(self.project_repo,
                                                                  self.user_permission_validator)




    def test_set_params_execute(self):

        projects = self.project_update_interactor.set_params(
            logged_id=self.user_orm.id,
        ).execute()
        self.assertEqual(type(projects), list)
        self.assertEqual(len(projects), 10)
        self.assertEquals(type(projects.pop()), Project)


    def test_set_params_execute_no_logged_exception(self):
        with self.assertRaises(NoLoggedException):
            projects = self.project_update_interactor.set_params(
                logged_id=None,
            ).execute()


# --------------------------- Month Payment Tests -------------------------------- #

class CreateMonthPaymentInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.project_orm = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.month_payment_orm = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=100
        )

        self.project_repo = ProjectRepo()
        self.month_payment_repo = MonthPaymentRepo()
        permission_validator = UserPermissionValidator(UserRepo())
        rate_validator = RateValidator()
        self.month_payment_interactor = CreateMonthPaymentInteractor(self.month_payment_repo, self.project_repo,
                                                                     permission_validator, rate_validator)

    def test_method_set_params(self):
        created_month_payment = self.month_payment_interactor.set_params(
            project_id=self.project_orm.id,
            rate=110,
            logged_id=self.user_orm.id
        ).execute()
        created_month_payment_orm = MonthPaymentORM.objects.get(id=created_month_payment.id)

        self.assertEqual(created_month_payment.id, created_month_payment_orm.id)
        self.assertEqual(created_month_payment.project_id, created_month_payment_orm.project_id)
        self.assertEqual(created_month_payment.rate, 110)


    def test_method_set_params_no_logged_exception(self):

        with self.assertRaises(NoLoggedException):
            self.month_payment_interactor.set_params(
                project_id=self.project_orm.id,
                rate=self.month_payment_orm.rate,
                logged_id=None
            ).execute()


    def test_method_set_params_no_permission_exception(self):

        with self.assertRaises(NoPermissionException):
            self.month_payment_interactor.set_params(
                project_id=self.project_orm.id,
                rate=self.month_payment_orm.rate,
                logged_id=self.user_orm.id+10
            ).execute()


    def test_method_set_params_entity_does_not_exist_exception(self):

        with self.assertRaises(EntityDoesNotExistException):
            self.month_payment_interactor.set_params(
                project_id=self.project_orm.id+10,
                rate=self.month_payment_orm.rate,
                logged_id=self.user_orm.id
            ).execute()


    def test_method_rate_validator_invalid_entity_exception(self):

        with self.assertRaises(InvalidEntityException):
            self.month_payment_interactor.set_params(
                project_id=self.project_orm.id,
                rate="Wrong type",
                logged_id=self.user_orm.id
            ).execute()

        with self.assertRaises(InvalidEntityException):
            self.month_payment_interactor.set_params(
                project_id=self.project_orm.id,
                rate=-10,
                logged_id=self.user_orm.id
            ).execute()



class GetMonthPaymentInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.project_orm = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.month_payment_orm = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=100
        )

        self.month_payment_repo = MonthPaymentRepo()
        permission_validator = UserPermissionValidator(UserRepo)
        self.month_payment_interactor = GetMonthPaymentInteractor(self.month_payment_repo, permission_validator)


    def test_method_set_params(self):
        month_payment = self.month_payment_interactor.set_params(
            month_payment_id=self.month_payment_orm.id,
            logged_id=self.user_orm.id
        ).execute()

        self.assertEqual(month_payment.id, self.month_payment_orm.id)
        self.assertEqual(month_payment.project_id, self.project_orm.id)
        self.assertEqual(month_payment.rate, self.month_payment_orm.rate)


    def test_method_set_params_no_logged_exception(self):

        with self.assertRaises(NoLoggedException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                logged_id=None
            ).execute()


    def test_method_set_params_entity_does_not_exist_exception(self):

        with self.assertRaises(EntityDoesNotExistException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id+10,
                logged_id=self.user_orm.id
            ).execute()



class UpdateMonthPaymentInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.project_orm = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.month_payment_orm = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=100
        )

        self.project_repo = ProjectRepo()
        self.month_payment_repo = MonthPaymentRepo()
        permission_validator = UserPermissionValidator(UserRepo())
        rate_validator = RateValidator()
        self.month_payment_interactor = UpdateMonthPaymentInteractor(self.month_payment_repo, self.project_repo,
                                                                     permission_validator, rate_validator)

    def test_method_set_params(self):
        updated_month_payment = self.month_payment_interactor.set_params(
            month_payment_id=self.month_payment_orm.id,
            project_id=self.project_orm.id,
            rate=130,
            logged_id=self.user_orm.id
        ).execute()

        self.assertEqual(updated_month_payment.id, self.month_payment_orm.id)
        self.assertEqual(updated_month_payment.project_id, self.project_orm.id)
        self.assertEqual(updated_month_payment.rate, 130)


    def test_method_set_params_no_logged_exception(self):

        with self.assertRaises(NoLoggedException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                rate=self.month_payment_orm.rate,
                logged_id=None
            ).execute()


    def test_method_set_params_no_permission_exception(self):

        with self.assertRaises(NoPermissionException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                rate=self.month_payment_orm.rate,
                logged_id=self.user_orm.id+10
            ).execute()


    def test_method_set_params_entity_does_not_exist_exception(self):

        with self.assertRaises(EntityDoesNotExistException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id+10,
                rate=self.month_payment_orm.rate,
                logged_id=self.user_orm.id
            ).execute()


    def test_method_rate_validator_invalid_entity_exception(self):

        with self.assertRaises(InvalidEntityException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                rate="Wrong type",
                logged_id=self.user_orm.id
            ).execute()

        with self.assertRaises(InvalidEntityException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                rate=-10,
                logged_id=self.user_orm.id
            ).execute()



class DeleteMonthPaymentInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.project_orm = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.month_payment_orm = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=100
        )

        self.project_repo = ProjectRepo()
        self.month_payment_repo = MonthPaymentRepo()
        permission_validator = UserPermissionValidator(UserRepo())
        self.month_payment_interactor = DeleteMonthPaymentInteractor(self.month_payment_repo, self.project_repo,
                                                                     permission_validator)

    def test_method_set_params(self):
        deleted_month_payment = self.month_payment_interactor.set_params(
            month_payment_id=self.month_payment_orm.id,
            project_id=self.project_orm.id,
            logged_id=self.user_orm.id
        ).execute()

        self.assertEqual(deleted_month_payment.id, self.month_payment_orm.id)
        self.assertEqual(deleted_month_payment.project_id, self.project_orm.id)
        self.assertEqual(deleted_month_payment.rate, self.month_payment_orm.rate)


    def test_method_set_params_no_logged_exception(self):
        with self.assertRaises(NoLoggedException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                logged_id=None
            ).execute()


    def test_method_set_params_no_permission_exception(self):
        with self.assertRaises(NoPermissionException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                logged_id=self.user_orm.id + 10
            ).execute()


    def test_method_set_params_entity_does_not_exist_exception(self):
        with self.assertRaises(EntityDoesNotExistException):
            self.month_payment_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id + 10,
                logged_id=self.user_orm.id
            ).execute()



class GetAllMonthPaymentsInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.project_orm = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.project_orm = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=100
        )

        self.month_payment_repo = MonthPaymentRepo()
        permission_validator = UserPermissionValidator(UserRepo)
        self.month_payment_interactor = GetAllMonthPaymentsInteractor(self.month_payment_repo, permission_validator)


    def test_method_set_params(self):
        month_payments = self.month_payment_interactor.set_params(
            project_id=self.project_orm.id,
            logged_id=self.user_orm.id
        ).execute()

        self.assertTrue(isinstance(month_payments, list))
        self.assertEqual(month_payments[0].project_id, self.project_orm.id)
        self.assertEqual(month_payments[0].rate, self.project_orm.rate)


    def test_method_set_params_no_logged_exception(self):

        with self.assertRaises(NoLoggedException):
            self.month_payment_interactor.set_params(
                project_id=self.project_orm.id,
                logged_id=None
            ).execute()
