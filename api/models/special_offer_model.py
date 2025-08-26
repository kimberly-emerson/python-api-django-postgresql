"""
tba
"""
import uuid
from django.db import models


class SpecialOffer(models.Model):
    """
    tba
    """

    special_offer_id = models.BigAutoField(
        primary_key=True
    )
    description = models.CharField(
        max_length=255,
        unique=True
    )
    discount_percentage = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        db_column="discount_pct"
    )
    special_offer_type = models.CharField(
        max_length=50,
        db_column="type"
    )
    category = models.CharField(
        max_length=50
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    minimum_quantity = models.PositiveSmallIntegerField(
        db_column="min_qty"
    )
    maximum_quantity = models.PositiveSmallIntegerField(
        db_column="max_qty"
    )
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
        db_table = "special_offers"
        managed = False
        verbose_name = "Special Offer"
        verbose_name_plural = "Special Offers"
        ordering = ['special_offer_id']
        get_latest_by = 'modified_date'
