class ExampleException(Exception):

    def __init__(self, source, code, message):
        super().__init__(message)
        self._source = source
        self._code = code


    @property
    def source(self):
        return self._source

    @property
    def code(self):
         return self._code


class EntityDoesNotExistException(ExampleException):
    def __init__(self):
        super().__init__(source='entity', code='not_fond', message='Entity not font')


class SerializerException(ExampleException):
    def __init__(self, message):
        super().__init__(source='serializer', code='model_not', message=message)


class NoPermissionException(ExampleException):
    def __init__(self):
        super().__init__(source='permission', code='denied', message='Permission denied')