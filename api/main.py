"""
tba
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
