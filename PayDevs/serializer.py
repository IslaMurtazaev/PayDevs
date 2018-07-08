import inspect

from PayDevs.exceptions import SerializerException, PayDevsException, EntityDoesNotExistException


class BaseSerializer(object):
    fields = None
    model = None

    @classmethod
    def serializer(cls, obj):
        if cls.model is not obj.__class__:
            raise SerializerException('the obj argument must be an instance of the class model')
        result = dict()
        attributes = inspect.getmembers(cls.model)
        # attributes = inspect.getmembers(MyClass, lambda a:not(inspect.isroutine(a)))
        if cls.fields == '__all__':
            for a in attributes:
                if not (a[0].startswith('__') and a[0].endswith('__')):
                    result[a[0]] = getattr(obj, a[0])

        else:
            fields = set(cls.fields)
            attr_set = set([a[0] for a in attributes])
            diff_attr = fields.difference(attr_set)
            if diff_attr:
                raise SerializerException('Class {0} does not have the '
                                          'attribute {1}'.format(cls.model.__name__, list(diff_attr)[0]))
            for a in attributes:
                if not (a[0].startswith('__') and a[0].endswith('__')) and (a[0] in fields):
                    result[a[0]] = getattr(obj, a[0])

        return result



class ListSerializer(BaseSerializer):

    @classmethod
    def serializer(cls, list_obj):
        result = list()
        for obj in list_obj:
            result.append(super().serializer(obj))
        return result


class ExampleExceptionSerializer(BaseSerializer):
    model = PayDevsException
    fields = ['source', 'code']

    @classmethod
    def serializer(cls, exception):
        ser = super().serializer(exception)
        ser['message'] = str(exception)
        body = {
            'error': ser
        }
        return body


# class ExampleExceptionSerializer(object):
#     @staticmethod
#     def serialize(exception):
#         result = {
#             'source': exception.source,
#             'code': exception.code,
#             'message': str(exception),
#         }
#         return result
