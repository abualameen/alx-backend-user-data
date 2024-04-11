#!/usr/bin/env python3
"""
this is a module for Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns the hashed passwd"""
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ the function validates the password """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
