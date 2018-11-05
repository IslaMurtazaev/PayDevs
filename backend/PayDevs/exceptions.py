class PayDevsException(Exception):
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


class InvalidEntityException(PayDevsException):
    pass


class EntityDoesNotExistException(PayDevsException):
    def __init__(self):
        super().__init__(source='entity', code='not_found', message='Entity not found')


class NoLoggedException(PayDevsException):
    def __init__(self):
        super().__init__(source='authentication', code='required', message='Authentication required')



class SerializerException(PayDevsException):
    def __init__(self, message):
        super().__init__(source='serializer', code='model_not', message=message)


class NoPermissionException(PayDevsException):
    def __init__(self, message='Permission denied'):
        super().__init__(source='permission', code='denied', message=message)


class EntityIntegrityException(PayDevsException):
    def __init__(self, username):
        super().__init__(source='entity', code='user_already_exists', message="User already username: "
                                               "'%s' already exists" % username)
