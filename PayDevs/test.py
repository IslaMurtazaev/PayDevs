from django.test import TestCase

from PayDevs.exceptions import SerializerException
from PayDevs.serializer import BaseSerializer


class SerializerTest(TestCase):
    def setUp(self):
        class ExampleModel(object):
            attr1 = 2
            attr2 = 100
            attr3 = 5
            name = "ExampleClass"

        self.model = ExampleModel

    def test_baserializer_method_serializer_fields__all__(self):
        dict_test = {
            'attr1': 2,
            'attr2': 100,
            'attr3': 5,
            'name': "ExampleClass"
        }

        class TestSerializer(BaseSerializer):
            model = self.model
            fields = '__all__'

        self.assertDictEqual(TestSerializer.serializer(self.model()), dict_test)

    def test_baserializer_method_serializer_fields_list(self):
        dict_test = {
            'attr1': 2,
            'name': "ExampleClass"
        }

        class TestSerializer(BaseSerializer):
            model = self.model
            fields = ['attr1', 'name']

        self.assertDictEqual(TestSerializer.serializer(self.model()), dict_test)

    def test_baserializer_method_serializer_exception(self):
        dict_test = {
            'attr1': 2,
            'name': "ExampleClass"
        }

        class TestSerializer(BaseSerializer):
            model = self.model
            fields = ['attr1', 'name', 'attr4']

        with self.assertRaises(SerializerException):
            TestSerializer.serializer(self.model())
        try:
            TestSerializer.serializer(self.model())
        except SerializerException as e:
            self.assertRegex(str(e), 'attr4')
