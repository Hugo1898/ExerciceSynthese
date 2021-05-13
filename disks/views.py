from django.shortcuts import render
from .models import *


def voir_albums(request):
    return render(request, 'disks/voir_albums.html', {'albums': Album.objects.all()})


def voir_tracks(request, album_id):
    return render(request, 'disks/voir_tracks.html', {'tracks': Track.objects.filter(album=album_id)})


def voir_recherche(request, search):
    return render(request, 'disks/voir_recherche.html',
                  {'search': search, 'search_result': Album.objects.filter(title__contains=search)})

