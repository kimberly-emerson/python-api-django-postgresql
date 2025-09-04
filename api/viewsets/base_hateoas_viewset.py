"""
tba
"""
from rest_framework import viewsets

from api.mixins.hateoas_mixin import HATEOASMixin
from api.utils.basename_handler import class_to_plural_basename


class BaseHATEOASViewSet(HATEOASMixin, viewsets.ModelViewSet):
    """
    Base class for all HATEOAS-enabled ViewSets.
    Automatically derives plural kebab-case basename from class name,
    but allows explicit override via `basename_override`.
    """

    lookup_field = "pk"
    basename_override: str = None  # subclasses can set this

    @classmethod
    def get_basename(cls):
        """
        tba
        """
        if getattr(cls, "basename", None):
            return cls.basename
        return class_to_plural_basename(
            cls.__name__,
            custom_plural=cls.basename_override
        )
