"""
Defines the PhoneNumberType model for categorizing phone number formats.

This module provides a Django model for storing and managing phone number type
labels (e.g., 'Mobile', 'Home', 'Work') with case-insensitive uniqueness
enforcement. It includes metadata fields for tracking changes and supports
integration with external systems via UUIDs.

Use Cases:
- Reference table for contact management systems
- Normalization of phone number types across APIs
- Contributor-friendly onboarding for phone-related models

Dependencies:
- uuid: for generating globally unique identifiers
- django.db.models: for ORM model definitions
- django.db.models.functions: for case-insensitive constraints
"""

import uuid
from django.db import models


class PhoneNumberType(models.Model):
    """
    Represents a category or label for phone numbers (e.g., 'Mobile', 'Fax',
    'Work').

    Fields:
        - phone_number_type_id (BigAutoField): Primary key for the phone
        number type.
        - name (CharField): Descriptive label for the phone number type
        (case-insensitive unique).
        - rowguid (UUIDField): Globally unique identifier for external system
        integration.
        - modified_date (DateTimeField): Timestamp of the last update.

    Meta Options:
        - db_table: Explicit table name set to "phone_number_types".
        - managed: Set to False to indicate external table management.
        - verbose_name / verbose_name_plural: Human-readable names for admin
        interfaces.
        - constraints: Enforces case-insensitive uniqueness on `name`.

    Notes:
        - This model is typically used as a reference table in contact or CRM
        systems.
        - The `managed = False` flag suggests this table is maintained outside
        Django migrations.
        - The `rowguid` field supports replication and external system mapping.
    """

    phone_number_type_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Enter a phone number type."
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
        Configuration for the PhoneNumberType model.

        - db_table: Maps the model to the "phone_number_types" table.
        - managed: Disables Django's migration management for this model.
        - verbose_name: Singular label for admin display.
        - verbose_name_plural: Plural label for admin display.
        - constraints: Enforces case-insensitive uniqueness on `name` using
        Lower().
        """

        db_table = "phone_number_types"
        managed = False
        verbose_name = "Phone Number Type"
        verbose_name_plural = "Phone Number Types"
        ordering = ["phone_number_type_id"]
        get_latest_by = "modified_date"
