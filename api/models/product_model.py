"""
tba
"""
import uuid
from django.db import models

from api.models.unit_measures_model import UnitMeasure
from api.models.product_subcategories_model import ProductSubcategory
from api.models.product_model_model import ProductModel


class Product(models.Model):
    """
    tba
    """

    product_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        help_text="Enter a product."
    )
    product_number = models.CharField(
        max_length=25,
        default=False
    )
    make_flag = models.BooleanField(
        default=False
    )
    finished_goods = models.BooleanField(
        default=False
    )
    color = models.CharField(
        max_length=15
    )
    safety_stock_level = models.PositiveSmallIntegerField()
    reorder_point = models.PositiveSmallIntegerField()
    standard_cost = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    list_price = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    size = models.CharField(
        max_length=5
    )
    size_unit_measure = models.ForeignKey(
        UnitMeasure,
        on_delete=models.CASCADE
    )
    weight_unit_measure = models.ForeignKey(
        UnitMeasure,
        on_delete=models.CASCADE
    )
    weight = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    days_to_manufacture = models.PositiveSmallIntegerField()
    product_line = models.CharField(
        max_length=2
    )
    class_field = models.CharField(
        max_length=2,
        db_column="class"
    )
    style = models.CharField(
        max_length=2
    )
    product_subcategory = models.ForeignKey(
        ProductSubcategory,
        on_delete=models.CASCADE
    )
    product_model = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE
    )
    sell_start_date = models.DateTimeField()
    discontinued_date = models.DateTimeField()
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
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
        db_table = "products"
        managed = False
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["product_id"]
        get_latest_by = "modified_date"
