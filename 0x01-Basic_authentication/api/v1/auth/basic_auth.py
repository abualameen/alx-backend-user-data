#!/usr/bin/env python3
"""
this module is the basic auth class

"""

from models.user import User
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar


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
                isinstance(decoded_base64_authorization_header, str) \
                or ":" not in decoded_base64_authorization_header:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_password = decoded_base64_authorization_header.split(
           ':', 1)
        return user_email, user_password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """this function checks user obj from creden"""
        if user_email is None or not isinstance(user_email, str) or \
                user_pwd is None or not isinstance(user_pwd, str):
            return None
        user_list = User.search({'email': user_email})
        if not user_list:
            return None
        user = user_list[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user"""
        if request is None:
            return None
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None
        email, pwd = self.extract_user_credentials(decoded_auth)
        if email is None or pwd is None:
            return None
        user = self.user_object_from_credentials(email, pwd)
        return user
