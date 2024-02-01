from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(username=request.data.get('username'))
            response.data['user_id'] = user.id
        return response


class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

    