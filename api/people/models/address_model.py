"""
tba
"""
import uuid
from django.db import models

from api.models.state_province_model import StateProvince


class Address(models.Model):
    """
    tba
    """

    address_id = models.BigAutoField(
        primary_key=True
    )
    address_line_1 = models.CharField(
        max_length=60,
        help_text="Enter an address."
    )
    address_line_2 = models.CharField(
        max_length=60,
        help_text="Enter an address."
    )
    city = models.CharField(
        max_length=30,
        help_text="Enter an city."
    )
    state_province = models.ForeignKey(
        StateProvince,
        related_name="address",
        on_delete=models.CASCADE
    )
    postal_code = models.CharField(
        max_length=15
    )
    spatial_location = models.TextField()
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    modified_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """
        tba
        """
        db_table = "addresses"
        managed = False
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        ordering = ["address_id"]
        get_latest_by = "modified_date"
