#!/usr/bin/env python3
"""
this module is the SessionAut
"""

from api.v1.auth.auth import Auth
import uuid
from typing import TypeVar
from models.user import User


T = TypeVar('T')


class SessionAuth(Auth):
    """ this is the session auth class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ this method creats a session"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ this function retrieves the session id """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> str:
        """ This method """
        if not request:
            return None
        session_id = request.cookies.get('_my_session_id')
        if not session_id:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None
        return User.get(user_id)
