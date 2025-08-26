"""
tba
"""
import uuid
from django.db import models

from api.models.product_category_model import ProductCategory


class ProductSubcategory(models.Model):
    """
    tba
    """

    product_subcategory_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
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
        db_table = "product_subcategories"
        managed = False
        verbose_name = "Product Subcategory"
        verbose_name_plural = "Product Subcategories"
        ordering = ["product_subcategory_id"]
        get_latest_by = "modified_date"
