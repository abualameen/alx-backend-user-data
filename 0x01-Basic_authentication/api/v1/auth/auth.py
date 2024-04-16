#!/usr/bin/env python3
"""
this is the module

"""

from typing import List, TypeVar
from flask import request


class Auth:
    """ Class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for the given path """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        # making sure that paths are slash tolerant
        path = path.rstrip("/") + "/"
        return path not in excluded_paths
        

    def authorization_header(self, request=None) -> str:
        """ Gets the Authorization header from the request """
        if request is None:
            return None
        if request.headers.get('Authorization') == None:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user from the request """
        return None
