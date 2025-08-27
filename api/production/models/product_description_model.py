"""
tba
"""
import uuid
from django.db import models


class ProductDescription(models.Model):
    """
    tba
    """

    product_description_id = models.BigAutoField(
        primary_key=True
    )
    description = models.CharField()
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.description}"

    class Meta:
        """
        tba
        """
        db_table = "product_descriptions"
        managed = False
        verbose_name = "Product Description"
        verbose_name_plural = "Product Descriptions"
        ordering = ["product_description_id"]
        get_latest_by = "modified_date"
