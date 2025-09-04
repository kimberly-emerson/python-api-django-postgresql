"""
tba
"""
import logging
from rest_framework.views import exception_handler as drf_exception_handler

from api.admin.models.api_error_model import ApiError
from api.utils.logging_handler import log_event

logger = logging.getLogger(__name__)


def custom_exception_handler(exception, context):
    """
    Exception handler that logs errors into ApiError model.

    Parameters
    ----------
    exception : Exception
        The exception raised.
    context : dict
        Additional context including the request.

    Returns
    -------
    Response
        Standardized DRF response with error details.
    """
    # generate response
    response = drf_exception_handler(exception, context)

    # log on exception
    if response is not None:
        request = context.get("request")

        # get values
        user = getattr(request.user, "username", None) if request else None
        path = request.path if request else ""
        method = request.method if request else ""

        # set values
        detail = response.data.get("detail", str(exception))
        code = getattr(exception, "default_code", "error")
        error_type = (
            "server_error" if response.status_code >= 500 else "client_error"
        )
        # save to database
        # pylint: disable=no-member
        ApiError.objects.create(
            code=code,
            detail=detail,
            attr="null",  # could be extended with field-level info
            error_type=error_type,
            path=path,
            method=method,
            user=user,
        )

        log_event(
            "ERROR",
            f"{code}: {detail}",
            user=user,
            method=method,
            path=request.get_full_path()
        )

    return response
