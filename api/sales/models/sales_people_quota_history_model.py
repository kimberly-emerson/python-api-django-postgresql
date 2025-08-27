"""
tba
"""

import uuid
from django.db import models

from api.models.sales_people_model import SalesPeople


class SalesPeopleQuotaHistory(models.Model):
    """
    tba
    """

    sales_person = models.ForeignKey(
        SalesPeople,
        related_name='sales_people_quota_history',
        verbose_name='Sales Person',
        primary_key=True,
        on_delete=models.CASCADE
    )
    quota_date = models.DateTimeField(
        primary_key=True,
        on_delete=models.CASCADE,
        auto_now=True
    )
    sales_quota = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
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

        db_table = "sales_people_quota_history"
        managed = False
        verbose_name = "Sales People Quota History"
        verbose_name_plural = "Sales People Quota History"
        unique_together = [
            'sales_person',
            'quota_date'
        ]
        ordering = [
            'sales_person_id',
            'quota_date'
        ]
        get_latest_by = 'modified_date'
