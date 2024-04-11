#!/usr/bin/env python3
"""
Filtered Logger Module
"""

import re
from typing import List


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format log record"""
        record.msg = filter_datum(
                                    self.fields,
                                    self.REDACTION,
                                    record.msg,
                                    self.SEPARATOR
                                    )
        return super().format(record)
