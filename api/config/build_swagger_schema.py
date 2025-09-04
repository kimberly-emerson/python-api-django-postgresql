"""
tba
"""
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import serializers

DEFAULT_SCHEMA_OPTIONS = {
    
}

DEFAULT_ERROR_RESPONSES = {
    400: OpenApiResponse(description='Bad Request: malformed request or validation failure.'),
    401: OpenApiResponse(description='Unauthorized: missing or invalid authentication.'),
    403: OpenApiResponse(description='Forbidden: authenticated but lacks permission.'),
    404: OpenApiResponse(description='Not Found: resource not found.'),
    405: OpenApiResponse(description='Method Not Allowed: HTTP method not supported.'),
    406: OpenApiResponse(description='Not Acceptable: server cannot produce content matching Accept header.'),
    415: OpenApiResponse(description='Unsupported Media Type: request Content-Type not supported.'),
    429: OpenApiResponse(description='Too Many Requests: rate limit exceeded.'),
    500: OpenApiResponse(description='Internal Server Error:  an unexpected condition on the server that prevented it from fulfilling the request.'),    
}


def build_schema_extension(
    *,
    model: str,
    operation_id: str,
    serializer: type[serializers.Serializer],
    success_code: int = 200,
    extra_responses: dict[int, OpenApiResponse] = None,
    request_serializer: type[serializers.Serializer] = None,
    tags: list[str] = None
):
    """
    Factory for generating a full extend_schema decorator for DRF endpoints.

    Args:
        operation_id (str): Unique identifier for OpenAPI operation.
        serializer (Serializer): Serializer class for successful response.
        success_code (int): HTTP status code for success.
        success_description (str): Description of success response.
        extra_responses (dict): Optional additional error responses.
        request_serializer (Serializer): Optional request body serializer.
        tags (list): Optional OpenAPI tags.
        summary (str): Optional short summary.
        description (str): Optional long-form description.

    Returns:
        extend_schema: Decorator for DRF endpoint.
    """
    summary, description, success_description = build_resource_options(model, operation_id)

    success_response = {
        success_code: OpenApiResponse(response=serializer, description=success_description)
    }
    error_responses = {**DEFAULT_ERROR_RESPONSES, **(extra_responses or {})}
    all_responses = {**success_response, **error_responses}

    return extend_schema(
        operation_id=operation_id,
        responses=all_responses,
        request=request_serializer,
        tags=tags,
        summary=summary,
        description=description
    )


def build_resource_options(resource, operation_id):
    """
    tba
    """
    summary = None
    description = None
    success_description = None

    match operation_id:
        case "list":
            summary = f"Retrieve all {resource} resources.",
            description = f"Returns a paginated list of {resource} resources.",
            success_description = f"List of {resource} resources returned successfully."
        case "retrieve":
            summary = f"Retrieve a single {resource} resource.",
            description = f"Returns {resource} record by ID. Raises 404 if not found.",
            success_description = f"{resource} resource retrieved successfully."
        case "create":
            summary = f"Create a new {resource} resource.",
            description = f"Accepts validated input and persists a new {resource} record. Returns created {resource} object.",
            success_description = f"{resource} resource created successfully."
        case "update":
            summary = f"Fully updates an existing {resource} resource.",
            description = f"Accepts validated input and updates {resource} record. Returns updated {resource} object.",
            success_description = f"{resource} resource updated successfully."
        case "partial_update":
            summary = f"Partially updates an existing {resource} resource.",
            description = f"Accepts validated input and partially updates {resource} record. Returns updated {resource} object.",
            success_description = f"{resource} resource updated successfully."
        case "destroy":
            summary = f"Deletes {resource} record for the provided ID.",
            description = f"Deletes {resource} resource by ID. Raises 404 if not found.",
            success_description = f"{resource} resource deleted successfully."

    return summary, description, success_description
