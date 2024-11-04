from rest_framework import serializers
from .models import GamesOfUsers, Games


class GameOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamesOfUsers
        fields = ('user', 'games', 'score',)

    def validate(self, attrs):
        if Games.objects.filter(name=attrs['game']).exists():
            return attrs
        raise serializers.ValidationError({"games": "This game Doesnt Exist!!!"})

    def create(self, validated_data):
        game = GamesOfUsers.objects.get(validated_data['game'])
        user = self.context['request'].user
        games_of_users = GamesOfUsers(
            user=user,
            games=game,
            score=validated_data['score']
        )

        games_of_users.save()
        return games_of_users
