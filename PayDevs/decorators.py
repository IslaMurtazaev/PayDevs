from PayDevs.exceptions import PayDevsException
from PayDevs.serializers import ExceptionSerializer
from PayDevs.constants import exception_status_codes





def serialize_exception(method):
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except PayDevsException as e:
            ExceptionSerializer.model = e.__class__
            body = ExceptionSerializer.serialize(e)
            try:
                status = exception_status_codes[type(e)]
            except KeyError:
                raise e
        return body, status

    return method_wrapper
