from django.contrib import admin
from .models import Games, GamesOfUsers

# Register your models here.
admin.site.register(Games)
admin.site.register(GamesOfUsers)
