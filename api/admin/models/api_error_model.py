"""
tba
"""
from django.db import models
from django.utils import timezone


class ApiError(models.Model):
    """
    Model to store API error events for observability and debugging.

    Attributes
    ----------
    code : str
        Short machine-readable error code (e.g., "not_found", "validation_error").
    detail : str
        Human-readable description of the error.
    attr : str
        Field or attribute associated with the error. Can be 'null' if not field-specific.
    error_type : str
        Type of error (e.g., "client_error", "validation_error", "server_error").
    path : str
        Request path where the error occurred.
    method : str
        HTTP method of the failed request.
    user : str
        Username or user ID if available (nullable).
    created_at : datetime
        Timestamp when the error was logged.
    """

    code = models.CharField(
        max_length=100,
        null="null"
    )
    detail = models.TextField(
        default="null"
    )
    attr = models.CharField(
        max_length=100,
        default="null"
    )
    error_type = models.CharField(
        max_length=50,
        default="client_error"
    )
    path = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    method = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    user = models.CharField(
        max_length=255,
        blank=True,
        null=True
        )
    created_at = models.DateTimeField(
        default=timezone.now
    )

    class Meta:
        """
        tba
        """
        db_table = "api_error"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.code}: {self.detail[:50]}"
