"""
tba
"""
from django.db import models


class ApiError(models.Model):
    """
    tba
    """

    description = models.CharField(
        max_length=255
    )
    schema = models.TextField(
        max_length=255
    )
    example = models.TextField()

    class Meta:
        """
        tba
        """

        verbose_name = "Api Error"
        verbose_name_plural = "Api Errors"
