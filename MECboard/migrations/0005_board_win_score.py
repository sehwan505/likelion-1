# Generated by Django 2.2.4 on 2019-11-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0004_auto_20191024_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='win_score',
            field=models.IntegerField(default=0),
        ),
    ]