from django.test import TestCase

from account.models import UserORM


class LoginUserInteractorTest(TestCase):
    def setUp(self):
        self.user = UserORM.objects.create(
            username="testUser",
            email="test@gmail.com",
            password='qwert12345'
        )


    