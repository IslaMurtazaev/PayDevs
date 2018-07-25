from PayDevs.exceptions import PayDevsException
from PayDevs.serializer import ExceptionSerializer
from PayDevs.constants import exception_status_codes





def serialize_exception(method):
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except PayDevsException as e:
            ExceptionSerializer.model = e.__class__
            body = ExceptionSerializer.serialize(e)
            status = exception_status_codes[type(e)]
        return body, status

    return method_wrapper
