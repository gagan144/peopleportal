from django.http import JsonResponse
from django.core.exceptions import ValidationError


class ApiResponse:
    """
    A class to create a http json response mostly used to for API/AJAX requests.

    The content of the response is as follows:

        >>> { "status_code": <int http code>, "status": "<status>", "message":"<message">, ... }
    """

    # --- enums ---
    ST_SUCCESS = 'success'
    ST_PARTIAL_SUCCESS = 'partial_success'
    ST_IGNORED = 'ignored'  # No update or change
    ST_FAILED = 'failed'  # Operation failed
    ST_NOT_ALLOWED = 'not_allowed'  # GET or POST not allowed
    ST_FORBIDDEN = 'forbidden'  # Access is not allowed or prohibited
    ST_UNAUTHORIZED = 'unauthorized '  # Authentication fails
    ST_BAD_REQUEST = 'bad_request'  # Bad request formation/Invalid or missing parameteres
    ST_SERVER_ERROR = 'server_error'  # Any internal server error

    CH_STATUS = (
        (ST_SUCCESS, 'Success'),
        (ST_PARTIAL_SUCCESS, 'Partial success'),
        (ST_IGNORED, 'Ignored'),
        (ST_FAILED, 'Failed'),
        (ST_NOT_ALLOWED, 'Not Allowed'),
        (ST_FORBIDDEN, 'Forbidden'),
        (ST_UNAUTHORIZED, 'Unauthorized'),
        (ST_BAD_REQUEST, 'Bad request'),
        (ST_SERVER_ERROR, 'Server error'),
    )

    STATUS_CODES = {
        ST_SUCCESS: 200,
        ST_PARTIAL_SUCCESS: 206,
        ST_IGNORED: 204,
        ST_FAILED: 299,
        ST_NOT_ALLOWED: 405,
        ST_FORBIDDEN: 403,
        ST_UNAUTHORIZED: 401,
        ST_BAD_REQUEST: 400,
        ST_SERVER_ERROR: 500
    }

    @staticmethod
    def http(status, message, **kwargs):
        if status not in ApiResponse.STATUS_CODES:
            raise ValidationError("Invalid api response status '{}'.".format(status))

        status_code = ApiResponse.STATUS_CODES[status]

        data = {
            "status": status,
            "status_code": status_code,
            "message": message,
        }
        data.update(kwargs)

        return JsonResponse(data, status=status_code)