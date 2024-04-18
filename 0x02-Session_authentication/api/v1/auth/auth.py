#!/usr/bin/env python3
"""
this is the module

"""

from os import getenv
from typing import List, TypeVar
from flask import request


class Auth:
    """ Class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for the given path """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        # making sure that paths are slash tolerant
        for excluded_path in excluded_paths:
            if excluded_path.endswith("*"):
                if path.startswith(excluded_path[:-1]):
                    return False
            else:
                if path == excluded_path:
                    return False
        # path = path.rstrip("/") + "/"
        # return path not in excluded_paths
        return True

    def authorization_header(self, request=None) -> str:
        """ Gets the Authorization header from the request """
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user from the request """
        return None

    def session_cookie(self, request=None):
        """ session cookie method """
        if request is None:
            return None
        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name)
