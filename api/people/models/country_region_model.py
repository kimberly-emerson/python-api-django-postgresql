"""
CountryRegion Model

tba
"""
from django.db import models


class CountryRegionManager(models.Manager):
    """
    tba
    """


class CountryRegion(models.Model):
    """
    Represents a country using a standardized country region code and name.

    Fields:
        - country_region_code (CharField): Primary key representing the
        country region code.
        - name (CharField): A short name or abbreviation for the country
        (max 3 characters).
        - rowguid (UUIDField): A globally unique identifier for the record.
        - modified_date (DateTimeField): Timestamp of the last modification.

    Meta Options:
        - db_table: Explicit table name set to "country_regions".
        - managed: Set to False to indicate external table management.
        - verbose_name / verbose_name_plural: Human-readable names for admin
        interfaces.
        - constraints: Enforces case-insensitive uniqueness on
        `country_region_code`.

    Notes:
        - This model is typically used in reference tables for localization,
        reporting, or integration with external APIs.
        - The `managed = False` flag suggests this table is maintained outside
        Django migrations.
    """

    country_region_code = models.CharField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Enter a country region code."
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    objects = CountryRegionManager()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        """
        Configuration for the CountryRegion model.

        - db_table: Maps the model to the "country_regions" table.
        - managed: Disables Django's migration management for this model.
        - verbose_name: Singular label for admin display.
        - verbose_name_plural: Plural label for admin display.
        """
        db_table = "country_regions"
        managed = False
        verbose_name = "Country Region"
        verbose_name_plural = "Country Regions"
        ordering = ["country_region_code"]
        get_latest_by = "modified_date"
