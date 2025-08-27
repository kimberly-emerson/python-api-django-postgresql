"""
tba
"""
from django.db import models


class UnitMeasure(models.Model):
    """
    tba
    """

    unit_measure_code = models.CharField(
        max_length=8,
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        unique=True
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
        db_table = "unit_measures"
        managed = False
        verbose_name = "Unit Measure"
        verbose_name_plural = "Unit Measures"
        ordering = ['unit_measure_id']
        get_latest_by = 'modified_date'
