"""
tba
"""
import uuid
from django.db import models


class People(models.Model):
    """
    tba
    """

    person_id = models.BigAutoField(
        primary_key=True
    )
    person_type = models.CharField(
        max_length=2,
        help_text="Enter a person type."
    )
    name_style = models.BooleanField(
        default=False
    )
    title = models.CharField(
        max_length=8
    )
    first_name = models.CharField(
        max_length=50,
        help_text="Enter a first name."
    )
    middle_name = models.CharField(
        max_length=50,
        help_text="Enter a middle name."
    )
    last_name = models.CharField(
        max_length=50,
        help_text="Enter a last name."
    )
    suffix = models.CharField(
        max_length=10
    )
    email_promotion = models.IntegerField()
    additional_contact_info = models.TextField()
    demographics = models.TextField()
    country_region_code = models.CharField(
        max_length=3
    )
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        """
        tba
        """
        db_table = "people"
        managed = False
        verbose_name = "People"
        verbose_name_plural = "People"
        ordering = ["person_id"]
        get_latest_by = "modified_date"
