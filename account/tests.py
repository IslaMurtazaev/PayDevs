from django.test import TestCase
from account.models import UserORM
from account.validators import *
from PayDevs.exceptions import InvalidEntityException

#----------------PASSWORD VALIDATORS TESTS------------------------------------#

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
        UserORM.objects.create(username="IslamIsTheBest", email="islam.muratazaev@gmail.com",\
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


#----------------EMAIL VALIDATORS TESTS-------------------------------------#



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


class EmailForbiddenEmailDomainsValidatorMetodTest(TestCase):


    def test_method_validate_type(self):
        self.assertEqual(None, EmailForbiddenEmailDomainsValidator().validate('exmaple@mail.ru'))
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
