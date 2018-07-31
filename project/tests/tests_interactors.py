import datetime

from django.test import TestCase
from pytz import UTC

from PayDevs.constants import DATE_TIME_FORMAT
from account.models import UserORM
from account.repositories import UserRepo
from project.entities import Project, HourPayment, WorkTime, WorkTask
from project.interactors import GetProjectInteractor, CreateProjectInteractor, UpdateProjectInteractor, \
    DeleteProjectInteractor, GetAllProjectsInteractor, GetHourPaymentInteractor, CreateHourPaymentInteractor, \
    UpdateHourPaymentInteractor, DeleteHourPaymentInteractor, GetAllHourPaymentInteractor, GetWorkTimeInteractor, \
    CreateWorkTimeInteractor, UpdateWorkTimeInteractor, DeleteWorkTimeInteractor, GetAllWorkTimeInteractor, \
    GetTaskInteractor, CreateTaskInteractor, UpdateTaskInteractor, DeleteTaskInteractor, GetAllTasksInteractor, \
    CreateMonthPaymentInteractor, GetMonthPaymentInteractor, UpdateMonthPaymentInteractor, DeleteMonthPaymentInteractor, \
    GetAllMonthPaymentsInteractor, GetWorkedDayInteractor, CreateWorkedDayInteractor, UpdateWorkedDayInteractor, \
    DeleteWorkedDayInteractor, GetAllWorkedDaysInteractor, ProjectGetTotalInteractor

from project.models import ProjectORM, HourPaymentORM, WorkTimeORM, MonthPaymentORM, WorkedDayORM, WorkTaskORM
from project.repositories import ProjectRepo, HourPaymentRepo, WorkTimeRepo, MonthPaymentRepo, WorkedDayRepo, WorkTaskRepo
from project.validators import PermissionValidator, FieldValidator
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
        self.user_permission_validator = PermissionValidator(UserRepo())

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
        self.user_permission_validator = PermissionValidator(UserRepo())
        self.field_validator = FieldValidator()
        self.project_interactor = CreateProjectInteractor(self.project_repo, self.user_permission_validator,
                                                          self.field_validator)

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
        self.user_permission_validator = PermissionValidator(UserRepo())
        self.field_validator = FieldValidator()
        self.project_update_interactor = UpdateProjectInteractor(self.project_repo,
                                                                 self.user_permission_validator,
                                                                 self.field_validator)

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
        self.user_permission_validator = PermissionValidator(UserRepo())
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
        self.project_repo = ProjectRepo()
        self.user_permission_validator = PermissionValidator(UserRepo())
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
        permission_validator = PermissionValidator(UserRepo())
        field_validator = FieldValidator()
        self.month_payment_interactor = CreateMonthPaymentInteractor(self.month_payment_repo, self.project_repo,
                                                                     permission_validator, field_validator)

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
        permission_validator = PermissionValidator(UserRepo)
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
        permission_validator = PermissionValidator(UserRepo())
        field_validator = FieldValidator()
        self.month_payment_interactor = UpdateMonthPaymentInteractor(self.month_payment_repo, self.project_repo,
                                                                     permission_validator, field_validator)

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

        month_payment_repo = MonthPaymentRepo()
        permission_validator = PermissionValidator(UserRepo())
        self.month_payment_interactor = DeleteMonthPaymentInteractor(month_payment_repo, permission_validator)

    def test_method_set_params(self):
        deleted_month_payment = self.month_payment_interactor.set_params(
            month_payment_id=self.month_payment_orm.id,
            logged_id=self.user_orm.id
        ).execute()

        self.assertEqual(deleted_month_payment.id, self.month_payment_orm.id)
        self.assertEqual(deleted_month_payment.project_id, self.project_orm.id)
        self.assertEqual(deleted_month_payment.rate, self.month_payment_orm.rate)


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
        permission_validator = PermissionValidator(UserRepo)
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



class CreateWorkedDayInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.user_orm2 = UserORM.objects.create_user(
            username='testUser2',
            email='test_user2@mail.com',
            password='qwert12345'
        )
        self.project_orm = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.project_orm2 = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project2',
            description='Without any rights',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.month_payment_orm = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=100
        )
        self.month_payment_orm2 = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=80
        )
        self.worked_day_orm = WorkedDayORM.objects.create(
            month_payment_id=self.month_payment_orm.id,
            day=datetime.datetime.today().date(),
            paid=False
        )

        self.project_repo = ProjectRepo()
        self.month_payment_repo = MonthPaymentRepo()
        self.worked_day_repo = WorkedDayRepo()
        permission_validator = PermissionValidator(UserRepo())
        field_validator = FieldValidator()
        self.worked_day_interactor = CreateWorkedDayInteractor(self.worked_day_repo, self.month_payment_repo,
                                                               self.project_repo, permission_validator,
                                                               field_validator)

    def test_method_set_params(self):
        created_worked_day = self.worked_day_interactor.set_params(
            month_payment_id=self.month_payment_orm.id,
            project_id=self.project_orm.id,
            day="1999-08-02",
            paid=True,
            logged_id=self.user_orm.id
        ).execute()
        created_worked_day_orm = WorkedDayORM.objects.get(id=created_worked_day.id)

        self.assertEqual(created_worked_day.id, created_worked_day_orm.id)
        self.assertEqual(created_worked_day.month_payment_id, created_worked_day_orm.month_payment_id)
        self.assertEqual(created_worked_day.paid, created_worked_day_orm.paid)
        self.assertEqual(created_worked_day.day, "1999-08-02")


    def test_method_set_params_no_logged_exception(self):

        with self.assertRaises(NoLoggedException):
            self.worked_day_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018-09-01",
                paid=True,
                logged_id=None
            ).execute()


    def test_method_set_params_no_permission_exception(self):

        with self.assertRaises(NoPermissionException):
            self.worked_day_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018-09-01",
                paid=True,
                logged_id=self.user_orm2.id
            ).execute()

        with self.assertRaises(NoPermissionException):
            self.worked_day_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm2.id,
                day="2018-09-01",
                paid=True,
                logged_id=self.user_orm.id
            ).execute()


    def test_method_set_params_entity_does_not_exist_exception(self):

        with self.assertRaises(EntityDoesNotExistException):
            self.worked_day_interactor.set_params(
                month_payment_id=self.month_payment_orm.id+10,
                project_id=self.project_orm.id,
                day="2018-09-01",
                paid=True,
                logged_id=self.user_orm.id
            ).execute()


    def test_method_date_validator_invalid_entity_exception(self):

        with self.assertRaises(InvalidEntityException):
            self.worked_day_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018-09-00",
                paid=True,
                logged_id=self.user_orm.id
            ).execute()

        with self.assertRaises(InvalidEntityException):
            self.worked_day_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018 09 01",
                paid=True,
                logged_id=self.user_orm.id
            ).execute()



class GetWorkedDayInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.user_orm2 = UserORM.objects.create_user(
            username='testUser2',
            email='test_user2@mail.com',
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
        self.worked_day_orm = WorkedDayORM.objects.create(
            month_payment_id=self.month_payment_orm.id,
            day=datetime.datetime.today().date(),
            paid=False
        )

        self.worked_day_repo = WorkedDayRepo()
        permission_validator = PermissionValidator(UserRepo())
        self.worked_day_interactor = GetWorkedDayInteractor(self.worked_day_repo, permission_validator)


    def test_interactor_methods(self):
        worked_day = self.worked_day_interactor.set_params(
            worked_day_id=self.worked_day_orm.id,
            logged_id=self.user_orm.id
        ).execute()

        self.assertEqual(worked_day.id, self.worked_day_orm.id)
        self.assertEqual(worked_day.month_payment_id, self.month_payment_orm.id)
        self.assertEqual(worked_day.day, self.worked_day_orm.day)

        worked_day = self.worked_day_interactor.set_params(
            worked_day_id=self.worked_day_orm.id,
            logged_id=self.user_orm2.id
        ).execute()

        self.assertEqual(worked_day.id, self.worked_day_orm.id)
        self.assertEqual(worked_day.month_payment_id, self.month_payment_orm.id)
        self.assertEqual(worked_day.day, self.worked_day_orm.day)


    def test_interactor_methods_no_logged_exception(self):

        with self.assertRaises(NoLoggedException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id,
                logged_id=None
            ).execute()


    def test_interactor_methods_entity_does_not_exist_exception(self):

        with self.assertRaises(EntityDoesNotExistException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id+10,
                logged_id=self.user_orm.id
            ).execute()



class UpdateWorkedDayInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.user_orm2 = UserORM.objects.create_user(
            username='testUser2',
            email='test_user2@mail.com',
            password='qwert12345'
        )
        self.project_orm = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.project_orm2 = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project2',
            description='Without any rights',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.month_payment_orm = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=100
        )
        self.month_payment_orm2 = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=80
        )
        self.worked_day_orm = WorkedDayORM.objects.create(
            month_payment_id=self.month_payment_orm.id,
            day=datetime.datetime.today().date(),
            paid=False
        )
        self.worked_day_orm2 = WorkedDayORM.objects.create(
            month_payment_id=self.month_payment_orm2.id,
            day=datetime.datetime.today().date(),
            paid=False
        )

        project_repo = ProjectRepo()
        month_payment_repo = MonthPaymentRepo()
        worked_day_repo = WorkedDayRepo()
        permission_validator = PermissionValidator(UserRepo())
        date_validator = FieldValidator()
        self.worked_day_interactor = UpdateWorkedDayInteractor(worked_day_repo, month_payment_repo,
                                                               project_repo, permission_validator,
                                                               date_validator)

    def test_method_set_params(self):
        updated_worked_day = self.worked_day_interactor.set_params(
            worked_day_id = self.worked_day_orm.id,
            month_payment_id=self.month_payment_orm.id,
            project_id=self.project_orm.id,
            day="2018-06-18",
            logged_id=self.user_orm.id
        ).execute()

        self.assertEqual(updated_worked_day.id, self.worked_day_orm.id)
        self.assertEqual(updated_worked_day.month_payment_id, self.month_payment_orm.id)
        self.assertEqual(updated_worked_day.day.date(), datetime.date(2018, 6, 18))


    def test_method_set_params_no_logged_exception(self):

        with self.assertRaises(NoLoggedException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id,
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018-06-18",
                logged_id=None
            ).execute()


    def test_method_set_params_no_permission_exception(self):

        with self.assertRaises(NoPermissionException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id,
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018-06-18",
                logged_id=self.user_orm2.id
            ).execute()

        with self.assertRaises(NoPermissionException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id,
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm2.id,
                day="2018-06-18",
                logged_id=self.user_orm.id
            ).execute()

        with self.assertRaises(NoPermissionException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id,
                month_payment_id=self.month_payment_orm2.id,
                project_id=self.project_orm.id,
                day="2018-06-18",
                logged_id=self.user_orm.id
            ).execute()

        with self.assertRaises(NoPermissionException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm2.id,
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018-06-18",
                logged_id=self.user_orm.id
            ).execute()

    def test_method_set_params_entity_does_not_exist_exception(self):

        with self.assertRaises(EntityDoesNotExistException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id+10,
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018-06-18",
                logged_id=self.user_orm.id
            ).execute()


    def test_method_date_validator_invalid_entity_exception(self):

        with self.assertRaises(InvalidEntityException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id,
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018 06 18",
                logged_id=self.user_orm.id
            ).execute()

        with self.assertRaises(InvalidEntityException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id,
                month_payment_id=self.month_payment_orm.id,
                project_id=self.project_orm.id,
                day="2018-06-18T12:00:00",
                logged_id=self.user_orm.id
            ).execute()



class DeleteWorkedDayInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.user_orm2 = UserORM.objects.create_user(
            username='testUser2',
            email='test_user2@mail.com',
            password='qwert12345'
        )
        self.project_orm = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.project_orm2 = ProjectORM.objects.create(
            user_id=self.user_orm.id,
            title='Test Project2',
            description='Without any rights',
            type_of_payment='M_P',
            start_date=datetime.datetime.now()
        )
        self.month_payment_orm = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=100
        )
        self.month_payment_orm2 = MonthPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=80
        )
        self.worked_day_orm = WorkedDayORM.objects.create(
            month_payment_id=self.month_payment_orm.id,
            day=datetime.date(2018, 6, 18),
            paid=False
        )
        self.worked_day_orm2 = WorkedDayORM.objects.create(
            month_payment_id=self.month_payment_orm2.id,
            day=datetime.datetime.today().date(),
            paid=False
        )


        worked_day_repo = WorkedDayRepo()
        permission_validator = PermissionValidator(UserRepo())
        self.worked_day_interactor = DeleteWorkedDayInteractor(worked_day_repo, permission_validator)

    def test_method_set_params(self):
        deleted_worked_day = self.worked_day_interactor.set_params(
            worked_day_id=self.worked_day_orm.id,
            logged_id=self.user_orm.id
        ).execute()

        self.assertEqual(deleted_worked_day.id, self.worked_day_orm.id)
        self.assertEqual(deleted_worked_day.month_payment_id, self.month_payment_orm.id)
        self.assertEqual(deleted_worked_day.day, datetime.date(2018, 6, 18))


    def test_method_set_params_no_logged_exception(self):

        with self.assertRaises(NoLoggedException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id,
                logged_id=None
            ).execute()


    def test_method_set_params_entity_does_not_exist_exception(self):

        with self.assertRaises(EntityDoesNotExistException):
            self.worked_day_interactor.set_params(
                worked_day_id=self.worked_day_orm.id+10,
                logged_id=self.user_orm.id
            ).execute()



class GetAllWorkedDaysInteractorTest(TestCase):

    def setUp(self):
        self.user_orm = UserORM.objects.create_user(
            username='testUser',
            email='test_user@mail.com',
            password='qwert12345'
        )
        self.user_orm2 = UserORM.objects.create_user(
            username='testUser2',
            email='test_user2@mail.com',
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
        self.worked_day_orm = WorkedDayORM.objects.create(
            month_payment_id=self.month_payment_orm.id,
            day=datetime.datetime.today().date(),
            paid=False
        )

        worked_day_repo = WorkedDayRepo()
        month_payment_repo = MonthPaymentRepo()
        permission_validator = PermissionValidator(UserRepo())
        self.worked_day_interactor = GetAllWorkedDaysInteractor(worked_day_repo, month_payment_repo,
                                                                permission_validator)

    def test_interactor_methods(self):
        worked_days = self.worked_day_interactor.set_params(
            month_payment_id=self.month_payment_orm.id,
            logged_id=self.user_orm.id
        ).execute()

        self.assertTrue(isinstance(worked_days, list))
        self.assertEqual(worked_days[0].id, self.worked_day_orm.id)
        self.assertEqual(worked_days[0].month_payment_id, self.month_payment_orm.id)
        self.assertEqual(worked_days[0].day, self.worked_day_orm.day)

        worked_days = self.worked_day_interactor.set_params(
            month_payment_id=self.month_payment_orm.id,
            logged_id=self.user_orm2.id
        ).execute()

        self.assertTrue(isinstance(worked_days, list))
        self.assertEqual(worked_days[0].id, self.worked_day_orm.id)
        self.assertEqual(worked_days[0].month_payment_id, self.month_payment_orm.id)
        self.assertEqual(worked_days[0].day, self.worked_day_orm.day)

    def test_interactor_methods_no_logged_exception(self):
        with self.assertRaises(NoLoggedException):
            self.worked_day_interactor.set_params(
                month_payment_id=self.month_payment_orm.id,
                logged_id=None
            ).execute()

    def test_interactor_methods_entity_does_not_exist_exception(self):
        with self.assertRaises(EntityDoesNotExistException):
            self.worked_day_interactor.set_params(
                month_payment_id=self.month_payment_orm.id + 10,
                logged_id=self.user_orm.id
            ).execute()



class GetHourPaymentInteractorTest(TestCase):
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

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        hour_payment_repo = HourPaymentRepo()
        user_project_validate = PermissionValidator(UserRepo())
        self.get_hour_payment_interactor = GetHourPaymentInteractor(hour_payment_repo, user_project_validate)

    def test_set_params_execute(self):
        hour_payment = self.get_hour_payment_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id,
            hour_payment_id=self.hour_payment_orm.id

        ).execute()

        self.assertEqual(hour_payment.id, self.hour_payment_orm.id),
        self.assertEqual(hour_payment.rate, self.hour_payment_orm.rate)
        self.assertEqual(hour_payment.rate, 500)

    def test_execute_entity_not_found_exception(self):
        with self.assertRaises(EntityDoesNotExistException):
            self.get_hour_payment_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm.id,
                hour_payment_id=None

            ).execute()

    def test_execute_entity_no_logged_exception(self):
        with self.assertRaises(NoLoggedException):
            self.get_hour_payment_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id

            ).execute()


class CreateHourPaymentInteractorTest(TestCase):
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
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm2 = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        hour_payment_repo = HourPaymentRepo()
        user_project_validate = PermissionValidator(UserRepo())
        project_repo = ProjectRepo()
        field_validator = FieldValidator()
        self.create_hour_payment_interactor = CreateHourPaymentInteractor(hour_payment_repo,
                                                                          project_repo,
                                                                          user_project_validate,
                                                                          field_validator)

    def test_set_params_execute(self):
        create_hour_paymnet = self.create_hour_payment_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id,
            rate=700

        ).execute()
        hour_payment_orm = HourPaymentORM.objects.get(id=create_hour_paymnet.id)
        self.assertEquals(create_hour_paymnet.id, hour_payment_orm.id)
        self.assertEquals(create_hour_paymnet.rate, hour_payment_orm.rate)
        self.assertEquals(700, hour_payment_orm.rate)

    def test_set_params_execute_validate_type_of_payment(self):
        with self.assertRaises(InvalidEntityException):
            self.create_hour_payment_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm2.id,
                rate=700

            ).execute()

        try:
            self.create_hour_payment_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm2.id,
                rate=700

            ).execute()
        except InvalidEntityException as e:
            self.assertRegex(str(e), 'The type of payment for the project must be H_P')

    def test_set_params_execute_validate(self):
        project_orm = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm_2.id
        )
        with self.assertRaises(NoPermissionException):
            self.create_hour_payment_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=project_orm.id,
                rate=700

            ).execute()


class UpdateHourPaymentInteractorTest(TestCase):
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
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm2 = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        hour_payment_repo = HourPaymentRepo()
        user_project_validate = PermissionValidator(UserRepo())
        project_repo = ProjectRepo()
        rate_validator = FieldValidator()
        self.update_hour_payment_interactor = UpdateHourPaymentInteractor(hour_payment_repo,
                                                                          project_repo,
                                                                          user_project_validate,
                                                                          rate_validator
                                                                          )

    def test_set_params_execute(self):
        updated_hour_payment = self.update_hour_payment_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id,
            hour_payment_id=self.hour_payment_orm.id,
            rate=1000
        ).execute()
        updated_hour_payment_orm = HourPaymentORM.objects.get(id=self.hour_payment_orm.id)
        self.assertEqual(updated_hour_payment.id, self.hour_payment_orm.id)
        self.assertEqual(updated_hour_payment.rate, 1000)
        self.assertEqual(updated_hour_payment_orm.rate, 1000)

    def test_set_params_execute_not_found(self):
        with self.assertRaises(EntityDoesNotExistException):
            self.update_hour_payment_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm.id,
                hour_payment_id=None,
                rate=1000
            ).execute()

    def test_set_params_execute_no_permission(self):
        with self.assertRaises(NoPermissionException):
            self.update_hour_payment_interactor.set_params(
                logged_id=self.user_orm_2.id,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                rate=1000
            ).execute()

    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.update_hour_payment_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                rate=1000
            ).execute()

    def test_set_params_execute_no_permission_project_id(self):
        with self.assertRaises(NoPermissionException):
            self.update_hour_payment_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm2.id,
                hour_payment_id=self.hour_payment_orm.id,
                rate=1000
            ).execute()


class DeleteHourPaymentInteractorTest(TestCase):
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
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm2 = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        hour_payment_repo = HourPaymentRepo()
        user_project_validate = PermissionValidator(UserRepo())
        self.delete_hour_payment_interactor = DeleteHourPaymentInteractor(hour_payment_repo, user_project_validate)

    def test_set_params_execute(self):
        deleted_hour_payment = self.delete_hour_payment_interactor.set_params(
            logged_id=self.user_orm.id,
            hour_payment_id=self.hour_payment_orm.id
        ).execute()
        self.assertEqual(deleted_hour_payment.id, self.hour_payment_orm.id)
        with self.assertRaises(HourPaymentORM.DoesNotExist):
            HourPaymentORM.objects.get(id=self.hour_payment_orm.id)

    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.delete_hour_payment_interactor.set_params(
                logged_id=None,
                hour_payment_id=self.hour_payment_orm.id
            ).execute()



class GetAllHourPaymentInteractorTest(TestCase):
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
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm2 = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        hour_payment_repo = HourPaymentRepo()
        user_project_validate = PermissionValidator(UserRepo())
        self.get_all_hour_payment_interactor = GetAllHourPaymentInteractor(hour_payment_repo, user_project_validate)

    def test_set_params_execute(self):
        for i in range(10):
            HourPaymentORM.objects.create(
                project_id=self.project_orm2.id,
                rate=500
            )
        hour_payments = self.get_all_hour_payment_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm2.id
        ).execute()

        self.assertEqual(type(hour_payments), list)
        self.assertEqual(len(hour_payments), 10)
        self.assertEqual(type(hour_payments.pop()), HourPayment)
        self.assertEqual(hour_payments.pop().project_id, self.project_orm2.id)

    def test_set_params_execute_no_logged(self):
        for i in range(10):
            HourPaymentORM.objects.create(
                project_id=self.project_orm2.id,
                rate=500
            )
        with self.assertRaises(NoLoggedException):
            self.get_all_hour_payment_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm2.id
            ).execute()


class GetWorkTimeInteractorTest(TestCase):
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
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm2 = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        self.work_time_orm = WorkTimeORM.objects.create(
            hour_payment_id=self.hour_payment_orm.id,
            paid=False,
            start_work=datetime.datetime.now() - datetime.timedelta(hours=5),
            end_work=datetime.datetime.now()
        )

        work_time_repo = WorkTimeRepo()
        user_project_validate = PermissionValidator(UserRepo())
        self.get_work_time_interactor = GetWorkTimeInteractor(work_time_repo, user_project_validate)

    def test_set_params_execute(self):
        work_time = self.get_work_time_interactor.set_params(
            logged_id=self.user_orm.id,
            work_time_id=self.work_time_orm.id
        ).execute()

        self.assertEqual(work_time.id, self.work_time_orm.id)

        self.assertEqual(work_time.start_work, self.work_time_orm.start_work.replace(tzinfo=UTC))
        self.assertEqual(work_time.end_work, self.work_time_orm.end_work.replace(tzinfo=UTC))
        self.assertEqual(work_time.paid, self.work_time_orm.paid)
        self.assertEqual(work_time.paid, False)

    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.get_work_time_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                work_time_id=self.work_time_orm.id
            ).execute()



    def test_set_params_execute_entity_not_found(self):
        with self.assertRaises(EntityDoesNotExistException):
            self.get_work_time_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                work_time_id=self.work_time_orm.id + 5000
            ).execute()


class CreateWorkTimeInteractorTest(TestCase):
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
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm2 = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        self.hour_payment_orm2 = HourPaymentORM.objects.create(
            project_id=self.project_orm2.id,
            rate=500
        )

        work_time_repo = WorkTimeRepo()
        hour_payment_repo = HourPaymentRepo()
        user_project_validate = PermissionValidator(UserRepo())
        project_date_validate = FieldValidator()
        self.create_work_time_interactor = CreateWorkTimeInteractor(work_time_repo, hour_payment_repo,
                                                                    user_project_validate, project_date_validate)

    def test_set_params_execute(self):
        created_work_time = self.create_work_time_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id,
            hour_payment_id=self.hour_payment_orm.id,
            start_work="2018-9-20T10:00:00.000000Z+0600",
            end_work="2018-9-20T18:30:00.000000Z+0600",
            paid=True
        ).execute()

        work_time_orm = WorkTimeORM.objects.get(id=created_work_time.id)

        self.assertEqual(work_time_orm.id, created_work_time.id)
        self.assertEqual(work_time_orm.paid, created_work_time.paid)
        self.assertEqual(work_time_orm.start_work, created_work_time.start_work)
        self.assertEqual(work_time_orm.end_work, created_work_time.end_work)
        self.assertEqual(work_time_orm.hour_payment.id, created_work_time.hour_payment_id)

    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.create_work_time_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                start_work="2018-9-20T10:00:00.000000Z+0600",
                end_work="2018-9-20T18:30:00.000000Z+0600",
                paid=True
            ).execute()

    def test_set_params_execute_no_permission(self):
        with self.assertRaises(NoPermissionException):
            self.create_work_time_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm2.id,
                start_work="2018-9-20T10:00:00.000000Z+0600",
                end_work="2018-9-20T18:30:00.000000Z+0600",
                paid=True
            ).execute()

    def test_set_params_execute_no_date_validate(self):
        with self.assertRaises(InvalidEntityException):
            self.create_work_time_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                start_work="2018-9-20T107",
                end_work="2018-9-20T18:30:00.000000Z+0600",
                paid=True
            ).execute()

        try:
            self.create_work_time_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                start_work="2018-9-20T18:30:00.000000Z+0600",
                end_work="2018-9-20T107",
                paid=True
            ).execute()

        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Invalid datetime format')


class UpdateWorkTimeInteractorTest(TestCase):
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
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm2 = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        self.hour_payment_orm2 = HourPaymentORM.objects.create(
            project_id=self.project_orm2.id,
            rate=500
        )

        self.work_time_orm = WorkTimeORM.objects.create(
            hour_payment=self.hour_payment_orm,
            start_work=datetime.datetime.now().replace(hour=10),
            end_work=datetime.datetime.now().replace(hour=19),
            paid=False
        )

        self.work_time_orm2 = WorkTimeORM.objects.create(
            hour_payment=self.hour_payment_orm2,
            start_work=datetime.datetime.now().replace(hour=9),
            end_work=datetime.datetime.now().replace(hour=18),
            paid=True
        )

        work_time_repo = WorkTimeRepo()
        hour_payment_repo = HourPaymentRepo()
        user_project_validate = PermissionValidator(UserRepo())
        project_date_validate = FieldValidator()
        project_repo = ProjectRepo()
        self.update_work_time_interactor = UpdateWorkTimeInteractor(work_time_repo, project_repo, hour_payment_repo,
                                                                    user_project_validate, project_date_validate)

    def test_set_params_execute(self):
        update_work_time = self.update_work_time_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id,
            hour_payment_id=self.hour_payment_orm.id,
            work_time_id=self.work_time_orm.id,
            start_work="2018-9-20T18:30:00.000000Z+0600",
            paid=True
        ).execute()

        self.assertEqual(type(update_work_time), WorkTime)
        self.assertEqual(update_work_time.start_work,
                         datetime.datetime.strptime("2018-9-20T18:30:00.000000Z+0600", DATE_TIME_FORMAT).
                         replace(tzinfo=datetime.timezone(datetime.timedelta(0, 21600))))

        update_work_time_orm = WorkTimeORM.objects.get(id=update_work_time.id)
        self.assertEqual(update_work_time_orm.paid, True)
        self.assertEqual(update_work_time_orm.start_work,
                         datetime.datetime.strptime("2018-9-20T18:30:00.000000Z+0600", DATE_TIME_FORMAT).
                         replace(tzinfo=datetime.timezone(datetime.timedelta(0, 21600))))
        self.assertNotEqual(update_work_time_orm.start_work, self.work_time_orm.start_work)
        self.assertNotEqual(update_work_time_orm.paid, self.work_time_orm.paid)
        self.assertEqual(update_work_time_orm.end_work, self.work_time_orm.end_work.replace(tzinfo=UTC))

    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.update_work_time_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                work_time_id=self.work_time_orm.id,
                start_work="2018-9-20T18:30:00.000000Z+0600",
                paid=True
            ).execute()

    def test_set_params_execute_no_permission_user(self):
        with self.assertRaises(NoPermissionException):
            self.update_work_time_interactor.set_params(
                logged_id=self.user_orm_2.id,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                work_time_id=self.work_time_orm.id,
                start_work="2018-9-20T18:30:00.000000Z+0600",
                paid=True
            ).execute()

    def test_set_params_execute_no_logged_project_id(self):
        with self.assertRaises(NoPermissionException):
            self.update_work_time_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm2.id,
                hour_payment_id=self.hour_payment_orm.id,
                work_time_id=self.work_time_orm.id,
                start_work="2018-9-20T18:30:00.000000Z+0600",
                paid=True
            ).execute()

    def test_set_params_execute_no_permission_hour_payment_id(self):
        with self.assertRaises(NoPermissionException):
            self.update_work_time_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm2.id,
                work_time_id=self.work_time_orm.id,
                start_work="2018-9-20T18:30:00.000000Z+0600",
                paid=True
            ).execute()

    def test_set_params_execute_entity_not_found(self):
        with self.assertRaises(EntityDoesNotExistException):
            self.update_work_time_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm.id,
                hour_payment_id=self.hour_payment_orm.id,
                work_time_id=None,
                start_work="2018-9-20T18:30:00.000000Z+0600",
                paid=True
            ).execute()


class DeleteWorkTimeInteractorTest(TestCase):
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
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm2 = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        self.hour_payment_orm2 = HourPaymentORM.objects.create(
            project_id=self.project_orm2.id,
            rate=500
        )

        self.work_time_orm = WorkTimeORM.objects.create(
            hour_payment=self.hour_payment_orm,
            start_work=datetime.datetime.now().replace(hour=10),
            end_work=datetime.datetime.now().replace(hour=19),
            paid=False
        )

        self.work_time_orm2 = WorkTimeORM.objects.create(
            hour_payment=self.hour_payment_orm2,
            start_work=datetime.datetime.now().replace(hour=9),
            end_work=datetime.datetime.now().replace(hour=18),
            paid=True
        )

        work_time_repo = WorkTimeRepo()
        user_project_validate = PermissionValidator(UserRepo())
        self.delete_work_time_interactor = DeleteWorkTimeInteractor(work_time_repo, user_project_validate)

    def test_set_params_execute(self):
        deleted_work_time = self.delete_work_time_interactor.set_params(
            logged_id=self.user_orm.id,
            hour_payment_id=self.hour_payment_orm.id,
            work_time_id=self.work_time_orm.id

        ).execute()

        self.assertEqual(type(deleted_work_time), WorkTime)

        with self.assertRaises(WorkTimeORM.DoesNotExist):
            WorkTimeORM.objects.get(id=self.work_time_orm.id)

        with self.assertRaises(WorkTimeORM.DoesNotExist):
            WorkTimeORM.objects.get(id=deleted_work_time.id)

    def test_set_params_execute_no_logged_exception(self):
        with self.assertRaises(NoLoggedException):
            self.delete_work_time_interactor.set_params(
                logged_id=None,
                hour_payment_id=self.hour_payment_orm.id,
                work_time_id=self.work_time_orm.id
            ).execute()


class GetAllWorkTimeInteractorTest(TestCase):
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
            type_of_payment='H_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm2 = ProjectORM.objects.create(
            title='Test Project Month Payment',
            description='My Test project',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.hour_payment_orm = HourPaymentORM.objects.create(
            project_id=self.project_orm.id,
            rate=500
        )

        self.hour_payment_orm2 = HourPaymentORM.objects.create(
            project_id=self.project_orm2.id,
            rate=500
        )


        work_time_repo = WorkTimeRepo()
        user_project_validate = PermissionValidator(UserRepo())
        self.get_all_work_time_interactor = GetAllWorkTimeInteractor(work_time_repo, user_project_validate)


    def test_set_params_execute(self):
        for i in range(10):
            WorkTimeORM.objects.create(
                hour_payment=self.hour_payment_orm,
                start_work=datetime.datetime.now().replace(hour=10) - datetime.timedelta(days=i),
                end_work=datetime.datetime.now().replace(hour=19) - datetime.timedelta(days=i),
                paid=False
            )
        work_times = self.get_all_work_time_interactor.set_params(
            logged_id=self.user_orm.id,
            hour_payment_id=self.hour_payment_orm.id
        ).execute()

        self.assertEqual(type(work_times), list)
        self.assertEqual(len(work_times), 10)
        self.assertEqual(type(work_times.pop()), WorkTime)
        self.assertEqual(work_times.pop().hour_payment_id, self.hour_payment_orm.id)


    def test_set_params_execute_no_logged(self):
        for i in range(10):
            WorkTimeORM.objects.create(
                hour_payment=self.hour_payment_orm,
                start_work=datetime.datetime.now().replace(hour=10) - datetime.timedelta(days=i),
                end_work=datetime.datetime.now().replace(hour=19) - datetime.timedelta(days=i),
                paid=False
            )

        with self.assertRaises(NoLoggedException):
            self.get_all_work_time_interactor.set_params(
                logged_id=None,
                hour_payment_id=self.hour_payment_orm.id
            ).execute()


class GetTaskInteractorTest(TestCase):

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

        self.work_task_orm = WorkTaskORM.objects.create(
            project_id=self.project_orm.id,
            title="Task Project Test",
            description="Test Test test",
            price=300,
            completed=False,
            paid=False

        )
        work_task_repo = WorkTaskRepo()
        user_project_validate = PermissionValidator(UserRepo())
        self.get_task_interactor = GetTaskInteractor(work_task_repo, user_project_validate)

    def test_set_params_execute(self):
        work_task = self.get_task_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id,
            task_id=self.work_task_orm.id
        ).execute()
        self.assertEqual(work_task.id, self.work_task_orm.id)
        self.assertEqual(work_task.title, self.work_task_orm.title)
        self.assertEqual(work_task.description, self.work_task_orm.description)
        self.assertEqual(work_task.paid, self.work_task_orm.paid),
        self.assertEqual(work_task.completed, self.work_task_orm.completed)

    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.get_task_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id,
                task_id=self.work_task_orm.id
            ).execute()


    def test_set_params_execute_entity_not_found(self):
        with self.assertRaises(EntityDoesNotExistException):
            self.get_task_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm.id,
                task_id=None
            ).execute()



class CreateTaskInteractorTest(TestCase):

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
            type_of_payment='T_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm_2 = ProjectORM.objects.create(
            title='Test Project 2',
            description='My Test project 2',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm_2.id
        )

        self.work_task_orm = WorkTaskORM.objects.create(
            project_id=self.project_orm.id,
            title="Task Project Test",
            description="Test Test test",
            price=300,
            completed=False,
            paid=False
        )
        work_task_repo = WorkTaskRepo()
        user_project_validate = PermissionValidator(UserRepo())
        project_repo = ProjectRepo()
        type_of_payment_validator = FieldValidator()
        self.create_task_interactor = CreateTaskInteractor(work_task_repo, project_repo, user_project_validate,
                                                           type_of_payment_validator)



    def test_set_params_execute(self):
        created_task = self.create_task_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id,
            title="Test TaskInteractor",
            description="Test set_params execute",
            price=500,
            completed=False,
            paid=False
        ).execute()

        task_orm = WorkTaskORM.objects.get(id=created_task.id)
        self.assertEqual(created_task.project_id, self.project_orm.id)
        self.assertEqual(created_task.title, "Test TaskInteractor")
        self.assertEqual(created_task.description, "Test set_params execute")
        self.assertEqual(created_task.price, 500)
        self.assertEqual(created_task.completed, False)
        self.assertEqual(created_task.paid, False)

        self.assertEqual(created_task.project_id, task_orm.project.id)
        self.assertEqual(created_task.title, task_orm.title)
        self.assertEqual(created_task.description, task_orm.description)
        self.assertEqual(created_task.price, task_orm.price)
        self.assertEqual(created_task.completed, task_orm.completed)
        self.assertEqual(created_task.paid, task_orm.paid)

    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.create_task_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id,
                title="Test TaskInteractor",
                description="Test set_params execute",
                price=500,
                completed=False,
                paid=False
            ).execute()

    def test_set_params_execute_no_pemission(self):
        with self.assertRaises(NoPermissionException):
            self.create_task_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=self.project_orm_2.id,
                title="Test TaskInteractor",
                description="Test set_params execute",
                price=500,
                completed=False,
                paid=False
            ).execute()


    def test_set_params_execute_type_of_payment_validate(self):
        project_orm = ProjectORM.objects.create(
            title='Test Project 2',
            description='My Test project 2',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        with self.assertRaises(InvalidEntityException):
            self.create_task_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=project_orm.id,
                title="Test TaskInteractor",
                description="Test set_params execute",
                price=500,
                completed=False,
                paid=False
            ).execute()

        try:
            self.create_task_interactor.set_params(
                logged_id=self.user_orm.id,
                project_id=project_orm.id,
                title="Test TaskInteractor",
                description="Test set_params execute",
                price=500,
                completed=False,
                paid=False
            ).execute()

        except InvalidEntityException as e:
            self.assertRegex(str(e), "The type of payment for the project must be T_P")



class UpdateTaskInteractorTest(TestCase):

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
            type_of_payment='T_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm_2 = ProjectORM.objects.create(
            title='Test Project 2',
            description='My Test project 2',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm_2.id
        )

        self.work_task_orm = WorkTaskORM.objects.create(
            project_id=self.project_orm.id,
            title="Task Project Test",
            description="Test Test test",
            price=300,
            completed=False,
            paid=False
        )
        work_task_repo = WorkTaskRepo()
        user_project_validate = PermissionValidator(UserRepo())
        project_repo = ProjectRepo()
        self.update_task_interactor = UpdateTaskInteractor(work_task_repo, project_repo, user_project_validate)



    def test_set_params_execute(self):
        updated_task = self.update_task_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id,
            task_id=self.work_task_orm.id,
            title="Task Project Test Update",
            price=3000,
            completed=True,
            paid=True
        ).execute()
        self.assertEqual(type(updated_task), WorkTask)
        self.assertEqual(self.work_task_orm.id, updated_task.id)
        task_orm = WorkTaskORM.objects.get(id=updated_task.id)
        self.assertEqual(updated_task.project_id, self.project_orm.id)
        self.assertEqual(updated_task.title, "Task Project Test Update")
        self.assertEqual(updated_task.description, "Test Test test")
        self.assertEqual(updated_task.price, 3000)
        self.assertEqual(updated_task.paid, True)
        self.assertEqual(updated_task.completed, True)

        self.assertEqual(updated_task.title, task_orm.title)
        self.assertEqual(updated_task.description, task_orm.description)
        self.assertEqual(updated_task.price, task_orm.price)
        self.assertEqual(updated_task.paid, task_orm.paid)
        self.assertEqual(updated_task.completed, task_orm.completed)



    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.update_task_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id,
                task_id=self.work_task_orm.id,
                title="Task Project Test Update",
                price=3000,
                completed=True,
                paid=True
            ).execute()


    def test_set_params_execute_no_permission(self):
        with self.assertRaises(NoPermissionException):
            self.update_task_interactor.set_params(
                logged_id=self.user_orm_2.id,
                project_id=self.project_orm.id,
                task_id=self.work_task_orm.id,
                title="Task Project Test Update",
                price=3000,
                completed=True,
                paid=True
            ).execute()


    def test_set_params_execute_no_permission_project_id(self):
        project_orm = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        with self.assertRaises(NoPermissionException):
            self.update_task_interactor.set_params(
                logged_id=self.user_orm_2.id,
                project_id=project_orm.id,
                task_id=self.work_task_orm.id,
                title="Task Project Test Update",
                price=3000,
                completed=True,
                paid=True
            ).execute()




class DeleteTaskInteractorTest(TestCase):

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
            type_of_payment='T_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm_2 = ProjectORM.objects.create(
            title='Test Project 2',
            description='My Test project 2',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm_2.id
        )

        self.work_task_orm = WorkTaskORM.objects.create(
            project_id=self.project_orm.id,
            title="Task Project Test",
            description="Test Test test",
            price=300,
            completed=False,
            paid=False
        )
        work_task_repo = WorkTaskRepo()
        user_project_validate = PermissionValidator(UserRepo())
        self.delete_task_interactor = DeleteTaskInteractor(work_task_repo, user_project_validate)


    def test_set_params_execute(self):
        deleted_task = self.delete_task_interactor.set_params(
            logged_id=self.user_orm.id,
            task_id=self.work_task_orm.id
        ).execute()

        self.assertEqual(type(deleted_task), WorkTask)
        self.assertEqual(deleted_task.id, self.work_task_orm.id)
        with self.assertRaises(WorkTaskORM.DoesNotExist):
            WorkTaskORM.objects.get(id=self.work_task_orm.id)

    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.delete_task_interactor.set_params(
                logged_id=None,
                task_id=self.work_task_orm.id
            ).execute()




class GetAllTaskInteractorTest(TestCase):

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
            type_of_payment='T_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm.id
        )

        self.project_orm_2 = ProjectORM.objects.create(
            title='Test Project 2',
            description='My Test project 2',
            type_of_payment='M_P',
            start_date=datetime.datetime.now() - datetime.timedelta(days=30),
            end_date=datetime.datetime.now(),
            user_id=self.user_orm_2.id
        )
        for i in range(10):
            WorkTaskORM.objects.create(
                project_id=self.project_orm.id,
                title="Task Project Test",
                description="Test Test test",
                price=300,
                completed=False,
                paid=False
            )
        work_task_repo = WorkTaskRepo()
        user_project_validate = PermissionValidator(UserRepo())
        field_validator = FieldValidator()
        self.get_all_task_interactor = GetAllTasksInteractor(work_task_repo, user_project_validate, field_validator)


    def test_set_params_execute(self):
        tasks = self.get_all_task_interactor.set_params(
            logged_id=self.user_orm.id,
            project_id=self.project_orm.id
        ).execute()

        self.assertEqual(type(tasks), list)
        self.assertEqual(len(tasks), 10)
        self.assertEqual(type(tasks.pop()), WorkTask)
        self.assertEqual(type(tasks.pop()), WorkTask)


    def test_set_params_execute_no_logged(self):
        with self.assertRaises(NoLoggedException):
            self.get_all_task_interactor.set_params(
                logged_id=None,
                project_id=self.project_orm.id
            ).execute()




class ProjectGetTotalInteractorTest(TestCase):
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
        self.user_repo = UserRepo()
        self.user_permission_validator = PermissionValidator(UserRepo())
        self.field_validator = FieldValidator()
        self.project_interactor = ProjectGetTotalInteractor(self.project_repo, self.user_repo,
                                                            self.user_permission_validator, self.field_validator)



