from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Track, Album, Artist
from .serializers import Trackserializer, Albumserializer, Artistserializer
from base64 import b64encode
import json 


def index(request):
    return HttpResponse("<h1>Bienvenido</h1>")


@api_view(['GET'])
def Artistmethod(request):
    api_urls = {
        'List': '/artist-list/',
        'Detail View' : '/artist-detail/<str:pk>/',
        'Create': '/artist-create/',
        'Delete': 'artist-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET', 'POST'])
def Artistlist(request):

    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = Artistserializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        body = request.data
        name = body['name']
        age = body['age']
        new_id = b64encode(name.encode()).decode('utf-8')
        newartist = {
                    "id": f'{new_id[:22]}',
                    "name": f'{name}',
                    "age": age,
                    "albums": f'https://apihost.com/artists/{new_id}/albums',
                    "tracks": f'https://apihost.com/artists/{new_id}/tracks',
                    "self_url": f'https://apihost.com/artists/{new_id}'
                    }
        serializer = Artistserializer(data=newartist)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def Artistdetail(request, pk):
    if request.method == 'GET':
        artists = Artist.objects.get(id=pk)
        serializer = Artistserializer(artists, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        artists = Artist.objects.get(id=pk)
        artists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Artistalbums(request, pk):
    if request.method == 'GET':
        albums = get_object_or_404(Album, artist_id=pk)
        serializer = Albumserializer(albums, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        name = data['name']
        genre = data['genre']
        new_id = b64encode(name.encode()).decode('utf-8')
        newalbum = {
                    "id": f'{new_id[:22]}',
                    "artist_id": pk,
                    "name": f'{name}',
                    "genre": genre,
                    "artist": f'https://apihost.com/albums/{new_id}/artists',
                    "tracks": f'https://apihost.com/albums/{new_id}/tracks',
                    "self_url": f'https://apihost.com/albums/{new_id}'
                    }
        serializer = Albumserializer(data=newalbum)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Artisttracks(request, pk):
    albums = Album.objects.get(artist_id=pk)
    serializer = Albumserializer(albums, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def Albumlist(request):
    albums = Album.objects.all()
    serializer = Albumserializer(albums, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def Albumdetail(request, pk):
    if request.method == 'GET':
        albums = Album.objects.get(id=pk)
        serializer = Albumserializer(albums, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        albums = Album.objects.get(id=pk)
        albums.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def Albumtracks(request, pk):
    if request.method == 'GET':
        tracks = get_object_or_404(Track, album_id=pk)
        serializer = Trackserializer(tracks, many=False)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        name = data['name']
        duration = data['duration']
        new_id = b64encode(name.encode()).decode('utf-8')
        newtrack = {
                    "id": f'{new_id[:22]}',
                    "album_id": pk,
                    "name": f'{name}',
                    "duration": duration,
                    "artist": f'https://apihost.com/tracks/{new_id}/artists',
                    "album": f'https://apihost.com/tracks/{new_id}/albums',
                    "self_url": f'https://apihost.com/tracks/{new_id}'
                    }
        serializer = Trackserializer(data=newtrack)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Tracklist(request):
    tracks = Track.objects.all()
    serializer = Trackserializer(tracks, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])

def Trackdetail(request, pk):
    if request.method == 'GET':
        tracks = Track.objects.get(id=pk)
        serializer = Trackserializer(tracks, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        tracks = Track.objects.get(id=pk)
        tracks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)













