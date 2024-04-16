#!/usr/bin/env python3
"""
this module is the basic auth class

"""


from api.v1.auth.auth import Auth
import base64
import binascii


class BasicAuth(Auth):
    """this class the basic auth"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ this function return base64 string """
        if authorization_header is None or not \
                isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        credentials = authorization_header.split(' ')
        if len(credentials) != 2:
            return None
        # try:
            # return base64.b64decode(credentials[1]).decode('utf-8')
        # except binascii.Error:
        return credentials[1]
