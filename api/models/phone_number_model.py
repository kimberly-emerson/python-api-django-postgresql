"""

"""


from django.db import models
from django.db.models import UniqueConstraint

from api.models.people_model import People
from api.models.phone_number_type_model import PhoneNumberType


class PhoneNumber(models.Model):
    """
    tba
    """

    person = models.ForeignKey(
        People,
        on_delete=models.CASCADE,
        primary_key=True
    )
    phone_number_type = models.ForeignKey(
        PhoneNumberType,
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(
        max_length=25,
        primary_key=True
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.phone_number}"

    class Meta:
        """
        tba
        """

        db_table = "phone_numbers"
        managed = False
        verbose_name = "Phone Number"
        verbose_name_plural = "Phone Numbers"
        ordering = [
            "person",
            "phone_number"
        ]
        get_latest_by = "modified_date"
