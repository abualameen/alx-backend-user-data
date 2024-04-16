#!/usr/bin/env python3

from typing import List, TypeVar
from flask import request


class Auth:
    """ Class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for the given path """
        return False

    def authorization_header(self, request=None) -> str:
        """ Gets the Authorization header from the request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user from the request """
        return None
