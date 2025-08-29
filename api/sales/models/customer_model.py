"""
tba
"""
import uuid
from django.db import models

from api.people.models.people_model import People
from api.sales.models.sales_territory_model import SalesTerritory
from api.sales.models.store_model import Store


class Customer(models.Model):
    """
    tba
    """

    customer_id = models.BigAutoField(
        primary_key=True
    )
    person = models.OneToOneField(
        People,
        on_delete=models.CASCADE,
        primary_key=True
    )
    person_type = models.CharField(
        max_length=2,
        help_text="Enter a person type."
    )
    sales_territory = models.ForeignKey(
        SalesTerritory,
        on_delete=models.CASCADE
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE
    )
    account_number = models.CharField(
        max_length=255
    )
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.account_number}"

    class Meta:
        """
        tba
        """
        db_table = "customers"
        managed = False
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["customer_id"]
        get_latest_by = "modified_date"
