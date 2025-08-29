"""
State Province Model

Defines the StateProvince model, representing administrative regions within a
country that are linked to sales territories and country regions.

This model is part of the location hierarchy used for sales and demographic
reporting. It supports contributor-friendly relationships to CountryRegion and
SalesTerritory, and includes metadata for auditability and integration.

Intended Use:
- Workforce development and training datasets
- Sales territory mapping and reporting
- Contributor onboarding for location-based models

Related Models:
- CountryRegion
- SalesTerritory
"""

import uuid
from django.db import models

from api.people.models.country_region_model import CountryRegion
from api.sales.models.sales_territory_model import SalesTerritory


class StateProvince(models.Model):
    """
    Refines the StateProvince model, representing administrative regions
    within a country that are linked to sales territories and country regions.

    This model is part of the location hierarchy used for sales and
    demographic reporting. It supports contributor-friendly relationships to
    CountryRegion and SalesTerritory, and includes metadata for auditability
    and integration.

    Intended Use:
    - Workforce development and training datasets
    - Sales territory mapping and reporting
    - Contributor onboarding for location-based models

    Related Models:
    - CountryRegion
    - SalesTerritory
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

    def __str__(self):
        return f"{self.name}"

    class Meta:
        """
        Configuration for the StateProvince model's database behavior and
        admin display.

        Attributes:
            db_table (str): Explicit name of the database table
            ("state_provinces").
            managed (bool): Set to False to indicate that Django does not
            manage this table's schema.
            verbose_name (str): Singular name used in admin and documentation
            ("State Province").
            verbose_name_plural (str): Plural name used in admin and
            documentation ("State Provinces").
            ordering (list): Default ordering by state_province_id.
            get_latest_by (str): Field used to determine the most recently
            modified record.

        Notes:
            - `managed = False` assumes external schema control (e.g., legacy
            database or ETL sync).
            - `get_latest_by` enables queryset methods like `latest()` for
            audit and sync tracking.
            - Contributor onboarding should include schema awareness and
            external migration notes.
        """
        db_table = "state_provinces"
        managed = False
        verbose_name = "State Province"
        verbose_name_plural = "State Provinces"
        ordering = ['state_province_id']
        get_latest_by = 'modified_date'
