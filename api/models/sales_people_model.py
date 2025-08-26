'''
tba
'''
import uuid
from django.db import models


class SalesPeople(models.Model):
    '''
    tba
    '''

    sales_person_id = models.BigAutoField(
        primary_key=True
    )
    sales_quota = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    bonus = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    commission_percentage = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        db_column='commission_pct'
    )
    sales_ytd = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    sales_last_year = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        '''
        tba
        '''
        db_table = 'sales_people'
        managed = False
        verbose_name = 'Sales People'
        verbose_name_plural = 'Sales People'
        ordering = ['sales_person_id']
        get_latest_by = 'modified_date'
