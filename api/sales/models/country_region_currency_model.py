"""
tba
"""
from django.db import models

from api.people.models.country_region_model import CountryRegion
from api.sales.models.currency_model import Currency


class CountryRegionCurrency(models.Model):
    """
    tba
    """

    country_region = models.OneToOneField(
        CountryRegion,
        on_delete=models.CASCADE,
        primary_key=True
    )
    currency = models.CharField(
        Currency,
        on_delete=models.CASCADE,
        primary_key=True
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """
        tba
        """
        db_table = "country_region_currencies"
        managed = False
        verbose_name = "Country Region Currency"
        verbose_name_plural = "Country Region Currencies"
        unique_together = [
            "country_region",
            "currency"
        ]
        ordering = [
            "country_region",
            "currency"
        ]
