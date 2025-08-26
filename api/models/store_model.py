"""
tba
"""

import uuid
from django.db import models

from api.models.sales_people_model import SalesPeople


class Store(models.Model):
    """
    tba
    """

    store_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter a ship method."
    )
    sales_person = models.ForeignKey(
        SalesPeople,
        related_name='stores',
        verbose_name='Sales Person',
        on_delete=models.CASCADE
    )
    demographics = models.TextField()
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

        db_table = "stores"
        managed = False
        verbose_name = "Store"
        verbose_name_plural = "Stores"
        ordering = ['store_id']
        get_latest_by = 'modified_date'
