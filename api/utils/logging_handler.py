"""
    Structured logging utility for REST API events.

    Args:
        level (str): Logging level (INFO, WARNING, ERROR).
        message (str): Human-readable log message.
        **kwargs (Any): Contextual fields (user, method, path, status, etc).

    Example:
        log_event("INFO", "AddressType created", user="admin", id=123, status=201)
"""
import logging
import json
from datetime import datetime, timezone
from typing import Any, Dict

logger = logging.getLogger(__name__)


def log_event(level: str, message: str, **kwargs: Any) -> None:
    """
    Structured logging utility for REST API events.

    Args:
        level (str): Logging level (INFO, WARNING, ERROR).
        message (str): Main log message.
        **kwargs (Any): Contextual fields (user, method, path, etc).
    """
    log_data: Dict[str, Any] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "message": message,
        **kwargs
    }
    getattr(logger, level.lower())(json.dumps(log_data))
