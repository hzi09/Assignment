from django.shortcuts import get_object_or_404, render, redirect
from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomUserProfileForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .serializers import CustomUserCreationSerializer, CustomUserProfileSerializer


class SignupAPIView(APIView) :
    permission_classes = [AllowAny]

    def post(self, request) :
        serializer = CustomUserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            auth_login(request, user)
            response_data = {
                'message': 'user create successful',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView) :
    permission_classes = [IsAuthenticated]
    
    def post(self, request) :
        auth_logout(request)
        response_data = {
            'message' : 'logout successful'
        }
        return Response(response_data, status=status.HTTP_200_OK)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username) :
        user = get_object_or_404(CustomUser, username=username)
        serializer = CustomUserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, username) :
        user = get_object_or_404(CustomUser, username=username)
        if user != request.user:
            return Response({'error': 'You do not have permission to edit this profile.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = CustomUserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)