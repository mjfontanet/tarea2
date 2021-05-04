from django.db import models

class Artist(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    name = models.CharField(max_length=300)
    age = models.IntegerField(default=0)
    albums = models.URLField(max_length=1000)
    tracks = models.URLField(max_length=1000)
    self_url = models.URLField(max_length=1000)

class Album(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    genre = models.CharField(max_length=300)
    artist = models.URLField(max_length=1000)
    tracks = models.URLField(max_length=1000)
    self_url = models.URLField(max_length=1000)

class Track(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    album_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    duration = models.FloatField(default=0)
    times_played = models.IntegerField(default=0)
    artist = models.URLField(max_length=1000)
    album = models.URLField(max_length=1000)
    self_url = models.URLField(max_length=1000)

