"""
tba
"""
import uuid
from django.db import models

from api.people.models.address_model import Address
from api.sales.models.customer_model import Customer
from api.sales.models.ship_method_model import ShipMethod
from api.sales.models.sales_people_model import SalesPeople
from api.sales.models.sales_territory_model import SalesTerritory
from api.sales.models.credit_card_model import CreditCard
from api.sales.models.currency_rate_model import CurrencyRate


class SalesOrderHeader(models.Model):
    """
    tba
    """

    sales_order_id = models.BigAutoField(
        primary_key=True
    )
    revision_number = models.PositiveSmallIntegerField()
    order_date = models.DateTimeField()
    due_date = models.DateTimeField()
    ship_date = models.DateTimeField()
    status = models.PositiveSmallIntegerField()
    online_order_flag = models.BooleanField(
        default=False
    )
    sales_order_number = models.CharField(
        max_length=255
    )
    purchase_order_number = models.CharField(
        max_length=255
    )
    account_number = models.CharField(
        max_length=255
    )
    customer = models.ForeignKey(
        Customer,
        related_name='sales_order_headers',
        verbose_name='Customer',
        on_delete=models.CASCADE
    )
    sales_person = models.ForeignKey(
        SalesPeople,
        related_name='sales_order_headers',
        verbose_name='Sales Person',
        on_delete=models.CASCADE
    )
    sales_territory = models.ForeignKey(
        SalesTerritory,
        related_name='sales_order_headers',
        verbose_name='Sales Territory',
        on_delete=models.CASCADE
    )
    bill_to_address = models.ForeignKey(
        Address,
        related_name='sales_order_headers',
        verbose_name='Billing Address',
        on_delete=models.CASCADE
    )
    ship_to_address = models.ForeignKey(
        Address,
        related_name='sales_order_headers',
        verbose_name='Shipping Address',
        on_delete=models.CASCADE
    )
    ship_method = models.ForeignKey(
        ShipMethod,
        related_name='sales_order_headers',
        verbose_name='Ship Method',
        on_delete=models.CASCADE
    )
    credit_card = models.ForeignKey(
        CreditCard,
        related_name='sales_order_headers',
        verbose_name='Credit Card',
        on_delete=models.CASCADE
    )
    credit_card_approval_code = models.CharField(
        max_length=15
    )
    currency_rate = models.ForeignKey(
        CurrencyRate,
        related_name='sales_order_headers',
        verbose_name='Currency Rate',
        on_delete=models.CASCADE
    )
    subtotal = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    tax_amount = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    freight = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    comment = models.CharField(
        max_length=128
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
        db_table = "sales_order_headers"
        managed = False
        verbose_name = "Sales Order Header"
        verbose_name_plural = "Sales Order Headers"
        ordering = ["sales_order_id"]
        get_latest_by = "modified_date"
