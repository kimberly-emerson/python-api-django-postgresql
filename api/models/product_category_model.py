"""
tba
"""
import uuid
from django.db import models


class ProductCategory(models.Model):
    """
    tba
    """

    product_category_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        unique=True
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
        db_table = "product_categories"
        managed = False
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ["name"]
        get_latest_by = "modified_date"
