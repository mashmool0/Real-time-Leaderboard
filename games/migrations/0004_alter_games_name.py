# Generated by Django 5.1.2 on 2024-11-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_gamesofusers_delete_gamesoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]