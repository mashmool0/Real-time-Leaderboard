from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import OnlyUnAuthenticatedUserPermission


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Create your views here.

class RegisterView(APIView):
    serializer_class = [UserSerializer]
    permission_classes = [OnlyUnAuthenticatedUserPermission]

    def post(self, request):
        ser = UserSerializer(data=request.data)
        if ser.is_valid():
            user = ser.save()
            data = get_tokens_for_user(user)

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
