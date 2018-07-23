from django.test import TestCase
from account.models import UserORM
from project.models import ProjectORM, HourPaymentORM, WorkTimeORM, WorkTaskORM, MonthPaymentORM, WorkDayORM
from project.entities import Project, WorkTask, WorkTime, WorkedDay
from project.repositories import ProjectRepo, WorkTaskRepo
from project.interactors import GetProjectInteractor, CreateProjectInteractor
from PayDevs.exceptions import *
from project.validators import *
#TODO add integration tests, interactors tests etc..

# -------------------------- Project_Tests ------------------------------------- #

class ProjectRepoMethodTest(TestCase):

    def setUp(self):
        self.user = UserORM(username="islam", password='sizam123')
        self.user.save()
        self.project_repo = ProjectRepo()

        self.project = ProjectORM(title="PayDevs", description="Time is Money", user=self.user, type_of_payment='T_P',
                                  end_date=timezone.now() + timedelta(days=30), status=True)
        self.project.save()



    def test_get_method(self):
        project1 = self.project_repo.get(user_id=self.user.id, project_id=self.project.id)
        project2 = self.project_repo.get(user_id=self.user.id, title=self.project.title)

        self.assertIsNotNone(project1)

        self.assertTrue(project1.__dict__ == project2.__dict__)

        self.assertEqual(project1.title, "PayDevs")

        self.assertEqual(project1.description, "Time is Money")

        self.assertEqual(project1.type_of_payment, "T_P")

        self.assertTrue(project1.status)

        with self.assertRaises(NoPermissionException):
            self.project_repo.get(user_id=self.user.id+1, project_id=self.project.id)

        with self.assertRaises(EntityDoesNotExistException):
            self.project_repo.get(user_id=self.user.id, project_id=self.project.id+1)



    def test_create_method(self):
        project1 = self.project_repo.create(self.user.id, "TestingTesting", "1..2..3..", "H_P", 12)

        self.assertIsNotNone(project1)

        self.assertEqual(project1.title, "TestingTesting")

        self.assertEqual(project1.description, "1..2..3..")

        self.assertTrue(project1.status)

        with self.assertRaises(NoPermissionException):
            self.project_repo.create(self.user.id+1, "TestingTesting", "1..2..3..", "H_P", 12)


    def test_set_rate_private_method(self):

        project_entity = self.project_repo.create(self.user.id, "TestingTesting", "1..2..3..", "H_P", 12)

        db_project = ProjectORM.objects.get(id=project_entity.id)

        type_of_payment1 = HourPaymentORM.objects.get(project=db_project)

        self.assertEqual(db_project.hourpaymentorm_set.all()[0], HourPaymentORM.objects.filter(project=db_project)[0])

        self.assertEqual(HourPaymentORM.objects.get(project=db_project), type_of_payment1)

        self.assertEqual(type_of_payment1.rate, 12)

        project2 = self.project_repo.create(self.user.id, "TestingTesting", "1..2..3..", "M_P", 300)

        type_of_payment2 = MonthPaymentORM.objects.get(project=project2.id)

        self.assertEqual(MonthPaymentORM.objects.get(project=project2.id), type_of_payment2)

        self.assertEqual(type_of_payment2.rate, 300)



    def test_update_method(self):
        new_attrs = {
            'title': "PayDevs300",
            'description': "Bla-bla-bla",
            'type_of_payment': "M_P",
            'status': False
        }
        self.project_repo.update(self.user.id, self.project.id, new_attrs)

        updated_project = ProjectORM.objects.get(id=self.project.id)

        self.assertEqual(updated_project.title, "PayDevs300")

        self.assertEqual(updated_project.description, "Bla-bla-bla")

        self.assertEqual(updated_project.type_of_payment, "M_P")

        self.assertFalse(updated_project.status)


        new_attrs_with_None = {
            'title': "TimeTracker",
            'description': 'new name sucks',
            'type_of_payment': None,
            'status': None
        }
        self.project_repo.update(self.user.id, self.project.id, new_attrs_with_None)

        updated_project = ProjectORM.objects.get(id=self.project.id)

        self.assertEqual(updated_project.title, "TimeTracker")

        self.assertEqual(updated_project.description, "new name sucks")

        self.assertEqual(updated_project.type_of_payment, "M_P")

        self.assertFalse(updated_project.status)

        with self.assertRaises(NoPermissionException):
            self.project_repo.update(self.user.id+1, self.project.id, {})

        with self.assertRaises(NoPermissionException):
            self.project_repo.update(self.user.id, self.project.id+1, {})

        self.project_repo.update(self.user.id, self.project.id, {'not_existing_field': True})

        with self.assertRaises(AttributeError):
            self.project_repo.get(user_id=self.user.id, project_id=self.project.id).not_existing_field == True



    def test_delete_method(self):
        deleted_project_entity = self.project_repo.delete(user_id=self.user.id, project_id=self.project.id)

        self.assertEqual(deleted_project_entity.title, "PayDevs")

        self.assertEqual(deleted_project_entity.description, "Time is Money")

        self.assertEqual(deleted_project_entity.type_of_payment, "T_P")

        self.assertTrue(deleted_project_entity.status)

        with self.assertRaises(EntityDoesNotExistException):
            self.project_repo.get(user_id=self.user.id, project_id=self.project.id)



    def test_decode_private_method(self):
        project_entity = self.project_repo._decode_db_project(self.project)

        self.assertTrue(isinstance(project_entity, Project))

        self.assertNotEquals(project_entity.__dict__, self.project.__dict__)

        self.assertEqual(project_entity.id, self.project.id)

        self.assertEqual(project_entity.user, self.project.user.__str__())

        self.assertEqual(project_entity.title, self.project.title)

        self.assertEqual(project_entity.description, self.project.description)

        self.assertEqual(project_entity.start_date, self.project.start_date)

        self.assertEqual(project_entity.end_date, self.project.end_date)

        self.assertEqual(project_entity.type_of_payment, self.project.type_of_payment)

        self.assertEqual(project_entity.status, self.project.status)




    class ProjectInteractorsTest(TestCase):

        def setUp(self):
            self.create_project_interactor = CreateProjectInteractor(ProjectRepo())
            self.get_project_interactor = GetProjectInteractor(ProjectRepo())
            self.user = UserORM(username="IslaMurtazaev", password="sizam123")


        def test_methods(self):
            self.create_project_interactor.project_repo.create(self.user.id, "title1", "description1", "T_P")
            created_project = self.get_project_interactor.project_repo.get(self.user.id, "title1")

            self.assertEqual(created_project.title, "title1")

            self.assertEqual(created_project.description, "description1")

            self.assertEqual(created_project.type_of_payment, "T_P")

            self.assertEqual(created_project.status, True)



# ------------------------ Total_Tests -------------------------------------- #

class TotalMethodTest(TestCase):

    def setUp(self):
        self.user = UserORM(username="admin", password='qwert12345')
        self.user.save()

        self.project_with_tasks = ProjectORM(title="My Firs Project", user=self.user, type_of_payment='T_P')
        self.project_with_tasks.save()

        ProjectRepo().create(self.user.id, 'title', 'with hour payment', 'H_P', 12)

        ProjectRepo().create(self.user.id, 'title', 'with month payment', 'M_P', 300)



    def test_get_type_of_payment(self):

        task_payment = ProjectRepo().get_type_of_payment(self.user.id, self.project_with_tasks.id)

        self.assertEqual('T_P', task_payment)

        hour_payment = ProjectRepo().get_type_of_payment(self.user.id, ProjectORM.objects.get(description='with hour payment').id)

        self.assertEqual('H_P', hour_payment)

        month_payment = ProjectRepo().get_type_of_payment(self.user.id, ProjectORM.objects.get(description='with month payment').id)

        self.assertEqual('M_P', month_payment)



    def test_get_total_worked_tasks(self):
        for i in range(10):
            worked_task = WorkTaskORM(title='My Task number %s' % i, price=10 * (i + 1), completed=True, project=self.project_with_tasks)
            worked_task.save()

        total_worked = ProjectRepo().get_worked(project_id=self.project_with_tasks.id, type_of_payment='T_P')
        total = Project.get_total('T_P', total_worked)

        self.assertEqual(type(total), float)
        self.assertEqual(total, 550)


    def test_get_total_worked_paid_and_unpaid_tasks(self):
        for i in range(10):
            worked_task = WorkTaskORM(title='My Task number %s' % i, price=10 * (i + 1), completed=True, project=self.project_with_tasks)
            if i % 2 == 0:
                worked_task.paid = True
            else:
                worked_task.paid = False
            worked_task.save()

        total_worked = ProjectRepo().get_worked(project_id=self.project_with_tasks.id, type_of_payment='T_P')
        total = Project.get_total('T_P', total_worked)

        self.assertTrue(type(total_worked), WorkTask)
        self.assertEqual(type(total), float)
        self.assertEqual(total, 300)


    def test_get_total_worked_paid_tasks(self):
        worked_task = WorkTaskORM(title='My Task number %s' % 100, price=100000, completed=True, paid=True, project=self.project_with_tasks)
        worked_task.save()

        total_worked = ProjectRepo().get_worked(project_id=self.project_with_tasks.id, type_of_payment='T_P')
        total = Project.get_total('T_P', total_worked)

        self.assertEqual(type(total), int)
        self.assertEqual(total, 0)


    def test_get_total_worked_completed_and_uncompleted_tasks(self):
        for i in range(10):
            worked_task = WorkTaskORM(title='My Task number %s' % i, price=10 * (i + 1), project=self.project_with_tasks)
            if i % 2 == 0:
                worked_task.completed = False
            else:
                worked_task.completed = True
            worked_task.save()

        total_worked = ProjectRepo().get_worked(project_id=self.project_with_tasks.id, type_of_payment='T_P')
        total = Project.get_total('T_P', total_worked)

        self.assertEqual(type(total), float)
        self.assertEqual(total, 300)



    def test_total_worked_time(self):
        project = ProjectORM.objects.get(description='with hour payment')
        hour_payment = project.hourpaymentorm_set.get(id=1)
        HourPaymentORM(project=project, rate=15).save()
        hour_payment2 = project.hourpaymentorm_set.get(id=2)

        for i in range(10):
            worked_time = WorkTimeORM(hour_payment=hour_payment, start_work=timezone.now() + timedelta(days=i),
                                      end_work=timezone.now() + timedelta(hours=8, days=i))
            worked_time.save()

        total_worked = ProjectRepo().get_worked(project_id=project.id, type_of_payment='H_P',
                                                start_date_boundary=(timezone.now() - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                                end_date_boundary=(timezone.now() + timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

        self.assertEqual(type(total_worked[0]), WorkTime)

        self.assertEqual(len(total_worked), 1)

        total = Project.get_total('H_P', total_worked)

        self.assertEqual(total, 96)



        total_worked = ProjectRepo().get_worked(project_id=project.id, type_of_payment='H_P',
                                                start_date_boundary=(timezone.now() - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                                end_date_boundary=(timezone.now() + timedelta(hours=8, days=10)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

        self.assertEqual(type(total_worked[0]), WorkTime)

        self.assertEqual(len(total_worked), 10)

        total = Project.get_total('H_P', total_worked)

        self.assertEqual(total, 960)


        new_work_time = WorkTimeORM(hour_payment=hour_payment2, start_work=timezone.now() + timedelta(days=10), end_work=timezone.now() + timedelta(hours=8, days=10))
        new_work_time.save()

        total_worked = ProjectRepo().get_worked(project_id=project.id, type_of_payment='H_P',
                                                start_date_boundary=(timezone.now() - timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                                end_date_boundary=(timezone.now() + timedelta(hours=8, days=10)).strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

        self.assertEqual(len(total_worked), 11)

        total = Project.get_total('H_P', total_worked)

        self.assertEqual(total, 1080)


        with self.assertRaises(NoPermissionException):
            ProjectRepo().get_worked(project.id+10, 'H_P', "2018-08-02T00:00:00.000Z", "2018-08-03T00:00:00.000Z")


        with self.assertRaises(InvalidEntityException):
            ProjectRepo().get_worked(project.id, 'H_P', start_date_boundary=(timezone.now() - timedelta(hours=1)),
                                     end_date_boundary=(timezone.now() + timedelta(hours=8, days=10)))

        with self.assertRaises(InvalidEntityException):
            ProjectRepo().get_worked(project.id, 'H_P', "2018-08-02_00:00:00.000Z", "2018-08-03_00:00:00.000Z")



    def test_total_worked_days(self):
        project = ProjectORM.objects.get(description='with month payment')

        MonthPaymentORM(project=project, rate=100).save()

        month_payment = project.monthpaymentorm_set.get(id=1)

        month_payment2 = project.monthpaymentorm_set.get(id=2)

        WorkDayORM(month_payment=month_payment, day=timezone.now()).save()

        total_worked = ProjectRepo().get_worked(project_id=project.id, type_of_payment='M_P')

        self.assertEqual(total_worked, [])

        total = Project.get_total('M_P', total_worked)

        self.assertEqual(total, 0)

        with self.assertRaises(InvalidEntityException):
            ProjectRepo().get_worked(project_id=project.id, type_of_payment='H_P')


        previous_month = timezone.now().replace(month=timezone.now().month-1)

        WorkDayORM(month_payment=month_payment, day=previous_month).save()

        total_worked = ProjectRepo().get_worked(project_id=project.id, type_of_payment='M_P')

        self.assertEqual(len(total_worked), 1)

        self.assertTrue(type(total_worked[0]), WorkedDay)

        total = Project.get_total('M_P', total_worked)

        self.assertEqual(type(total), float)

        self.assertEqual(total, 300)



        WorkDayORM(month_payment=month_payment, day=previous_month).save()

        total_worked = ProjectRepo().get_worked(project_id=project.id, type_of_payment='M_P')

        self.assertTrue(len(total_worked) == 2)

        total = Project.get_total('M_P', total_worked)

        self.assertEqual(type(total), float)

        self.assertEqual(total, 600)

        with self.assertRaises(NoPermissionException):
            ProjectRepo().get_worked(project_id=project.id+10, type_of_payment='M_P')

        WorkDayORM(month_payment=month_payment2, day=previous_month).save()

        total_worked = ProjectRepo().get_worked(project_id=project.id, type_of_payment='M_P')

        total = Project.get_total('M_P', total_worked)

        self.assertTrue(len(total_worked) == 3)

        self.assertEqual(type(total), float)

        self.assertEqual(total, 700)




class TitleMinLengthValidatorMethodTest(TestCase):
    def test_method_type(self):
        self.assertEqual(None, TitleMinLengthValidator().validate('Pro'))
        self.assertEqual(None, TitleMinLengthValidator().validate('PayDevs'))

        with self.assertRaises(InvalidEntityException):
            TitleMinLengthValidator().validate('A')


        with self.assertRaises(InvalidEntityException):
            TitleMinLengthValidator().validate(' ')



class TitleMaxLengthValidatorMethodTest(TestCase):
    def test_method_type(self):
        self.assertEqual(None, TitleMaxLengthValidator().validate('zhanzat'))
        self.assertEqual(None, TitleMaxLengthValidator().validate('zhanzatbekzatadiduduk'))

        with self.assertRaises(InvalidEntityException):
            TitleMaxLengthValidator().validate('zhanzatbekzatduulatadiletboldukanusonbek')


class TitleRegexValidatorMethodTest(TestCase):
    def test_method_type(self):
        self.assertEqual(None, TitleRegex().validate('24K'))
        self.assertEqual(None, TitleRegex().validate('Pay_Devs'))
        self.assertEqual(None, TitleRegex().validate('Pay-Devs'))
        self.assertEqual(None, TitleRegex().validate('McDonald\'s'))
        self.assertEqual(None, TitleRegex().validate('PayDevs 1.2'))



        with self.assertRaises(InvalidEntityException):
            TitleRegex().validate('-PayDevs')

        with self.assertRaises(InvalidEntityException):
            TitleRegex().validate('_Paydevs')


        with self.assertRaises(InvalidEntityException):
            TitleRegex().validate('zhanzat.')

        with self.assertRaises(InvalidEntityException):
            TitleRegex().validate('zhanzat, ')



class PositiveRateValidatorMethodTest(TestCase):
    def test_method_type(self):
        self.assertEqual(None, PositiveRateValidator().validate(200))
        self.assertEqual(None, PositiveRateValidator().validate(0))

        with self.assertRaises(InvalidEntityException):
            PositiveRateValidator().validate(-10)


class RateTypeValidatorMethodTest(TestCase):
    def test_method_type(self):
        self.assertEqual(None, RateTypeValidator().validate(234.45))
        self.assertEqual(None, RateTypeValidator().validate(234))        

        with self.assertRaises(InvalidEntityException):
            RateTypeValidator().validate("Billion")

        with self.assertRaises(InvalidEntityException):
            RateTypeValidator().validate(None)

        with self.assertRaises(InvalidEntityException):
            RateTypeValidator().validate([100,34,21])

        with self.assertRaises(InvalidEntityException):
            RateTypeValidator().validate((12,3,543))


class NoRangeValidatorMethodTest(TestCase):

    def test_method_type(self):
        start_date = timezone.now()
        end_date = start_date + timedelta(days=30)
        self.assertEqual(None, NoRangeValidator().validate(start_date, end_date))

        with self.assertRaises(InvalidEntityException):
            NoRangeValidator().validate(start_date, start_date)



class StartBeforeEndValidatorMethodTest(TestCase):

    def test_method_type(self):
        start_date = timezone.now()
        end_date = start_date - timedelta(days=30)

        with self.assertRaises(InvalidEntityException):
            StartBeforeEndValidator().validate(start_date, end_date)



class TypeOfPaymentValidatorMethodTest(TestCase):

    def test_method_type(self):
        self.assertEqual(None, TypeOfPaymentValidator().validate('H_P'))
        self.assertEqual(None, TypeOfPaymentValidator().validate('M_P'))


        with self.assertRaises(InvalidEntityException):
            TypeOfPaymentValidator().validate('Y_P')