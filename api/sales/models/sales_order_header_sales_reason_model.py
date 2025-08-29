"""
tba
"""
from django.db import models

from api.sales.models.sales_order_header_model import SalesOrderHeader
from api.sales.models.sales_reason_model import SalesReason


class SalesOrderHeaderSalesReason(models.Model):
    """
    tba
    """

    sales_order = models.ForeignKey(
        SalesOrderHeader,
        related_name='sales_order_header_sales_reasons',
        verbose_name='Sales Order Header',
        on_delete=models.CASCADE
    )
    sales_reason = models.ForeignKey(
        SalesReason,
        related_name='sales_order_header_sales_reasons',
        verbose_name='Sales Reason',
        on_delete=models.CASCADE
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """
        tba
        """
        db_table = "sales_order_header_sales_reasons"
        managed = False
        verbose_name = "Sales Order Header Sales Reason"
        verbose_name_plural = "Sales Order Header Sales Reasons"
        unique_together = [
            "sales_order",
            "sales_reason"
        ]
        ordering = [
            "sales_order",
            "sales_reason"
        ]
        get_latest_by = "modified_date"
