"""
tba
"""
import uuid
from django.db import models

from api.models.sales_people_model import SalesPeople
from api.models.sales_territory_model import SalesTerritory


class SalesTerritoriesHistory(models.Model):
    """
    tba
    """

    sales_person = models.ForeignKey(
        SalesPeople,
        related_name='sales_territories_history',
        verbose_name='Sales Person',
        primary_key=True,
        on_delete=models.CASCADE
    )
    sales_territory = models.ForeignKey(
        SalesTerritory,
        related_name='sales_territories_history',
        verbose_name='Sales Territory',
        primary_key=True,
        on_delete=models.CASCADE
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """
        tba
        """
        db_table = "sales_territories_history"
        managed = False
        verbose_name = "Sales Territories History"
        verbose_name_plural = "Sales Territories History"
        ordering = [
            'sales_person',
            'sales_territory'
        ]
        get_latest_by = 'modified_date'
