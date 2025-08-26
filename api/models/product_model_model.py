"""
tba
"""
import uuid
from django.db import models


class ProductModel(models.Model):
    """
    tba
    """

    product_model_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    catalog_description = models.TextField()
    instructions = models.TextField()
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
        db_table = "product_models"
        managed = False
        verbose_name = "Product Model"
        verbose_name_plural = "Product Models"
        ordering = ["product_model_id"]
        get_latest_by = "modified_date"
