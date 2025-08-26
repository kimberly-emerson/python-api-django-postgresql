"""
tba
"""
from django.db import models


class Currency(models.Model):
    """
    tba
    """

    currency_code = models.CharField(
        primary_key=True
    )
    name = models.CharField(
        max_length=3,
        unique=True,
        help_text="Enter a country region code."
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
        db_table = "currencies"
        managed = False
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        ordering = ["currency_code"]
        get_latest_by = "modified_date"
