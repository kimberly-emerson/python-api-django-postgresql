"""
tba
"""
from django.db import models


class SalesReason(models.Model):
    """
    tba
    """

    sales_reason_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    reason_type = models.CharField(
        max_length=50
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
        db_table = 'sales_reasons'
        managed = False
        verbose_name = 'Sales Reason'
        verbose_name_plural = 'Sales Reasons'
        ordering = ['sales_reason_id']
        get_latest_by = 'modified_date'
