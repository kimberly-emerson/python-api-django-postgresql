"""
tba
"""
import logging

logger = logging.getLogger(__name__)


class LoggingMixin:
    """
    tba
    """
    def log_action(self, action, instance=None, extra=None):
        """
        tba
        """
        user = getattr(self.request, "user", None)
        log_data = {
            "user": str(user),
            "action": action,
            "instance": getattr(instance, self.lookup_field, None) if instance else None,
            "extra": extra or {}
        }
        logger.info(log_data)

    def perform_create(self, serializer):
        """
        tba
        """
        instance = serializer.save()
        self.log_action("create", instance)
        return instance

    def perform_update(self, serializer):
        """
        tba
        """
        instance = serializer.save()
        self.log_action("update", instance)
        return instance

    def perform_destroy(self, instance):
        """
        tba
        """
        self.log_action("destroy", instance)
        instance.delete()
