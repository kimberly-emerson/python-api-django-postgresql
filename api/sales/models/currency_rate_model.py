"""
tba
"""
from django.db import models

from api.models.currency_model import Currency


class CurrencyRate(models.Model):
    """
    tba
    """

    currency_rate_id = models.BigAutoField(
        primary_key=True
    )
    currency_rate_date = models.DateTimeField()
    from_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE
    )
    to_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE
    )
    average_rate = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    end_of_date_rate = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """
        tba
        """
        db_table = "currency_rates"
        managed = False
        verbose_name = "Currency Rate"
        verbose_name_plural = "Currency Rates"
        ordering = ["currency_rate_id"]
        get_latest_by = "modified_date"
