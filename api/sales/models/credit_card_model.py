"""
tba
"""
from django.db import models


class CreditCard(models.Model):
    """
    tba
    """

    credit_card_id = models.BigAutoField(
        primary_key=True
    )
    card_type = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter a credit card type."
    )
    card_number = models.CharField(
        max_length=25,
        unique=True,
        help_text="Enter a credit card number."
    )
    expiration_year = models.SmallIntegerField(
        db_column="exp_year",
        help_text="Enter an expiration year."
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.card_number}"

    class Meta:
        """
        tba
        """
        db_table = "credit_cards"
        managed = False
        verbose_name = "Credit Card"
        verbose_name_plural = "Credit Cards"
        ordering = ["credit_card_id"]
        get_latest_by = "modified_date"
