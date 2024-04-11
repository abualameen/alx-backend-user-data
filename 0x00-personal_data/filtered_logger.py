import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format method to filter values in incoming log records """
        for field in self.fields:
            pattern = re.escape(field) + r'=[^' + \
                re.escape(self.SEPARATOR) + r']+'
            record.msg = re.sub(
                pattern, field + '=' + self.REDACTION, record.msg)
        return super().format(record)


# Define the PII_FIELDS constant
PII_FIELDS = ("field1", "field2", "field3", "field4", "field5")


def get_logger() -> logging.Logger:
    """Create and configure a logger named 'user_data'."""
    # Create a new logger named 'user_data'
    logger = logging.getLogger("user_data")

    # Set the logging level to INFO
    logger.setLevel(logging.INFO)

    # Prevent messages from being propagated to other loggers
    logger.propagate = False

    # Create a StreamHandler
    stream_handler = logging.StreamHandler()

    # Set the formatter for the StreamHandler to RedactingFormatter
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))

    # Add the StreamHandler to the logger
    logger.addHandler(stream_handler)

    return logger


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str
                 ) -> str:
    """ Filter the log message obfuscated """
    for field in fields:
        pattern = re.escape(field) + r'=[^' + \
            re.escape(separator) + r']+'
        message = re.sub(
            pattern, field + '=' + redaction, message)
    return message
