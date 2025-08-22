"""
Application bootstrap module.

This module serves as the entry point for initializing the logging system
and launching the application. It imports and invokes `configure_logging()`
from `utils.logger` to set up consistent log formatting and output destinations
for both file and console logging.

Once configured, it retrieves the 'api' logger instance for scoped logging
within the application domain.

Modules:
--------
- logging: Python standard logging library.
- utils.logger: Custom utility module for centralized logging configuration.

Functions:
----------
- main(): Initializes logging and logs startup message using the 'api' logger.

Usage:
------
Run this module directly to initialize logging and start the application.

Example:
--------
>>> python app.py
>>> # Logs will be written to file and console with standardized formatting.
"""

import logging
from utils.logger import configure_logging


def main() -> None:
    """
    Application entry point.

    This function configures the logging system using `configure_logging()`
    from the `utils.logger` module, ensuring consistent log formatting and
    output destinations.

    It also retrieves the 'api' logger instance, which can be used throughout
    the application for scoped logging.

    Intended to be called at application startup.

    Returns:
        None

    Example:
        >>> main()
        >>> logging.getLogger('api').info("API logger initialized.")
    """

    configure_logging()
    logging.getLogger('api').info("API logger initialized.")


if __name__ == "__main__":
    main()
