from django.test import TestCase, Client
from django.urls import reverse
from account.validators import *


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

        header = {'HTTP_AUTHORIZATION': token + "25" }
        response_get = self.client.get(reverse('get_user'), **header)
        body = json.loads(response_get.content.decode())
        message = body.get('error').get('message')
        self.assertRegex(message, 'Authentication required')

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
        self.assertRegex(message, 'Email not allowed')