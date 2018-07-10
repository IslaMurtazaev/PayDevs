from django.test import TestCase

from account.validators import EmailAtValidators, EmailForbiddenEmailDomainsValidator
from PayDevs.exceptions import InvalidEntityException


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