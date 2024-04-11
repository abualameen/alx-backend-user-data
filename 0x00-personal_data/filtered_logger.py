#!/usr/bin/env python3
"""
Filtered Logger Module
"""


import os
import mysql.connector
import logging
import re
from typing import List
from logging import StreamHandler


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
    stream_handler = StreamHandler()
    # Set the formatter for the StreamHandler to RedactingFormatter
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    # Add the StreamHandler to the logger
    logger.addHandler(stream_handler)
    return logger


def get_db():
    """Connect to the MySQL database using environment variables."""
    # Retrieve database credentials from environment variables
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    # Establish a connection to the database
    try:
        db = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL database: {err}")
        return None


def main():
    """Retrieve and display all rows in the users table."""
    # Get database connection
    db = get_db()
    if db:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users;")
        for row in cursor:
            filtered_row = {key: '***'
                            if key in PII_FIELDS
                            else value for key, value
                            in row.items()}
            ormatted_row = "; ".join(
                                        f"{key}={value}"for key,
                                        value in filtered_row.items())
            log_level = logging.getLogger().getEffectiveLevel()
            print(f"[HOLBERTON] user_data INFO {log_level} {formatted_row}")
        cursor.close()
        db.close()


# Define the PII_FIELDS constant
PII_FIELDS = ("name", "email", "phone", "ssn", "password")

if __name__ == "__main__":
    main()
