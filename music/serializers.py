from rest_framework import serializers
from .models import Track, Album, Artist



class Artistserializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('name', 'age')

class Albumserializer(serializers.ModelSerializer):


    class Meta:
        model = Album
        fields = ('name', 'genre')


class Trackserializer(serializers.ModelSerializer):


    class Meta:
        model = Track
        fields = ('name', 'duration')