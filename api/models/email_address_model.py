"""
tba
"""

import uuid
from django.db import models

from api.models.people_model import People


class EmailAddress(models.Model):
    """
    tba
    """

    person = models.OneToOneField(
        People,
        on_delete=models.CASCADE,
        primary_key=True
    )
    email_address_id = models.BigAutoField(
        primary_key=True
    )
    email_address = models.CharField(
        max_length=50,
        primary_key=True
    )
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.email_address}"

    class Meta:
        """
        tba
        """

        db_table = "email_addresses"
        managed = False
        verbose_name = "Email Address"
        verbose_name_plural = "Email Addresses"
        get_latest_by = "modified_date"
        unique_together = [
            "person",
            "email_address_id"
        ]
        ordering = ["email_address_id"]
        get_latest_by = "modified_date"
