from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GameOfUserSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class AddGameUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = GameOfUserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
