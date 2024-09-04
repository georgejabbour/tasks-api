# tasks/authentication.py
from django.contrib.auth.backends import BaseBackend
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from .models import Session, User

class SessionTokenAuthentication(BaseBackend):
    def authenticate(self, request):
        # Extract the session token from the Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        # Ensure the header follows the Bearer <sessionToken> format
        try:
            prefix, session_token = auth_header.split(' ')
            if prefix.lower() != 'bearer':
                return None
        except ValueError:
            return None

        print('session_token', session_token)

        try:
            # Fetch the session object using the session_token
            session = Session.objects.get(sessionToken=session_token)
            print('session', session)

            # Check if the session is expired
            if session.expires < timezone.now():
                # delete the session
                session.delete()
                raise PermissionDenied("Session has expired")

            # Get the user ID from the session data
            print('user_id', session.userId)
            user = User.objects.get(pk=session.userId)
            print('user', user)
            return user, None

        except Session.DoesNotExist:
            print('Session.DoesNotExist')
            raise PermissionDenied("Invalid session token, Session.DoesNotExist")
        except User.DoesNotExist:
            print('User.DoesNotExist')
            raise PermissionDenied("User does not exist")

        return None, None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
