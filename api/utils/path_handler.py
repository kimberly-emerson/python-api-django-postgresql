"""
Path resolution utility module.

This module centralizes directory path construction for key application
components using environment variables and the project’s root directory.
It ensures consistent, configurable access to subdirectories such as
`APP_DIR`, `CORE_DIR`, and `LOGS_DIR`.

Features:
---------
- Dynamically resolves absolute paths using `pathlib.Path`.
- Reads directory names from environment variables via `python-decouple`.
- Supports modular access to application, core, and logging directories.

Environment Variables:
----------------------
- `APP_DIR`: Relative path to the main application directory.
- `CORE_DIR`: Relative path to shared core utilities or services.
- `LOGS_DIR`: Relative path to the logging output directory.

Functions:
----------
- `get_app_path()`: Returns the absolute path to the application directory.
- `get_core_path()`: Returns the absolute path to the core services directory.
- `get_logs_path()`: Returns the absolute path to the logging directory.

Usage:
------
Import this module wherever directory paths are needed to avoid hardcoding and
to support flexible deployment configurations.

Example:
    from path_handler import get_logs_path
    log_file = f"{get_logs_path()}\\app.log"

Dependencies:
-------------
- `pathlib.Path`: For cross-platform path resolution.
- `decouple.config`: For environment-based configuration.
"""

from pathlib import Path
from decouple import config

ROOT_DIR = Path(__file__).resolve().parent.parent


def get_app_path() -> str:
    """
    Resolve the absolute path to the application directory.

    Reads the `APP_DIR` environment variable using `decouple.config` and
    appends it to the project root path. Useful for locating the main
    application package or entry point.

    Returns:
        str: Absolute path to the application directory.

    Example:
        >>> get_app_path()
        '../../api'
    """
    return f"{Path(ROOT_DIR)}\\{config('APP_DIR')}"


def get_core_path() -> str:
    """
    Resolve the absolute path to the core services or utilities directory.

    Reads the `CORE_DIR` environment variable and appends it to the project
    root.

    Typically used for shared logic, middleware, or reusable components.

    Returns:
        str: Absolute path to the core directory.

    Example:
        >>> get_core_path()
        '../../core'
    """
    return f"{Path(ROOT_DIR)}\\{config('CORE_DIR')}"


def get_logs_path() -> str:
    """
    Resolve the absolute path to the logging output directory.

    Reads the `LOGS_DIR` environment variable and appends it to the project
    root.

    Used for storing log files generated during application runtime.

    Returns:
        str: Absolute path to the logs directory.

    Example:
        >>> get_logs_path()
        '../../logs'
    """
    return f"{Path(ROOT_DIR)}\\{config('LOGS_DIR')}"
