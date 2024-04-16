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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ this decodes the autho header """
        if base64_authorization_header is None \
                or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """this function """
        if decoded_base64_authorization_header is None or not \
                isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_password = decoded_base64_authorization_header.split(
           ':', 1)
        return user_email, user_password