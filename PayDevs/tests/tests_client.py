import datetime

from django.test import TestCase, Client
from django.urls import reverse
import json

from PayDevs.constants import DATE_TIME_FORMAT
from account.models import UserORM
from project.models import HourPaymentORM, ProjectORM, WorkTimeORM, MonthPaymentORM, WorkedDayORM



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
            "start_date": "2016-12-20T23:00:00.000Z",
            "end_date": "2018-12-20T12:30:00.000Z",
            "type_of_payment": "H_P",

        })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.post(reverse('create_project'), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.project_id = body.get('id')

    def test_client_get_project(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.get(reverse('get_project', kwargs={'project_id': self.project_id}),
                                   content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('title'), "Project 1")
        self.assertEqual(body.get('description'), "Test tests")
        self.assertEqual(body.get('status'), True)

    def test_client_get_project_not_entity_error(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.get(reverse('get_project', kwargs={'project_id': 20000}),
                                   content_type="application/json", **header)
        body = json.loads(response.content.decode())
        code = body.get('error').get('code')
        source = body.get('error').get('source')
        message = body.get('error').get('message')
        self.assertEqual(code, 'not_found')
        self.assertEqual(source, 'entity')
        self.assertEqual(message, 'Entity not found')

    def test_create_project(self):
        data = json.dumps({
            "title": "Project web",
            "description": "logic web site",
            "start_date": "2016-12-20T23:00:00.000Z",
            "end_date": "2018-12-20T12:30:00.000Z",
            "type_of_payment": "H_P",

        })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.put(reverse('create_project'), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('title'), 'Project web')
        self.assertEqual(body.get('description'), 'logic web site')
        self.assertEqual(body.get('start_date'), '2016-12-20T23:00:00.000000Z')
        self.assertEqual(body.get('end_date'), '2018-12-20T12:30:00.000000Z')
        self.assertEqual(body.get('status'), True)


    def test_create_no_logged_error_project(self):
        data = json.dumps({
            "title": "Project web",
            "description": "logic web site",
            "start_date": "2016-12-20T23:00:00.000Z",
            "end_date": "2018-12-20T12:30:00.000Z",
            "type_of_payment": "H_P",

        })
        header = {'HTTP_AUTHORIZATION': None}
        response = self.client.put(reverse('create_project'), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        code = body.get('error').get('code')
        source = body.get('error').get('source')
        message = body.get('error').get('message')
        self.assertEqual(code, 'required')
        self.assertEqual(source, 'authentication')
        self.assertEqual(message, 'Authentication required')

    def test_update_project(self):
        data = json.dumps({
            "title": "Project web",
            "description": "logic web site Test update",
            "end_date": "2018-11-20T12:30:00.000Z",
            "status": True

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
            "start_date": "2016-12-20T23:00:00.000Z",
            "end_date": "2018-12-20T12:30:00.000Z",
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


    def test_create_hour_payment_no_logged_error(self):
        data = json.dumps({
            "rate": 500,
        })
        header = {'HTTP_AUTHORIZATION': None}
        response = self.client.post(reverse('create_hour_payment', kwargs={'project_id': self.project_id,
                                                                           }
                                            ), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        code = body.get('error').get('code')
        source = body.get('error').get('source')
        message = body.get('error').get('message')
        self.assertEqual(code, 'required')
        self.assertEqual(source, 'authentication')
        self.assertEqual(message, 'Authentication required')

    def test_get_hour_payment(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.get(reverse('get_hour_payment', kwargs={'hour_payment_id': self.hour_payment_db.id}
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
        response = self.client.delete(reverse('delete_hour_payment', kwargs={'hour_payment_id': self.hour_payment_db.id}
                                              ), content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('project_id'), self.project_db.id)
        self.assertEqual(body.get('rate'), 500)
        with self.assertRaises(HourPaymentORM.DoesNotExist):
            HourPaymentORM.objects.get(id=self.hour_payment_db.id)

    def test_get_all_hour_payment(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.get(reverse('get_all_hour_payments', kwargs={'project_id': self.project_db.id}
                                           ), content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(type(body), list)
        self.assertEqual(len(body), 1)



class WorkTimeClientTest(TestCase):
    def setUp(self):
        self.user_db = UserORM.objects.create_user(
            username="TestUser",
            email='test_user@gmail.com',
            password='qwert12345'
        )
        self.project_db = ProjectORM.objects.create(
            title='Test Project',
            description='My Test project',
            type_of_payment='T_P',
            start_date=datetime.datetime.now(),
            user=self.user_db

        )
        self.hour_payment_db = HourPaymentORM.objects.create(
            project_id=self.project_db.id,
            rate=500
        )
        self.work_time_db = WorkTimeORM.objects.create(
            hour_payment_id=self.hour_payment_db.id,
            start_work=datetime.datetime.strptime("2018-07-20T10:00:00.000Z", DATE_TIME_FORMAT),
            end_work=datetime.datetime.strptime("2018-07-20T18:30:00.000Z", DATE_TIME_FORMAT),
            paid=False,
        )
        data = json.dumps({'username': 'TestUser',
                           'password': 'qwert12345'})
        response = self.client.post(reverse('login_user'), data, content_type="application/json")
        body = json.loads(response.content.decode())
        self.token = body.get('token')

    def test_create_work_time(self):
        data = json.dumps({
            "start_work": "2018-12-20T10:00:00.000Z",
            "end_work": "2018-12-20T18:30:00.000Z",
            "paid": False,
        })
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.post(reverse('create_work_time', kwargs={'project_id': self.project_db.id,
                                                                        'hour_payment_id': self.hour_payment_db.id
                                                                        }
                                            ), data, content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('hour_payment_id'), self.hour_payment_db.id)
        self.assertEqual(body.get('paid'), False)
        self.assertEqual(body.get('start_work'), "2018-12-20T10:00:00.000000Z")
        self.assertEqual(body.get('end_work'), "2018-12-20T18:30:00.000000Z")

    def test_get_work_time(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        response = self.client.get(reverse('get_work_time', kwargs={'work_time_id': self.work_time_db.id}
                                           ), content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(body.get('hour_payment_id'), self.hour_payment_db.id)
        self.assertEqual(body.get('paid'), False)
        self.assertEqual(body.get('start_work'), "2018-07-20T10:00:00.000000Z")
        self.assertEqual(body.get('end_work'), "2018-07-20T18:30:00.000000Z")

    def test_update_create_work_time(self):
        data = json.dumps({
            "paid": True,
        })
        header = {'HTTP_AUTHORIZATION': self.token}
        old_work_time = WorkTimeORM.objects.get(id=self.work_time_db.id)
        response = self.client.put(reverse('update_work_time', kwargs={'project_id': self.project_db.id,
                                                                       'hour_payment_id': self.hour_payment_db.id,
                                                                       'work_time_id': self.work_time_db.id
                                                                       }
                                           ), data, content_type="application/json", **header)

        body = json.loads(response.content.decode())
        new_work_time = WorkTimeORM.objects.get(id=self.work_time_db.id)

        self.assertEqual(old_work_time.paid, False)
        self.assertEqual(body.get('hour_payment_id'), self.hour_payment_db.id)
        self.assertEqual(body.get('paid'), True)
        self.assertEqual(new_work_time.paid, True)

    def test_delete_work_time(self):
        header = {'HTTP_AUTHORIZATION': self.token}
        self.assertIsNotNone(WorkTimeORM.objects.get(id=self.work_time_db.id))
        response = self.client.delete(reverse('delete_work_time', kwargs={'work_time_id': self.work_time_db.id}
                                              ), content_type="application/json", **header)
        body = json.loads(response.content.decode())
        with self.assertRaises(WorkTimeORM.DoesNotExist):
            WorkTimeORM.objects.get(id=self.work_time_db.id)


    def test_get_all_work_time(self):
        header = {'HTTP_AUTHORIZATION': self.token}

        response = self.client.get(reverse('get_all_work_time', kwargs={'hour_payment_id': self.hour_payment_db.id}
                                           ), content_type="application/json", **header)
        body = json.loads(response.content.decode())
        self.assertEqual(type(body), list)
        self.assertEqual(len(body), 1)




class MonthPaymentClientTest(TestCase):
    def setUp(self):
        self.client = Client()

        db_user = UserORM.objects.create_user(
            username='IslaMurtazaev',
            password='alohamora',
            email='islam.murtazaev@hogwarts.edu.co.uk'
        )

        data = json.dumps({'username': 'IslaMurtazaev',
                           'password': 'alohamora'})
        response = self.client.post(reverse('login_user'), data, content_type="application/json")
        body = json.loads(response.content.decode())
        self.token = body.get('token')


        self.db_project = ProjectORM.objects.create(
            title="Dumbledore's Army",
            user_id=db_user.id,
            description="Defense against Dark Arts club",
            type_of_payment="T_P",
            start_date=datetime.datetime.now()
        )

        self.db_month_payment = MonthPaymentORM.objects.create(project_id=self.db_project.id, rate=120)


        db_user2 = UserORM.objects.create_user(
            username='You-know-who',
            password='avadakadabra',
            email='voldemort@snakemail.com'
        )

        self.db_project2 = ProjectORM.objects.create(
            title="Horcruxes",
            user_id=db_user2.id,
            description="Hidden fragment of Dark wizard soul",
            type_of_payment="T_P",
            start_date=datetime.datetime.now()
        )

        data = json.dumps({'username': 'You-know-who',
                           'password': 'avadakadabra'})
        response = self.client.post(reverse('login_user'), data, content_type="application/json")
        body = json.loads(response.content.decode())
        self.token2 = body.get('token')


    def test_create_month_payment(self):
        url_params = {
            'project_id': self.db_project.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        data = json.dumps({
            'rate': 150,
            'non_existent_attr': 'SPAM'
        })

        response = self.client.post(reverse('create_month_payment', kwargs=url_params), data,
                                    content_type='application/json', **headers)

        body = json.loads(response.content.decode())
        created_month_payment = MonthPaymentORM.objects.get(id=body.get('id'))

        self.assertEqual(created_month_payment.id, body.get('id'))
        self.assertEqual(created_month_payment.project_id, body.get('project_id'))
        self.assertEqual(created_month_payment.rate, body.get('rate'))
        self.assertIsNone(body.get('non_existent_attr'))


        response = self.client.post(reverse('create_month_payment', kwargs=url_params), data,
                                    content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())

        error = body.get('error')
        self.assertIsNotNone(error)
        self.assertEqual(error.get('code'), 'denied')
        self.assertEqual(error.get('source'), 'permission')
        self.assertEqual(error.get('message'), 'Permission denied')


        response = self.client.post(reverse('create_month_payment', kwargs=url_params), data,
                                    content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())

        error = body.get('error')
        self.assertIsNotNone(error)
        self.assertEqual(error.get('code'), 'denied')
        self.assertEqual(error.get('source'), 'permission')
        self.assertEqual(error.get('message'), 'Permission denied')


    def test_get_month_payment(self):
        url_params = {
            'month_payment_id': self.db_month_payment.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        response = self.client.get(reverse('get_month_payment', kwargs=url_params), **headers)

        body = json.loads(response.content.decode())

        self.assertEqual(self.db_month_payment.id, body.get('id'))
        self.assertEqual(self.db_month_payment.project_id, body.get('project_id'))
        self.assertEqual(self.db_month_payment.rate, body.get('rate'))


        response = self.client.get(reverse('get_month_payment', kwargs=url_params),
                                   content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())

        error = body.get('error')
        self.assertIsNone(error)


    def test_update_month_payment(self):
        url_params = {
            'project_id': self.db_project.id,
            'month_payment_id': self.db_month_payment.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        data = json.dumps({
            'rate': 200,
            'non_existent_attr': 'SPAM'
        })

        response = self.client.put(reverse('update_month_payment', kwargs=url_params), data,
                                   content_type='application/json', **headers)

        body = json.loads(response.content.decode())

        self.assertEqual(self.db_month_payment.id, body.get('id'))
        self.assertEqual(self.db_month_payment.project_id, body.get('project_id'))
        self.assertEqual(200, body.get('rate'))
        self.assertIsNone(body.get('non_existent_attr'))


        response = self.client.put(reverse('update_month_payment', kwargs=url_params), data,
                                   content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())

        error = body.get('error')
        self.assertIsNotNone(error)
        self.assertEqual(error.get('code'), 'denied')
        self.assertEqual(error.get('source'), 'permission')
        self.assertEqual(error.get('message'), 'Permission denied')


        response = self.client.put(reverse('update_month_payment', kwargs={'project_id': self.db_project2.id,
            'month_payment_id': self.db_month_payment.id}), data, content_type='application/json', **headers)
        body = json.loads(response.content.decode())

        error = body.get('error')
        self.assertIsNotNone(error)
        self.assertEqual(error.get('code'), 'denied')
        self.assertEqual(error.get('source'), 'permission')
        self.assertEqual(error.get('message'), 'Permission denied')


    def test_delete_month_payment(self):
        url_params = {
            'month_payment_id': self.db_month_payment.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        deleted_month_payment = self.db_month_payment

        response = self.client.delete(reverse('delete_month_payment', kwargs=url_params),
                                      content_type='application/json', **headers)
        body = json.loads(response.content.decode())

        self.assertEqual(deleted_month_payment.id, body.get('id'))
        self.assertEqual(deleted_month_payment.project_id, body.get('project_id'))
        self.assertEqual(deleted_month_payment.rate, body.get('rate'))

        with self.assertRaises(MonthPaymentORM.DoesNotExist):
            MonthPaymentORM.objects.get(id=deleted_month_payment.id)


        response = self.client.delete(reverse('delete_month_payment', kwargs=url_params),
                                      content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())
        error = body.get('error')
        self.assertIsNotNone(error)
        self.assertEqual(error.get('code'), 'not_found')
        self.assertEqual(error.get('source'), 'entity')
        self.assertEqual(error.get('message'), 'Entity not found')




    def test_get_all_month_payments(self):
        url_params = {
            'project_id': self.db_project.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        response = self.client.get(reverse('get_all_month_payments', kwargs=url_params),
                                   content_type='application/json', **headers)
        body = json.loads(response.content.decode())

        self.assertTrue(isinstance(body, list))
        self.assertEqual(len(body), 1)
        self.assertEqual(body[0].get('id'), self.db_month_payment.id)
        self.assertEqual(body[0].get('project_id'), self.db_month_payment.project_id)
        self.assertEqual(body[0].get('rate'), self.db_month_payment.rate)


        response = self.client.get(reverse('get_all_month_payments', kwargs=url_params),
                                   content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())
        self.assertTrue(isinstance(body, list))
        self.assertEqual(len(body), 1)
        self.assertEqual(body[0].get('id'), self.db_month_payment.id)
        self.assertEqual(body[0].get('project_id'), self.db_month_payment.project_id)
        self.assertEqual(body[0].get('rate'), self.db_month_payment.rate)



class WorkedDayClientTest(TestCase):
    def setUp(self):
        self.client = Client()

        db_user = UserORM.objects.create_user(
            username='IslaMurtazaev',
            password='alohamora',
            email='islam.murtazaev@hogwarts.edu.co.uk'
        )

        data = json.dumps({'username': 'IslaMurtazaev',
                           'password': 'alohamora'})
        response = self.client.post(reverse('login_user'), data, content_type="application/json")
        body = json.loads(response.content.decode())
        self.token = body.get('token')

        self.db_project = ProjectORM.objects.create(
            title="Dumbledore's Army",
            user_id=db_user.id,
            description="Defense against Dark Arts club",
            type_of_payment="T_P",
            start_date=datetime.datetime.now()
        )

        self.db_month_payment = MonthPaymentORM.objects.create(project_id=self.db_project.id, rate=120)

        self.db_worked_day = WorkedDayORM.objects.create(month_payment_id=self.db_month_payment.id,
                                                         day=datetime.datetime.today().date())

        db_user2 = UserORM.objects.create_user(
            username='You-know-who',
            password='avadakadabra',
            email='voldemort@snakemail.com'
        )

        self.db_project2 = ProjectORM.objects.create(
            title="Horcruxes",
            user_id=db_user2.id,
            description="Hidden fragment of Dark wizard soul",
            type_of_payment="T_P",
            start_date=datetime.datetime.now()
        )

        data = json.dumps({'username': 'You-know-who',
                           'password': 'avadakadabra'})
        response = self.client.post(reverse('login_user'), data, content_type="application/json")
        body = json.loads(response.content.decode())
        self.token2 = body.get('token')



    def test_create_worked_day(self):
        url_params = {
            'project_id': self.db_project.id,
            'month_payment_id': self.db_month_payment.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        data = json.dumps({
            'day': "2018-07-26",
            'paid': False,
            'non_existent_attr': 'SPAM'
        })

        response = self.client.post(reverse('create_worked_day', kwargs=url_params), data,
                                    content_type='application/json', **headers)

        body = json.loads(response.content.decode())
        created_worked_day = WorkedDayORM.objects.get(id=body.get('id'))

        self.assertEqual(created_worked_day.id, body.get('id'))
        self.assertEqual(created_worked_day.month_payment_id, body.get('month_payment_id'))
        self.assertEqual(created_worked_day.day, datetime.datetime.strptime(body.get('day'), '%Y-%m-%d').date())
        self.assertIsNone(body.get('non_existent_attr'))


        response = self.client.post(reverse('create_worked_day', kwargs=url_params), data,
                                    content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())

        error = body.get('error')
        self.assertIsNotNone(error)
        self.assertEqual(error.get('code'), 'denied')
        self.assertEqual(error.get('source'), 'permission')
        self.assertEqual(error.get('message'), 'Permission denied')


    def test_get_worked_day(self):
        url_params = {
            'worked_day_id': self.db_worked_day.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        response = self.client.get(reverse('get_worked_day', kwargs=url_params), **headers)

        body = json.loads(response.content.decode())

        self.assertEqual(self.db_worked_day.id, body.get('id'))
        self.assertEqual(self.db_worked_day.month_payment_id, body.get('month_payment_id'))
        self.assertEqual(self.db_worked_day.day, datetime.datetime.strptime(body.get('day'), '%Y-%m-%d').date())

        response = self.client.get(reverse('get_worked_day', kwargs=url_params),
                                   content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())

        error = body.get('error')
        self.assertIsNone(error)



    def test_update_worked_day(self):
        url_params = {
            'project_id': self.db_project.id,
            'month_payment_id': self.db_month_payment.id,
            'worked_day_id': self.db_worked_day.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        data = json.dumps({
            'day': "1999-08-02",
            'non_existent_attr': 'SPAM'
        })

        response = self.client.put(reverse('update_worked_day', kwargs=url_params), data,
                                   content_type='application/json', **headers)

        body = json.loads(response.content.decode())

        self.assertEqual(self.db_worked_day.id, body.get('id'))
        self.assertEqual(self.db_worked_day.month_payment_id, body.get('month_payment_id'))
        self.assertEqual('1999-08-02', body.get('day'))
        self.assertIsNone(body.get('non_existent_attr'))

        response = self.client.put(reverse('update_worked_day', kwargs=url_params), data,
                                   content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())

        error = body.get('error')
        self.assertIsNotNone(error)
        self.assertEqual(error.get('code'), 'denied')
        self.assertEqual(error.get('source'), 'permission')
        self.assertEqual(error.get('message'), 'Permission denied')

        response = self.client.put(reverse('update_worked_day', kwargs={'project_id': self.db_project2.id,
            'month_payment_id': self.db_month_payment.id, 'worked_day_id': self.db_worked_day.id}),
                                   data, content_type='application/json', **headers)
        body = json.loads(response.content.decode())

        error = body.get('error')
        self.assertIsNotNone(error)
        self.assertEqual(error.get('code'), 'denied')
        self.assertEqual(error.get('source'), 'permission')
        self.assertEqual(error.get('message'), 'Permission denied')


    def test_delete_worked_day(self):
        url_params = {
            'worked_day_id': self.db_worked_day.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        deleted_worked_day = self.db_worked_day

        response = self.client.delete(reverse('delete_worked_day', kwargs=url_params),
                                      content_type='application/json', **headers)
        body = json.loads(response.content.decode())

        self.assertEqual(deleted_worked_day.id, body.get('id'))
        self.assertEqual(deleted_worked_day.month_payment_id, body.get('month_payment_id'))
        self.assertEqual(self.db_worked_day.day, datetime.datetime.strptime(body.get('day'), '%Y-%m-%d').date())


        with self.assertRaises(WorkedDayORM.DoesNotExist):
            WorkedDayORM.objects.get(id=deleted_worked_day.id)


    def test_get_all_worked_days(self):
        url_params = {
            'month_payment_id': self.db_month_payment.id
        }

        headers = {
            'HTTP_AUTHORIZATION': self.token
        }

        response = self.client.get(reverse('get_all_worked_days', kwargs=url_params),
                                   content_type='application/json', **headers)
        body = json.loads(response.content.decode())

        self.assertTrue(isinstance(body, list))
        self.assertEqual(len(body), 1)
        self.assertEqual(body[0].get('id'), self.db_worked_day.id)
        self.assertEqual(body[0].get('month_payment_id'), self.db_worked_day.month_payment_id)
        self.assertEqual(datetime.datetime.strptime(body[0].get('day'), '%Y-%m-%d').date(), self.db_worked_day.day)

        response = self.client.get(reverse('get_all_worked_days', kwargs=url_params),
                                   content_type='application/json', **{'HTTP_AUTHORIZATION': self.token2})
        body = json.loads(response.content.decode())
        self.assertTrue(isinstance(body, list))
        self.assertEqual(len(body), 1)
        self.assertEqual(body[0].get('id'), self.db_worked_day.id)
        self.assertEqual(body[0].get('month_payment_id'), self.db_worked_day.month_payment_id)
        self.assertEqual(datetime.datetime.strptime(body[0].get('day'), '%Y-%m-%d').date(),
                         self.db_worked_day.day)
