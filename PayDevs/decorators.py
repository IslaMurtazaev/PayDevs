import json

from django.http import HttpResponse

from PayDevs.exceptions import PayDevsException
from PayDevs.serializers import ExceptionSerializer
from PayDevs.constants import exception_status_codes





def serialize_exception(method):
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except PayDevsException as e:
            ExceptionSerializer.model = e.__class__
            try:
                status = exception_status_codes[type(e)]
            except KeyError:
                raise e
            body = ExceptionSerializer.serialize(e)
        return body, status

    return method_wrapper



def json_exception(method):
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except json.JSONDecodeError as e:
            body = {
                'error': {
                        'source': 'json',
                        'code': 'json_error',
                        'message': str(e)
                    }
                }
            status = 400

        except Exception as e:
            raise e
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    return method_wrapper
