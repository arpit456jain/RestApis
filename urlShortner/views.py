from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import SignupSerializer,LoginSerializer
from core.models import UserProfile
from django.contrib.auth.models import User
from urlShortner.models import ShortenedURL
from urlShortner.serializers import ShortenedURLSerializer
from django.contrib.auth.hashers import check_password
import string, random
from django.http import HttpResponseRedirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404

class RedirectShortURLView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortenedURL, short_code=short_code)
        return HttpResponseRedirect(url_obj.original_url)


class GetOriginalURLView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_id = request.data.get("userId")
        short_code = request.data.get("short_code")

        if not user_id or not short_code:
            return Response({"error": "userId and short_code are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            url_obj = ShortenedURL.objects.get(short_code=short_code, user__id=user_id)
            return Response({"original_url": url_obj.original_url}, status=status.HTTP_200_OK)
        except ShortenedURL.DoesNotExist:
            return Response({"error": "No such URL found for this user."}, status=status.HTTP_404_NOT_FOUND)

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            UserProfile.objects.create(user=user, project="url_shortner")
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
                        if user.userprofile.project != "url_shortner":
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
    
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class ShortenURLView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_id = request.data.get("userId")
        original_url = request.data.get("original_url")

        # Check for missing data
        if not user_id or not original_url:
            return Response({'error': 'User and original URL required'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate unique short code
        short_code = generate_short_code()
        while ShortenedURL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()

        # Create entry
        url = ShortenedURL.objects.create(
            user_id=user_id,
            original_url=original_url,
            short_code=short_code
        )
        serializer = ShortenedURLSerializer(url)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

