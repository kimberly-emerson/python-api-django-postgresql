"""
tba
"""

from django.db import models

from api.models.sales_people_model import SalesPeople
from api.models.credit_card_model import CreditCard


class SalesPersonCreditCard(models.Model):
    """
    tba
    """

    sales_person = models.ForeignKey(
        SalesPeople,
        related_name='sales_person_credit_card',
        verbose_name='Sales Person',
        primary_key=True,
        on_delete=models.CASCADE
    )
    credit_card = models.ForeignKey(
        CreditCard,
        related_name='',
        verbose_name='',
        primary_key=True,
        on_delete=models.CASCADE
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """
        tba
        """

        db_table = "sales_person_credit_cards"
        managed = False
        verbose_name = "Sales Person Credit Card"
        verbose_name_plural = "Sales Person Credit Cards"
        ordering = [
            'sales_person',
            'credit_card'
        ],
        get_latest_by = 'modified_date'
