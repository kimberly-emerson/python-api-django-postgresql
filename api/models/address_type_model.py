"""
Address Type Model Definition

This module defines the `AddressType` model, which represents standardized
categories used to classify address records (e.g., 'Billing', 'Shipping',
'Headquarters') across the system. It includes a case-insensitive uniqueness
constraint on the `name` field  to prevent duplicate entries and supports
external system integration via a UUID field.

Key Features:
- Case-insensitive uniqueness enforced via `Lower("name")` constraint
- Globally unique identifier (`rowguid`) for cross-system mapping
- Auto-updated `modified_date` for audit and sync tracking
- `managed = False` for legacy or externally managed DB tables

Intended Use:
- Reference model for address categorization in related tables
- Supports consistent filtering, reporting, and external data exchange
- Ideal for systems requiring normalized address metadata

Note:
- Ensure serializers and admin interfaces reflect the uniqueness constraint
- Extend with multilingual support or soft-deletion if needed
"""

import uuid
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class AddressType(models.Model):
    """
    Defines a standardized category for classifying address records.

    The `AddressType` model represents distinct types of addresses such as
    'Billing', 'Shipping', or 'Headquarters'. Each type is uniquely identified
    by a case-insensitive `name` and includes metadata for external system
    integration and audit tracking.

    Fields:
        address_type_id (BigAutoField): Primary key for the address type.
        name (CharField): Unique name of the address type (case-insensitive).
        rowguid (UUIDField): Globally unique identifier for external mapping.
        modified_date (DateTimeField): Timestamp of the last update.

    Meta Options:
        db_table: "address_types"
        managed: False (used for legacy or externally managed tables)
        verbose_name: "Address Type"
        verbose_name_plural: "Address Types"
        constraints:
            - Enforces case-insensitive uniqueness on `name` using `Lower()`
            - Custom error message for duplicate entries

    Usage:
        Used to tag address records in related models, enabling consistent
        categorization, filtering, and reporting across systems.

    Example:
        AddressType.objects.create(name="Shipping")
    """

    address_type_id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter an address type."
    )
    rowguid = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Metadata configuration for the AddressType model.

        This class defines database-level behavior, naming conventions, and
        constraints for the `AddressType` table. It is configured for use with
        a legacy or externally managed database, and enforces case-insensitive
        uniqueness on the `name` field.

        Attributes:
          - db_table (str): Explicit table name in the database
            ("address_types").
          - managed (bool): Set to False to prevent Django from managing
          migrations.
          - verbose_name (str): Singular name for admin and documentation
          ("Address Type").
          - verbose_name_plural (str): Plural name for admin and documentation
          ("Address Types").
          - constraints (list): Enforces case-insensitive uniqueness on `name`
          using `Lower()`.

        Notes:
            - The uniqueness constraint prevents duplicate address types
            regardless of casing.
            - `managed = False` is typically used for legacy tables or
            external DB integrations.
            - Custom violation error message improves clarity during
            validation failures.
        """

        db_table = "address_types"
        managed = False
        verbose_name = "Address Type"
        verbose_name_plural = "Address Types"
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="address_type_name_case_insensitive_unique",
                violation_error_message="AddressType already exists "
                "(case insensitive match)",
            ),
        ]
