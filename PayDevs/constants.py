from enum import IntEnum, unique

from PayDevs.exceptions import EntityDoesNotExistException, NoPermissionException, PayDevsException, \
    EntityIntegrityException, InvalidEntityException, NoLoggedException, SerializerException


DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ%z"
DATE_FORMAT = "%Y-%m-%d"


@unique
class StatusCodes(IntEnum):
    CONTINUE = 100
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    REDIRECT = 303
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    SERVER_ERROR = 500




exception_status_codes = {
    EntityDoesNotExistException: 404,
    NoPermissionException: 403,
    EntityIntegrityException: 409,
    InvalidEntityException: 422,
    NoLoggedException: 401,
    SerializerException: 500
}
