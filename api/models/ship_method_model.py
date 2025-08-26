"""
tba
"""

import uuid
from django.db import models


class ShipMethod(models.Model):
    """
    tba
    """

    ship_method_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter a ship method."
    )
    ship_base = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    ship_rate = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        """
        tba
        """

        db_table = "ship_methods"
        managed = False
        verbose_name = "Ship Method"
        verbose_name_plural = "Ship Methods"
        ordering = ['ship_method_id']
        get_latest_by = 'modified_date'
