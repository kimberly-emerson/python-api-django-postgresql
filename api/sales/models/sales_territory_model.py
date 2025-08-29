"""
tba
"""
import uuid
from django.db import models

from api.people.models.country_region_model import CountryRegion


class SalesTerritory(models.Model):
    """
    tba
    """

    sales_territory_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Enter a sales territory."
    )
    country_region = models.ForeignKey(
        CountryRegion,
        related_name='sales_territories',
        verbose_name='Country Region',
        db_column='country_region_code',
        on_delete=models.CASCADE
    )
    region = models.CharField(
        max_length=50,
        help_text='Enter a region.'
    )
    sales_ytd = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    sales_last_year = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    cost_ytd = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    cost_last_year = models.DecimalField(
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
        db_table = "sales_territories"
        managed = False
        verbose_name = "Sales Territory"
        verbose_name_plural = "Sales Territories"
        ordering = ['sales_territory_id']
        get_latest_by = 'modified_date'
