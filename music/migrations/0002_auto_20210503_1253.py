# Generated by Django 3.2 on 2021-05-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='track',
            name='duration',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='track',
            name='times_played',
            field=models.IntegerField(default=0),
        ),
    ]
