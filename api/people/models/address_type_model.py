"""
tba
"""

import uuid
from django.db import models


class AddressTypeManager(models.Manager):
    """
    tba
    """


class AddressType(models.Model):
    """
    tba
    """

    address_type_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter an address type."
    )
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    objects = AddressTypeManager()

    class Meta:
        """
        tba
        """

        db_table = "address_types"
        managed = False
        verbose_name = "Address Type"
        verbose_name_plural = "Address Types"
        ordering = ["address_type_id"]
        get_latest_by = "modified_date"
