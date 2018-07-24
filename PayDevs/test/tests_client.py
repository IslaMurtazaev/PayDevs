from django.test import TestCase, Client
from django.urls import reverse
import json


class ClientAccountTest(TestCase):
    def setUp(self):
        self.client = Client()
        data = json.dumps({'username': 'TestUser',
                           'email': 'testuser@email.ru',
                           'password': 'qwert12345'})
        self.client.post(reverse('create_user'), data, content_type="application/json")
        data = json.dumps({'username': 'TestUser',
                           'password': 'qwert12345'})
        response = self.client.post(reverse('login_user'), data, content_type="application/json")
        body = json.loads(response.content.decode())
        self.token = body.get('token')


    def test_create_user_get_token(self):
        data = json.dumps({
                    "title": "Project web",
                    "description": "logic web site",
                    "start_date": "2016-12-20T23:00:00.000000Z+0600",
                    "end_date": "2018-12-20T12:30:00.000000Z+0600",
                    "type_of_payment": "H_P",

                })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.post(reverse('create_project'), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('title'), 'Project web')
        self.assertEqual(body.get('description'), 'logic web site')
        self.assertEqual(body.get('start_date'), "2016-12-20T23:00:00.000000Z+0600")
        self.assertEqual(body.get('end_date'), "2018-12-20T12:30:00.000000Z+0600")