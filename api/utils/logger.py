"""
Logging configuration module.

This module initializes application-wide logging using Python's built-in
`logging` library. It sets up both file-based and console logging with
distinct formats and levels to support diagnostics, monitoring, and
debugging across environments.

Features:
---------
- Logs are written to a timestamped file located at the path returned
by `get_logs_path()`.
- Console output is enabled via `StreamHandler` for immediate feedback
during development.
- Log messages include timestamp, severity level, logger name,
and message content.
- Console output uses a simplified format for readability.

File Logging:
-------------
- Location: `<logs_path>/app.log`
- Level: `INFO` and above
- Format: `YYYY-MM-DD HH:MM:SS - LEVEL - LOGGER - MESSAGE`

Console Logging:
----------------
- Output: `sys.stderr`
- Level: `INFO` and above
- Format: `LOGGER      : LEVEL    MESSAGE`

Usage:
------
Import this module early in your application entry point to ensure
consistent logging behavior.

Example:
    from logger_config import *  # Ensures logging is configured
    before other imports

Dependencies:
-------------
- `path_handler.get_logs_path`: Returns the directory path for storing
log files.
"""

import logging
from path_handler import get_logs_path


logging.basicConfig(
    filename=f"{get_logs_path()}\\app.log",
    level=logging.INFO,
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
