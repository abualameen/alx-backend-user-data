#!/usr/bin/env python3
""" this class the session expiration class"""
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth
import os


class SessionExpAuth(SessionAuth):
    """ This is the session auth class with expiration """
    def __init__(self):
        """ Initializes the SessionExpAuth """
        super().__init__()
        self.session_duration = int(os.getenv('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """ Creates a session with expiration """
        session_id = super().create_session(user_id)
        if session_id:
            self.user_id_by_session_id[session_id] = {
                'user_id': user_id,
                'created_at': datetime.now()
            }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Retrieves the user ID for a session ID """
        if not session_id:
            return None
        session_info = self.user_id_by_session_id.get(session_id)
        if not session_info:
            return None
        user_id = session_info.get('user_id')
        created_at = session_info.get('created_at')
        if self.session_duration <= 0:
            return user_id
        if not created_at:
            return None
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None
        return user_id
