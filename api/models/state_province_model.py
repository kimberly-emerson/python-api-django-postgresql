"""
tba
"""
import uuid
from django.db import models

from api.models.country_region_model import CountryRegion
from api.models.sales_territory_model import SalesTerritory


class StateProvince(models.Model):
    """
    tba
    """

    state_province_id = models.BigAutoField(
        primary_key=True
    )
    state_province_code = models.CharField(
        max_length=3,
        unique=True,
        help_text="Enter a state province code."
    )
    country_region = models.ForeignKey(
        CountryRegion,
        related_name='state_provinces',
        verbose_name='Country Region',
        on_delete=models.CASCADE
    )
    is_only_state_province_flag = models.BooleanField(
        default=True
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    sales_territory = models.ForeignKey(
        SalesTerritory,
        related_name='state_provinces',
        verbose_name='Sales Territory',
        on_delete=models.CASCADE
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
        db_table = "state_provinces"
        managed = False
        verbose_name = "State Province"
        verbose_name_plural = "State Provinces"
        ordering = ['state_province_id']
        get_latest_by = 'modified_date'
