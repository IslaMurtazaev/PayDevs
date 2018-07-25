import datetime

from django.test import TestCase, Client
from django.urls import reverse
import json

from account.models import UserORM
from project.models import HourPaymentORM, ProjectORM


class ClientProjectTest(TestCase):
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

        data = json.dumps({
            "title": "Project 1",
            "description": "Test tests",
            "start_date": "2016-12-20T23:00:00.000000Z+0600",
            "end_date": "2018-12-20T12:30:00.000000Z+0600",
            "type_of_payment": "H_P",

        })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.post(reverse('create_project'), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.project_id = body.get('id')

    def test_create_get(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.get(reverse('get_project', kwargs={'project_id': self.project_id}),
                                   content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('title'), "Project 1")
        self.assertEqual(body.get('description'), "Test tests")
        self.assertEqual(body.get('status'), True)

    def test_create_project(self):
        data = json.dumps({
            "title": "Project web",
            "description": "logic web site",
            "start_date": "2016-12-20T23:00:00.000000Z+0600",
            "end_date": "2018-12-20T12:30:00.000000Z+0600",
            "type_of_payment": "H_P",

        })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.put(reverse('create_project'), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('title'), 'Project web')
        self.assertEqual(body.get('description'), 'logic web site')
        self.assertEqual(body.get('start_date'), '2016-12-20 23:00:00+0600')
        self.assertEqual(body.get('end_date'), '2018-12-20 12:30:00+0600')
        self.assertEqual(body.get('status'), True)

    def test_update_project(self):
        data = json.dumps({
            "title": "Project web",
            "description": "logic web site Test update",

        })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.put(reverse('update_project', kwargs={'project_id': self.project_id}), data,
                                   content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('title'), 'Project web')
        self.assertEqual(body.get('description'), "logic web site Test update")
        self.assertEqual(body.get('status'), True)

    def test_update_delete(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        self.client.delete(reverse('delete_project', kwargs={'project_id': self.project_id}),
                           content_type="application/json", **header)

        response = self.client.get(reverse('get_project', kwargs={'project_id': self.project_id}),
                                   content_type="application/json", **header)

        body = json.loads(response.content.decode())
        message = body.get('error').get('message')
        source = body.get('error').get('source')
        code = body.get('error').get('code')
        self.assertEqual(source, 'entity')


class HourPaymentClientTest(TestCase):
    def setUp(self):
        self.user_db = UserORM.objects.create_user(
            username="TestUserDB",
            email='test_user@gmail.com',
            password='qwert12345'
        )

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

        data = json.dumps({
            "title": "Project 1",
            "description": "Test tests",
            "start_date": "2016-12-20T23:00:00.000000Z+0600",
            "end_date": "2018-12-20T12:30:00.000000Z+0600",
            "type_of_payment": "H_P",

        })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.post(reverse('create_project'), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.project_id = body.get('id')

        self.project_db = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user_id=body.get('user_id')

        )
        self.hour_payment_db = HourPaymentORM.objects.create(
            project_id=self.project_db.id,
            rate=500
        )

    def test_create_hour_payment(self):
        data = json.dumps({
            "rate": 500,
        })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.post(reverse('create_hour_payment', kwargs={'project_id': self.project_id,
                                                                           }
                                            ), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('project_id'), self.project_id)
        self.assertEqual(body.get('rate'), 500)

    def test_get_hour_payment(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.get(reverse('get_hour_payment', kwargs={'project_id': self.project_db.id,
                                                                       'hour_payment_id': self.hour_payment_db.id
                                                                       }
                                           ), content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('id'), self.hour_payment_db.id)
        self.assertEqual(body.get('project_id'), self.project_db.id)
        self.assertEqual(body.get('rate'), self.hour_payment_db.rate)

    def test_update_hour_payment(self):
        data = json.dumps({
            "rate": 300,
        })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.put(reverse('update_hour_payment', kwargs={'project_id': self.project_db.id,
                                                                          'hour_payment_id': self.hour_payment_db.id
                                                                          }
                                           ), data, content_type="application/json", **header)

        body = json.loads(response.content.decode())
        self.assertEqual(HourPaymentORM.objects.get(id=self.hour_payment_db.id).rate, 300)
        self.assertEqual(body.get('project_id'), self.project_db.id)
        self.assertEqual(body.get('rate'), 300)



    def test_delete_hour_payment(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.delete(reverse('delete_hour_payment', kwargs={'project_id': self.project_db.id,
                                                                             'hour_payment_id': self.hour_payment_db.id
                                                                             }
                                              ), content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('project_id'), self.project_db.id)
        self.assertEqual(body.get('rate'), 500)
        with self.assertRaises(HourPaymentORM.DoesNotExist):
            HourPaymentORM.objects.get(id=self.hour_payment_db.id)



    def test_get_all_hour_payment(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.get(reverse('get_all_hour_payment', kwargs={'project_id': self.project_db.id,                                                                       }
                                           ), content_type="application/json", **header)
        body = json.loads(response.content.decode())
        print(body)
        self.assertEqual(type(body), list)
        self.assertEqual(len(body), 1)
