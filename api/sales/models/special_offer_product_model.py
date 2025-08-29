"""
tba
"""
import uuid
from django.db import models

from api.production.models.product_model import Product
from api.sales.models.special_offer_model import SpecialOffer


class SpecialOfferProduct(models.Model):
    """
    tba
    """

    sales_offer_id = models.ForeignKey(
        SpecialOffer,
        related_name='special_offer_products',
        verbose_name='Special Offer',
        primary_key=True,
        on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Product,
        related_name='special_offer_products',
        verbose_name='Product',
        primary_key=True,
        on_delete=models.CASCADE
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
        db_table = "special_offer_products"
        managed = False
        verbose_name = "Special Offer Product"
        verbose_name_plural = "Special Offer Products"
        ordering = [
            'special_offer',
            'product'
        ]
        get_latest_by = 'modified_date'
