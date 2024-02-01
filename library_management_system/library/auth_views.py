"""
auth_views.py

This module contains views related to user authentication, including login and signup.

LoginView:
    Inherits from TokenObtainPairView provided by the rest_framework_simplejwt library.
    Responsible for handling user login and providing JWT tokens upon successful authentication.
    Extends the default behavior to include the user_id in the response for convenience.

    - POST:
        - Endpoint: /library/login/
        - Parameters:
            - username (string): User's username
            - password (string): User's password
        - Response:
            - 200 OK: Successful login, includes access and refresh tokens. Additional user_id is appended to the response data.

SignupView:
    Inherits from APIView provided by the Django Rest Framework.
    Responsible for handling user signup and creating a new user in the system.

    - POST:
        - Endpoint: /library/signup/
        - Parameters:
            - username (string): Desired username for the new user
            - password (string): Password for the new user
        - Response:
            - 201 Created: User created successfully.
            - 400 Bad Request: Username already exists.

Permissions:
    Both LoginView and SignupView allow any user (including unauthenticated users) to access their respective endpoints.
    This is achieved by setting the permission_classes attribute to (permissions.AllowAny,).

Note:
    - TokenObtainPairView is part of the rest_framework_simplejwt library, providing a standard implementation for JWT token generation.
    - The LoginView extends this functionality to include the user_id in the response, facilitating user identification in subsequent requests.
    - The SignupView checks for existing usernames and prevents creating a new user with an existing username.

Usage:
    - Include these views in your Django app's URL configuration.
    - Ensure proper endpoint configuration for login and signup in your app's urls.py file.
    - Integrate token-based authentication with your application to secure sensitive endpoints.

Author: Suyamoon Pathak
Date: 01-02-2024
"""


from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import NotFound, ValidationError

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            if response.status_code == status.HTTP_200_OK:
                user = User.objects.get(username=request.data.get('username'))
                response.data['user_id'] = user.id
            return response
        except User.DoesNotExist:
            raise NotFound('User not found')

class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            if User.objects.filter(username=username).exists():
                raise ValidationError({'error': 'Username already exists'})
            user = User.objects.create_user(username=username, password=password)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
