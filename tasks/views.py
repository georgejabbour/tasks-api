from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from tasks.models import *
from rest_framework_simplejwt.tokens import RefreshToken

def get_user_by_session_token(session_token):
    userSession = Session.objects.filter(sessionToken=session_token)
    if not userSession:
        return None
    user_id = userSession[0].userId
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None
    return user

class ExchangeTokenView(APIView):
    def post(self, request):
        session_token = request.data.get('session_token')
        print('session_token ExchangeTokenView', session_token)
        if not session_token:
            return Response({"error": "Session token is required"}, status=status.HTTP_400_BAD_REQUEST)

        userSession = Session.objects.filter(sessionToken=session_token)

        if not userSession:
            return Response({"error": "Invalid session token in ExchangeTokenView"}, status=status.HTTP_400_BAD_REQUEST)

        user = get_user_by_session_token(session_token)
        print('user', user)   
        # Generate or retrieve token
        # Issue JWT for the user
        refresh = RefreshToken.for_user(user)
        print('refresh', refresh)
        access_token = str(refresh.access_token)
        print('access_token', access_token)
        return Response({
            'access_token': access_token,
            'refresh_token': str(refresh)
        }, status=200)
    

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refreshToken')
        try:
            old_token = RefreshToken(refresh_token)
            user = User.objects.get(id=old_token.get(settings.SIMPLE_JWT['USER_ID_CLAIM'])) 

            new_refresh_token = RefreshToken.for_user(user)
            access_token = str(new_refresh_token.access_token)

            return Response({
                'access_token': access_token,
                'refresh_token': str(new_refresh_token)
            })
        except Exception as e:
            print('Exception', e) 
            return Response({"error": str(e)}, status=400)
