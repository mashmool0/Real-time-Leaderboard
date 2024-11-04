from rest_framework import serializers
from .models import GamesOfUsers, Games


class GameOfUserSerializer(serializers.ModelSerializer):
    game_name = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = GamesOfUsers
        fields = ('game_name', 'score',)

    def validate(self, attrs):
        # Check this game exist in Game database
        if not Games.objects.filter(name=attrs['game_name']).exists():
            raise serializers.ValidationError({"game_name": "this game Doesnt Exist"})

        # Check User had this game in his list of games or no
        game = Games.objects.get(name=attrs["game_name"])
        if GamesOfUsers.objects.filter(user=self.context['request'].user, games=game).exists():
            raise serializers.ValidationError(
                {"game": "you already have this game !! do you want update your score ?!"})
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        game = Games.objects.get(name=validated_data['game_name'])  # This will be the actual game instance
        games_of_users = GamesOfUsers(
            user=user,
            games=game,
            score=validated_data['score']
        )
        games_of_users.save()
        return {"Message": "Your Score And Your Game Saved"}
