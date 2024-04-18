#!/usr/bin/env python3
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ This is the session auth class with
        expiration stored in the database """
    def create_session(self, user_id=None):
        """ Creates a session stored in the database """
        session_id = super().create_session(user_id)
        if session_id:
            new_session = UserSession(user_id=user_id, session_id=session_id)
            new_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Retrieves the user ID for a session ID from the database """
        if not session_id:
            return None
        user_session = UserSession.find_first('session_id', session_id)
        if not user_session:
            return None
        user_id = user_session.user_id
        created_at = user_session.created_at
        if self.session_duration <= 0:
            return user_id
        if not created_at:
            return None
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None
        return user_id

    def destroy_session(self, request=None):
        """ Destroys a session stored in the database based
            on the Session ID from the request cookie """
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_session = UserSession.find_first('session_id', session_id)
        if not user_session:
            return False
        user_session.delete()
        return True
