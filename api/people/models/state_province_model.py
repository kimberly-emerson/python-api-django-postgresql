"""
State Province Model

tba
"""

import uuid
from django.db import models

from api.people.models.country_region_model import CountryRegion
from api.sales.models.sales_territory_model import SalesTerritory


class StateProvinceManager(models.Manager):
    """
    tba
    """


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
        db_column='country_region_code',
        on_delete=models.CASCADE
    )
    is_only_state_province_flag = models.BooleanField(
        default=False
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    sales_territory = models.ForeignKey(
        SalesTerritory,
        related_name='state_provinces',
        verbose_name='Sales Territory',
        db_column='sales_territory_id',
        on_delete=models.CASCADE
    )
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    objects = StateProvinceManager()

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
