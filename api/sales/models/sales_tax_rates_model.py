"""
tba
"""
import uuid
from django.db import models

from api.models.state_province_model import StateProvince


class SalesTaxRates(models.Model):
    """
    tba
    """

    sales_tax_rate_id = models.BigAutoField(
        primary_key=True
    )
    state_province_id = models.ForeignKey(
        StateProvince,
        related_name='sales_tax_rates',
        verbose_name='State Province',
        on_delete=models.CASCADE
    )
    tax_type = models.PositiveSmallIntegerField()
    tax_rate = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    name = models.CharField(
        max_length=255,
        unique=True
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
        db_table = 'sales_tax_rates'
        managed = False
        verbose_name = 'Sales Tax Rate'
        verbose_name_plural = 'Sales Tax Rates'
        ordering = ['sales_tax_rate_id']
        get_latest_by = 'modified_date'
