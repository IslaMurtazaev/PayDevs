from enum import IntEnum, unique


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
