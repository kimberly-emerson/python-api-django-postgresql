"""
Custom user model extending Django's AbstractUser.

This module defines `AppUser`, a subclass of Django's built-in `AbstractUser`, 
to support future customization of user-related fields, authentication logic, 
and profile attributes.

Use this model when you need to:
- Add custom fields (e.g., `bio`, `profile_image`, `role`)
- Override default authentication behavior
- Integrate with external identity providers or user metadata
- Maintain compatibility with Django's admin and auth systems

Example:
    class AppUser(AbstractUser):
        bio = models.TextField(blank=True)
        role = models.CharField(max_length=50, default='contributor')

Note:
    To activate this model, set `AUTH_USER_MODEL = 'yourapp.AppUser'` 
    in your Django settings before running migrations.

"""


class AppUser(AbstractUser):
    """
    🧬 Extensible user model for custom authentication and profile data.

    Inherits all fields and methods from `AbstractUser`, including:
    - `username`, `email`, `first_name`, `last_name`, `password`
    - Permissions: `is_staff`, `is_superuser`, `groups`, `user_permissions`

    Extend this class to add domain-specific fields or override methods 
    like `save()`, `get_full_name()`, or `has_perm()`.

    Recommended for projects requiring flexible user schemas.
    """
