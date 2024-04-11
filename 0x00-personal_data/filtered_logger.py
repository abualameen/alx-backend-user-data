#!/usr/bin/env python3
"""
Filtered Logger Module
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    This function filters log messages by obfuscating specified fields.
    """
    for field in fields:
        # Constructing the regular expression
        # pattern to match the field and its value
        pattern = re.escape(field) + r'=[^' + re.escape(separator) + r']+'
        # Replacing the matched pattern with the redaction
        message = re.sub(pattern, field + '=' + redaction, message)
    return message
