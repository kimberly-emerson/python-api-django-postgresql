"""
tba
"""
import uuid
from django.db import models

from api.models.sales_order_header_model import SalesOrderHeader
from api.models.product_model import Product
from api.models.special_offer_model import SpecialOffer


class SalesOrderDetail(models.Model):
    """
    tba
    """

    sales_order = models.ForeignKey(
        SalesOrderHeader,
        related_name='sales_order_details',
        verbose_name='Sales Order Header',
        primary_key=True,
        on_delete=models.CASCADE
    )
    sales_order_detail_id = models.BigAutoField(
        primary_key=True
    )
    character_tracking_number = models.CharField(
        max_length=25
    )
    order_quantity = models.PositiveSmallIntegerField()
    product_id = models.ForeignKey(
        Product,
        related_name='sales_order_details',
        on_delete=models.CASCADE
    )
    special_offer_id = models.ForeignKey(
        SpecialOffer,
        related_name="sales_order_details",
        on_delete=models.CASCADE,
    )
    unit_price = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    unit_price_discount = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    line_total = models.DecimalField(
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

    def __str__(self):
        return f"{self.character_tracking_number}"

    class Meta:
        """
        tba
        """
        db_table = "sales_order_details"
        managed = False
        verbose_name = "Sales Order Detail"
        verbose_name_plural = "Sales Order Details"
        unique_together = [
            "sales_order",
            "sales_detail_id"
        ]
        ordering = [
            "sales_detail_id"
        ]
        get_latest_by = "modified_date"
