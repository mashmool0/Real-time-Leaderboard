from unicodedata import name

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GameOfUserSerializer, UpdateGameScoreSerializer
from rest_framework.permissions import IsAuthenticated
from .models import GamesOfUsers


# Create your views here.

class CreateGameUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = GameOfUserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateGameScoreView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, game_name):
        try:
            game = GamesOfUsers.objects.get(games__name=game_name, user=request.user)
        except GamesOfUsers.DoesNotExist:
            return Response({"message": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateGameScoreSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Game score updated successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)