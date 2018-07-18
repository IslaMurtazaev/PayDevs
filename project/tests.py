from django.test import TestCase
from account.models import UserORM
from project.models import ProjectORM, HourPaymentORM, WorkTimeORM, WorkTaskORM, MonthPaymentORM, WorkDayORM
from project.entities import Project
from project.repositories import ProjectRepo, WorkTaskRepo
from PayDevs.exceptions import *
from project.validators import *


# -------------------------- Project_Tests ------------------------------------- #

class ProjectMethodTest(TestCase):

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


    def test_set_rate_private_methd(self):

        project1 = self.project_repo.create(self.user.id, "TestingTesting", "1..2..3..", "H_P", 12)

        self.assertEqual(HourPaymentORM.objects.get(project=project1.id).rate, 12)

        # self.assertGreater(len(project1.hourpaymentorm_set.all()), 0)




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

        with self.assertRaises(InvalidEntityException):
            self.project_repo.update(self.user.id, self.project.id, {'not_existing_field': True})



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


# ------------------------ TaskWork_Tests -------------------------------------- #

class WorkTaskMethodTest(TestCase):

    def setUp(self):
        user = UserORM(username="admin", password='qwert12345')
        user.save()
        self.user_id = user.id

        self.project = ProjectORM(title="My Firs Project", user=user, type_of_payment='T_P')
        self.project.save()
        self.project_id = self.project.id


    def test_get_total_method(self):
        for i in range(10):
            worked_task = WorkTaskORM(title='My Task number %s' % i, price=10 * (i + 1), completed=True, project=self.project)
            worked_task.save()

        total = ProjectRepo().get_total(user_id=self.user_id, project_id=self.project_id)

        self.assertEqual(type(total), float)
        self.assertEqual(total, 550)


    def test_get_total_paid_method(self):
        worked_task = WorkTaskORM(title='My Task number %s' % 100, price=100000, completed=True, paid=True, project=self.project)
        worked_task.save()

        total = ProjectRepo().get_total(user_id=self.user_id, project_id=self.project_id)

        self.assertEqual(type(total), int)
        self.assertEqual(total, 0)



# class HourPaymentMethodTest(TestCase):
#     def setUp(self):
#         user = User(username="admin", password='qwert12345')
#         user.save()
#         self.project = ProjectModel(name="My Firs Project", user=user, type_of_payment='H_P')
#         self.project.save()
#         self.hour_pay = HourPaymentModel(project=self.project, rate=10.0, start_rout_date=timezone.now() - timedelta(days=1),
#                                          end_rout_date=timezone.now() + timedelta(days=1))
#         self.hour_pay.save()


#     def test_method_total_type(self):
#         for i in range(10):
#             wt = WorkTime(rate=self.hour_pay, start_work=timezone.now()-timedelta(hours=2),
#                           end_work=timezone.now()-timedelta(hours=1))
#             wt.save()
#         self.assertEqual(type(self.hour_pay.total()), float)
#         self.assertEqual(self.hour_pay.total(), 100.0)



# class MonthPaymentMethodTest(TestCase):
#     def setUp(self):
#         user = User(username="admin", password='qwert12345')
#         user.save()
#         self.project = ProjectModel(name="My Firs Project", user=user, type_of_payment='M_P')
#         self.project.save()
#         self.month_pay = MonthPayment(project=self.project, rate=50.0)
#         self.month_pay.save()


#     def test_method_total_month(self):
#         for i in range(30):
#             workday = WorkDay(month_payment=self.month_pay, day=(timezone.now()-timedelta(days=1)).date(),
#                               have_worked=True)
#             workday.save()

#         self.assertEqual(self.month_pay.total(), 1500)



# class ProjectMethodTest(TestCase):
#     def setUp(self):
#         user = User(username="admin", password='qwert12345')
#         user.save()
#         self.project_task = ProjectModel(name="My Project Task", user=user, type_of_payment='T_P')
#         self.project_task.save()
#         self.project_hour = ProjectModel(name="My Project Hour Payment", user=user, type_of_payment='H_P')
#         self.project_hour.save()
#         self.project_month = ProjectModel(name="My Project Hour Payment", user=user, type_of_payment='M_P')
#         self.project_month.save()




#     def test_method_total_task(self):
#         for i in range(10):
#             hour_pay = TaskPayment(name='My Task number %s' % i, cost=10 * (i + 1), status=True,
#                                    project=self.project_task)
#             hour_pay.save()

#         self.assertEqual(self.project_task.total(), 550)

#     def test_method_total_hour(self):
#         for i in range(2):
#             hour_pay = HourPaymentModel(project=self.project_hour, rate=1.0,
#                                         start_rout_date=timezone.now()-timedelta(days=1),
#                                         end_rout_date=timezone.now() + timedelta(days=1))
#             hour_pay.save()
#             for j in range(10):
#                 wt = WorkTime(rate=hour_pay, start_work=timezone.now() - timedelta(hours=2),
#                               end_work=timezone.now() - timedelta(hours=1))
#                 wt.save()

#         self.assertEqual(type(self.project_hour.total()), float)
#         self.assertEqual(self.project_hour.total(), 20)

#     def test_method_total_month(self):
#         for i in range(10):
#             month_pay = MonthPayment(project=self.project_month, rate=1.0)
#             month_pay.save()

#             for j in range(30):
#                 workday = WorkDay(month_payment=month_pay, day=(timezone.now() - timedelta(days=(i + 1))).date(),
#                                   have_worked=(i % 2 == 0))
#                 workday.save()

#         self.assertEqual(self.project_month.total(), 150)


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