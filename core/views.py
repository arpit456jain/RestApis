from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import SignupSerializer,LoginSerializer
from core.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            project_name = request.data.get("project_name", None)
            UserProfile.objects.create(user=user, project=project_name)
            return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(username=serializer.validated_data['username'])
                if check_password(serializer.validated_data['password'], user.password):
                   try:
                        project_name = request.data.get("project_name", None)
                        if user.userprofile.project != project_name or project_name == None:
                            return Response({'error': 'Not authorized for this project'}, status=status.HTTP_403_FORBIDDEN)
                   except UserProfile.DoesNotExist:
                        return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)
                   token = RefreshToken.for_user(user)
                   return Response({
                        'message': 'Login successful',
                        'user_id': user.id,
                        'username': user.username,
                        'name': user.first_name,
                        'access': str(token.access_token),
                        'refresh': str(token),
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
