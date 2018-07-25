from django.test import TestCase

from PayDevs import settings
from PayDevs.exceptions import EntityDoesNotExistException, InvalidEntityException
from account.entities import User
from account.factories.token_factories import AuthTokenFactory
from account.factories.validate_factories import HashPasswordFactor
from account.interactors import LoginUserInteractor, RegisterUserInteractor, GetUsersInteractor, AuthUserInteractor
from account.models import UserORM
from account.repositories import UserRepo
from account.validators import UsernameEmailValidator


class LoginUserInteractorTest(TestCase):
    def setUp(self):
        self.user = UserORM.objects.create_user(
            username="testUser",
            email="tests@gmail.com",
            password='qwert12345'
        )


    def test_set_params_execute(self):
        user = LoginUserInteractor(UserRepo(), AuthTokenFactory().create()).\
            set_params(username="testUser", password='qwert12345', secret_key=settings.SECRET_KEY).execute()

        self.assertEqual(self.user.id, user.id)
        self.assertEqual(self.user.username, user.username)
        self.assertEqual(self.user.email, user.email)


    def test_set_params_execute_exception(self):
        with self.assertRaises(EntityDoesNotExistException):
            LoginUserInteractor(UserRepo(), AuthTokenFactory().create()).\
                set_params(username="testUser1", password='qwert12345', secret_key=settings.SECRET_KEY).execute()




class RegisterUserInteractorTest(TestCase):
    def test_set_params_execute(self):
        user = RegisterUserInteractor(UserRepo(), UsernameEmailValidator(), HashPasswordFactor()).set_params(
            username="testUser",
            email="tests@gmail.com",
            password='qwert12345',
        ).execute()

        self.assertEqual(type(user), User)
        self.assertEqual(user.username, "testUser")
        self.assertEqual(user.email, "tests@gmail.com")


    def test_set_params_execute_valid_username(self):
        try:
            user = RegisterUserInteractor(UserRepo(), UsernameEmailValidator(),
                                          HashPasswordFactor()).set_params(
                username="te",
                email="tests@gmail.com",
                password='qwert12345',
            ).execute()

        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Your username must contain at least 3 character.')


    def test_set_params_execute_valid_email(self):
        try:
            user = RegisterUserInteractor(UserRepo(), UsernameEmailValidator(),
                                          HashPasswordFactor()).set_params(
                username="testUser",
                email="testgmail@.com",
                password='qwert12345',
            ).execute()

        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Invalid email address')


    def test_set_params_execute_valid_password(self):
        try:
            user = RegisterUserInteractor(UserRepo(), UsernameEmailValidator(),
                                          HashPasswordFactor()).set_params(
                username="testUser",
                email="testg@mail.com",
                password='4545412345',
            ).execute()

        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Your password consists of only digits')
            
            

class GetUsersInteractorTest(TestCase):
    def setUp(self):
        self.user = UserORM.objects.create_user(
            username="testUser",
            email="tests@gmail.com",
            password='qwert12345'
        )

    def test_set_params_execute(self):
        user = GetUsersInteractor(UserRepo()).set_params(id=self.user.id).execute()
        self.assertEqual(user.id, self.user.id)
        self.assertEqual(user.username, self.user.username)
        self.assertEqual(user.email, self.user.email)


    def test_set_params_execute_excaption(self):
        with self.assertRaises(EntityDoesNotExistException):
            GetUsersInteractor(UserRepo()).set_params(id=255654).execute()




class AuthUserInteractorTest(TestCase):
    def setUp(self):
        self.user_db = UserORM.objects.create_user(
            username="testUser",
            email="tests@gmail.com",
            password='qwert12345'
        )
        self.user = LoginUserInteractor(UserRepo(), AuthTokenFactory().create()). \
            set_params(username="testUser", password='qwert12345', secret_key=settings.SECRET_KEY).execute()


    def test_set_params_execute(self):
        user_id = AuthUserInteractor(AuthTokenFactory().create()).set_params(token=self.user.token,
                                                            secret_key=settings.SECRET_KEY).execute()

        self.assertEqual(user_id, self.user.id)
        self.assertEqual(user_id, self.user.id)