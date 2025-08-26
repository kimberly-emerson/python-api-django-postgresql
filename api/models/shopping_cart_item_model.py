"""
tba
"""
from django.db import models

from api.models.product_model import Product


class ShoppingCartItem(models.Model):
    """
    tba
    """

    shopping_cart_item_id = models.BigAutoField(
        primary_key=True
    )
    shopping_card_id = models.BigAutoField()
    quantity = models.PositiveSmallIntegerField()
    product = models.ForeignKey(
        Product,
        related_name='shopping_cart_items',
        verbose_name='Product',
        primary_key=True,
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(
        db_column="date_created"
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """
        tba
        """
        db_table = "shopping_cart_items"
        managed = False
        verbose_name = "Shopping Cart Item"
        verbose_name_plural = "Shopping Cart Items"
        ordering = ['shopping_cart_item_id']
        get_latest_by = 'modified_date'
