from django.test import TestCase, Client
from django.urls import reverse
from account.entities import User
from account.models import UserORM
from account.serializers import UserSerializer, UserListSerializer
from account.validators import *
from PayDevs.exceptions import InvalidEntityException


# ----------------PASSWORD VALIDATORS TESTS------------------------------------#



class MinimumLengthValidatorMethodTest(TestCase):
    def test_method_validate_type(self):
        with self.assertRaises(InvalidEntityException):
            MinimumLengthValidator().validate('passwor')

        with self.assertRaises(InvalidEntityException):
            MinimumLengthValidator().validate('1234')

        self.assertIsNone(MinimumLengthValidator().validate('password'))

        self.assertIsNone(MinimumLengthValidator().validate('123456789'))

        self.assertIsNone(MinimumLengthValidator().validate('1234567890qwertyuioasdfghjklzxcvbnm'))


class UserAttributeSimilarityValidatorMethodTest(TestCase):
    def setUp(self):
        UserORM.objects.create(username="IslamIsTheBest", email="islam.muratazaev@gmail.com", \
                               password="islamisthebest")

    def test_method_validate_type(self):
        islam = UserORM.objects.get(username="IslamIsTheBest")
        with self.assertRaises(InvalidEntityException):
            UserAttributeSimilarityValidator().validate(password=islam.password, user=islam)

        self.assertIsNone(UserAttributeSimilarityValidator().validate(password='sizamopen', user=islam))


class CommonPasswordValidatorMethodTest(TestCase):
    def test_method_validate_type(self):
        with self.assertRaises(InvalidEntityException):
            CommonPasswordValidator().validate('123456789')

        with self.assertRaises(InvalidEntityException):
            CommonPasswordValidator().validate('abcdefghijklmnopqrstuvwxyz')

        with self.assertRaises(InvalidEntityException):
            CommonPasswordValidator().validate('~!@#$%^&*()_+')

        self.assertIsNone(CommonPasswordValidator().validate('sizam321'))

        self.assertIsNone(CommonPasswordValidator().validate('thisisverycomplicated1943'))

        self.assertIsNone(CommonPasswordValidator().validate('02081999myBD'))


class NumericPasswordValidatorMethodTest(TestCase):
    def test_method_validate_type(self):
        with self.assertRaises(InvalidEntityException):
            NumericPasswordValidator().validate('123456')

        with self.assertRaises(InvalidEntityException):
            NumericPasswordValidator().validate('0987654321')

        with self.assertRaises(InvalidEntityException):
            NumericPasswordValidator().validate('1234098765')

        self.assertIsNone(CommonPasswordValidator().validate('sizam321'))

        self.assertIsNone(CommonPasswordValidator().validate('hello'))

        self.assertIsNone(CommonPasswordValidator().validate('its'))

        self.assertIsNone(CommonPasswordValidator().validate('me'))


# ----------------EMAIL VALIDATORS TESTS-------------------------------------#



class EmailValidateMethodTest(TestCase):
    def test_method_validate_type(self):
        with self.assertRaises(InvalidEntityException):
            EmailAtValidators().validate('exmaplemail.ru')

        with self.assertRaises(InvalidEntityException):
            EmailAtValidators().validate('@exmaplemail.ru')

        with self.assertRaises(InvalidEntityException):
            EmailAtValidators().validate('exmaple@mail@.ru')

        with self.assertRaises(InvalidEntityException):
            EmailAtValidators().validate('exmaplemail@.ru')

        with self.assertRaises(InvalidEntityException):
            EmailAtValidators().validate('exmaplemail.ru@')

        with self.assertRaises(InvalidEntityException):
            EmailAtValidators().validate('exmaplemail.@ru')

        self.assertEqual(None, EmailAtValidators().validate('exmaple@mail.ru'))


class EmailForbiddenEmailDomainsValidatorMethodTest(TestCase):
    def test_method_validate_type(self):
        self.assertEqual(None, EmailForbiddenEmailDomainsValidator().validate('exmaple@mail.ru'))
        self.assertEqual(None, EmailForbiddenEmailDomainsValidator().validate('exmapl@gmail.com'))
        with self.assertRaises(InvalidEntityException):
            EmailForbiddenEmailDomainsValidator().validate('exmaple@027168.com')

        with self.assertRaises(InvalidEntityException):
            EmailForbiddenEmailDomainsValidator().validate('exmaple@0-mail.com')

        with self.assertRaises(InvalidEntityException):
            EmailForbiddenEmailDomainsValidator().validate('exmaple@0x00.name')

        with self.assertRaises(InvalidEntityException):
            EmailForbiddenEmailDomainsValidator().validate('exmaple@shitaway.ga')

        with self.assertRaises(InvalidEntityException):
            EmailForbiddenEmailDomainsValidator().validate('exmaple@zzz.com')


class ValidatorFunctionsTest(TestCase):
    def setUp(self):
        self.user = User(username='TestMyTest', email='test@mail.ru')

    def test_function_hashed_password(self):
        hashed = hashed_password('password', user=self.user).decode()
        self.assertTrue(check_password('password', hashed))
        with self.assertRaises(InvalidEntityException):
            hashed_password('pass').decode()
        with self.assertRaises(InvalidEntityException):
            hashed_password('123456789').decode()
        with self.assertRaises(InvalidEntityException):
            hashed_password('test@mail.ru', user=self.user).decode()
        with self.assertRaises(InvalidEntityException):
            hashed_password('TestMyTest', user=self.user).decode()

    def test_function_check_password(self):
        password = 'secret_password'
        hashed = hashed_password(password).decode()
        self.assertTrue(check_password(password, hashed))

    def test_function_validate_password_exception_source_code(self):
        try:
            hashed_password('passw', user=self.user).decode()
        except InvalidEntityException as e:
            self.assertEqual(e.source, 'validate')
            self.assertEqual(e.code, 'not_allowed')

    def test_function_validate_password_minimum_length(self):
        try:
            hashed_password('passw', user=self.user).decode()
        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Your password must contain at least 8 character.')

    def test_function_validate_password_numeric(self):
        try:
            hashed_password('45345465156', user=self.user).decode()
        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Your password consists of only digits.')

    def test_function_validate_password_common(self):
        try:
            hashed_password('qwertyui', user=self.user).decode()
        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Your password is a common sequence.')

    def test_function_validate_password_user_attribute(self):
        try:
            hashed_password('TestMyTest', user=self.user).decode()
        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Your password is too similar to your other fields.')

        try:
            hashed_password('test@mail.ru', user=self.user).decode()
        except InvalidEntityException as e:
            self.assertRegex(str(e), 'Your password is too similar to your other fields.')

    def test_function_validate_username(self):
        with self.assertRaises(InvalidEntityException):
            validate_username('we', user=self.user)

        with self.assertRaises(InvalidEntityException):
            validate_username('_zhanzat', user=self.user)

        with self.assertRaises(InvalidEntityException):
            validate_username('23123sdfsdf', user=self.user)

    def test_function_validate_email(self):
        user = User(username='TestMyTest', email='test@mail.ru')
        self.assertIsNone(validate_email('example@amil.ru', user=user))

    def test_function_validate_email_except(self):
        user = User(username='TestMyTest', email='test@mail.ru')
        with self.assertRaises(InvalidEntityException):
            validate_email('exampleamil.ru', user=user)

        with self.assertRaises(InvalidEntityException):
            validate_email('@exampleamil.ru', user=user)

        with self.assertRaises(InvalidEntityException):
            validate_email('exampleamil.ru@', user=user)

        with self.assertRaises(InvalidEntityException):
            validate_email('exampleamil@.ru', user=user)

        with self.assertRaises(InvalidEntityException):
            validate_email('exampleamil.@ru', user=user)

    def test_function_validate(self):
        try:
            validate('123', self.user, get_password_validators())
        except InvalidEntityException as e:
            self.assertEqual(e.source, 'validate')

        try:
            validate('qweqwe', self.user, get_email_validators())
        except InvalidEntityException as e:
            self.assertEqual(e.source, 'validate')


class ForbiddenNamesValidatorMethodTest(TestCase):
    def test_method_validate_type(self):
        self.assertEqual(None, ForbiddenNamesValidator().validate('zhanzat'))
        self.assertEqual(None, ForbiddenNamesValidator().validate('BrzinaRutina'))

        with self.assertRaises(InvalidEntityException):
            ForbiddenNamesValidator().validate('insTagram')
        with self.assertRaises(InvalidEntityException):
            ForbiddenNamesValidator().validate('PROJECTS')
        with self.assertRaises(InvalidEntityException):
            ForbiddenNamesValidator().validate('alpha')


class UsernameMinLengthValidatorMethodTest(TestCase):
    def test_method_type(self):
        self.assertEqual(None, UsernameMinLengthValidator().validate('Ali'))
        self.assertEqual(None, UsernameMinLengthValidator().validate('Abrakadabra'))

        with self.assertRaises(InvalidEntityException):
            UsernameMinLengthValidator().validate('Po')

        with self.assertRaises(InvalidEntityException):
            UsernameMinLengthValidator().validate('a')


class UsernameMaxLengthValidatorMethodTest(TestCase):
    def test_method_type(self):
        self.assertEqual(None, UsernameMaxLengthValidator().validate('zhanzat'))
        self.assertEqual(None,
                         UsernameMaxLengthValidator().validate('zhanzatbekzatduulatadiletboldukanusonbektaalaibeka'))

        with self.assertRaises(InvalidEntityException):
            UsernameMaxLengthValidator().validate('zhanzatbekzatduulatadiletboldukanusonbektaalaibekafhudlhfsjgyj')


class UsernameRegexMethodValidator(TestCase):
    def test_method_type(self):
        self.assertEqual(None, UsernameRegex().validate('asfsg'))
        self.assertEqual(None, UsernameRegex().validate('Asfsg'))
        self.assertEqual(None, UsernameRegex().validate('zhanzat98'))
        self.assertEqual(None, UsernameRegex().validate('zhanzat_mamytova'))
        self.assertEqual(None, UsernameRegex().validate('Asfsg.sdfdgf'))

        with self.assertRaises(InvalidEntityException):
            UsernameRegex().validate('14355')

        with self.assertRaises(InvalidEntityException):
            UsernameRegex().validate('1zhanzat')

        with self.assertRaises(InvalidEntityException):
            UsernameRegex().validate('_zhanzat')

        with self.assertRaises(InvalidEntityException):
            UsernameRegex().validate('zhanzat, bekzat')


class UserSerializerTest(TestCase):
    def test_user_serializer(self):
        user = User(id=1, username='TestName', email='test@gmail.com', password='123456789', is_active=True,
                    is_staff=False)
        serilalizer = {
            'id': 1,
            'username': 'TestName',
            'email': 'test@gmail.com',
            'is_active': True,
            'is_staff': False,
        }
        self.assertEqual(UserSerializer.model, User)
        self.assertEqual(UserSerializer.fields, ['id', 'username', 'email', 'is_active', 'is_staff'])
        self.assertDictEqual(UserSerializer.serializer(user), serilalizer)


class UserListSerializeTest(TestCase):
    def test_user_serializer(self):
        users = []
        for i in range(3):
            user = User(id=i, username='TestName%d' % i,
                        email='test%d@gmail.com' % i, password='123456789', is_active=True,
                        is_staff=False)
            users.append(user)

        serilalizer = [
            {
                'id': 0,
                'username': 'TestName0',
                'email': 'test0@gmail.com',
            },
            {
                'id': 1,
                'username': 'TestName1',
                'email': 'test1@gmail.com',
            },
            {
                'id': 2,
                'username': 'TestName2',
                'email': 'test2@gmail.com',
            },
        ]

        self.assertEqual(UserListSerializer.model, User)
        self.assertEqual(UserListSerializer.fields, ['id', 'username', 'email'])
        self.assertListEqual(UserListSerializer.serializer(users), serilalizer)


# --------------------------------------Test Client Account -----------------------------------------------#


class ClientAccountTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_creat_user_get_token(self):
        data = json.dumps({'username': 'TestUser',
                           'email': 'testuser@email.ru',
                           'password': 'qwert12345'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body.get('username'), 'TestUser')
        self.assertEqual(body.get('email'), 'testuser@email.ru')
        self.assertEqual(body.get('is_active'), True)
        self.assertEqual(body.get('is_staff'), False)
        # self.assertEqual(body.get('token'), 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
        #                                     'eyJ1c2VyX2lkIjoxfQ.eG9Qo15OqpTeRPyYjML'
        #                                     '8bTAVrGJ50-dDVx72m7d759o')

    def test_login_user_get_token(self):
        data = json.dumps({'username': 'TestUser',
                           'email': 'testuser@email.ru',
                           'password': 'qwert12345'})
        self.client.post(reverse('create_user'), data, content_type="application/json")
        data = json.dumps({'username': 'TestUser',
                'password': 'qwert12345'})
        response = self.client.post(reverse('login_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        token = body.get('token')
        header = {'HTTP_AUTHORIZATION': token}
        response_get = self.client.get(reverse('get_user'), **header)
        body = json.loads(response_get.content.decode())
        self.assertEqual(body.get('username'), 'TestUser')
        self.assertEqual(body.get('email'), 'testuser@email.ru')
        self.assertEqual(body.get('is_active'), True)
        self.assertEqual(body.get('is_staff'), False)

    def test_login_username_validate(self):
        data = json.dumps({'username': 'sd',
                           'email': 'testuser@email.ru',
                           'password': 'qwert12345'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        self.assertRegex(message, 'Your username must contain at least 3 character.')
        data = json.dumps({'username': 'zhanzatbekzatduulatadiletboldukanusonbektaalaibekafhudlhfsjgyj',
                           'email': 'testuser@email.ru',
                           'password': 'qwert12345'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        self.assertRegex(message, 'Your username is too long. Max allowed length is 50.')

        data = json.dumps({'username': '1sddfsdfsd',
                           'email': 'testuser@email.ru',
                           'password': 'qwert12345'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        self.assertRegex(message, 'Username not allowed')


class ClientAccountPasswordValidateTest(TestCase):


    def test_login_password_validate_max_len(self):
        data = json.dumps({'username': 'sddqweqweq',
                           'email': 'testuser@email.ru',
                           'password': 'qwert3'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        self.assertRegex(message, 'Your password must contain at least 8 character.')

    def test_login_password_validate_numeric(self):
        data = json.dumps({'username': 'sddqweqweq',
                           'email': 'testuser@email.ru',
                           'password': '121321231564'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        self.assertRegex(message, 'Your password consists of only digits.')


    def test_login_password_validate_attribute_similarity_salidator(self):
        data = json.dumps({'username': 'sddqweqweq',
                           'email': 'testuser@email.ru',
                           'password': 'sddqweqweq'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        self.assertRegex(message, 'Your password is too similar to your other fields.')


    def test_login_password_validate_common_password_validator(self):
        data = json.dumps({'username': 'sddqweqweq',
                           'email': 'testuser@email.ru',
                           'password': 'abcdefghijklmnopqrstuvwxyz'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        self.assertRegex(message, 'Your password is a common sequence.')



class ClientAccountEmailValidateTest(TestCase):

    def test_login_email_validator(self):
        data = json.dumps({'username': 'sddqweqweq',
                           'email': 'testuseremail.ru',
                           'password': 'abcdefghijklmnopqrstuvwxyz'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        self.assertRegex(message, 'Invalid email address')

    def test_login_email_domaine_validator(self):
        data = json.dumps({'username': 'sddqweqweq',
                           'email': 'testuser@027168.com',
                           'password': 'abcdefghijklmnopqrstuvwxyz'})
        response = self.client.post(reverse('create_user'), data, content_type="application/json")

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        print(message)
        self.assertRegex(message, 'Email not allowed')