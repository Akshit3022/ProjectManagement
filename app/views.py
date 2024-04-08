from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# from django.http import JsonResponse
from app.permissions import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    def post(self, request, format=None):
        serializer = RegiterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, 'Successful': 'Registration Successful..!'}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, "Successful":"Login Successful..!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid Credentials..!"}, status=status.HTTP_401_UNAUTHORIZED)    
            
        
class CustomUserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,format=None):
        serializer = CustomUserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK) 


class ChangePasswordView(APIView):  
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(data=request.data, context={'user' :request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"Successful":"Change Password Successful..!"}, status=status.HTTP_200_OK)
    
    
class SendResetPasswordEmaiView(APIView):
    def post(self, request):
        serializer = SendResetPasswordEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"Successful":"password reset link is sent..!"}, status=status.HTTP_200_OK)


class CustomUserResetPasswordView(APIView):
    def post(self, request, user_id, token, format=None):
        serializer = CustomUserResetPasswordSerializer(data=request.data, context={'user_id': user_id, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({"Successful":"password reset successful..!"}, status=status.HTTP_200_OK)
