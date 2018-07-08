from example_paydevs.exceptions import EntityDoesNotExistException, NoPermissionException, ExampleException
from example_paydevs.serializer import ExampleExceptionSerializer

exception_status_code = {
    EntityDoesNotExistException: 404,
    NoPermissionException: 403
}


def serialize_exception(method):
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except ExampleException as e:
            ExampleExceptionSerializer.model = e.__class__
            body = ExampleExceptionSerializer.serializer(e)
            status = exception_status_code[type(e)]
        return body, status

    return method_wrapper
