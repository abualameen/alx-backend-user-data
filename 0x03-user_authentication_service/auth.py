#!/usr/bin/env python3
"""
Auth module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    # Encode password string to bytes
    password_bytes = password.encode('utf-8')
    # Generate salted hash of the password using bcrypt
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    return hashed_password
