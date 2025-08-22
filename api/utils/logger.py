"""
Logging configuration module.

This module sets up a standardized logging system for the application,
writing logs to both a file and the console. It ensures consistent formatting
and log levels across environments, making debugging and monitoring easier
for developers and contributors.

Functions:
----------
- configure_logging():
    Initializes logging with the following settings:
    - File output: Logs are written to 'app.log' in the directory returned by
    `get_logs_path()`.
    - Console output: Logs are streamed to stderr with simplified formatting.
    - Log level: INFO and above.
    - Formats:
        - File: Timestamped, detailed format including logger name and message.
        - Console: Compact format for readability during development.

Dependencies:
-------------
- logging: Python standard library for logging.
- path_handler.get_logs_path: Custom utility to determine the log file
directory.

Usage:------
Call `configure_logging()` once at application startup to initialize logging.

Example:
--------
>>> from logger_config import configure_logging
>>> configure_logging()
>>> logging.info("Application started.")
"""

import logging
from path_handler import get_logs_path


def configure_logging():
    """
    Initializes application-wide logging configuration.

    This function sets up logging to output messages to both a log file and
    the console.

    It ensures consistent formatting and log levels for easier debugging,
    monitoring, and contributor onboarding.

    File Logging:
    - Location: `{get_logs_path()}\\app.log`
    - Level: INFO and above
    - Format: `%(asctime)s - %(levelname)s - %(name)s - %(message)s`
    - Date Format: `YYYY-MM-DD HH:MM:SS`

    Console Logging:
    - Output: stderr
    - Level: INFO and above
    - Format: `%(name)-12s: %(levelname)-8s %(message)s`

    Returns:
        None

    Example:
        >>> configure_logging()
        >>> logging.info("Logging initialized.")
    """

    logging.basicConfig(
        filename=f"{get_logs_path()}\\app.log",
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
