from PayDevs.exceptions import EntityDoesNotExistException, NoPermissionException, PayDevsException, \
    EntityIntegrityException, InvalidEntityException, NoLoggedException
from PayDevs.serializer import ExampleExceptionSerializer

exception_status_code = {
    EntityDoesNotExistException: 404,
    NoPermissionException: 403,
    EntityIntegrityException: 409,
    InvalidEntityException: 422,
    NoLoggedException: 401,
}


def serialize_exception(method):
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except PayDevsException as e:
            ExampleExceptionSerializer.model = e.__class__
            body = ExampleExceptionSerializer.serializer(e)
            status = exception_status_code[type(e)]
        return body, status

    return method_wrapper
