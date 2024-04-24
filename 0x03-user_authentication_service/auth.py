#!/usr/bin/env python3
"""
Auth module
"""

from db import DB, User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            User: The created User object.

        Raises:
            ValueError: If a user already exists with the given email.
        """
        try:
            # Check if user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # No user found with the given email, proceed with registration
            hashed_password = self._hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

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
