from django.shortcuts import render

from .models import Artist, Song

def artist_list(request):
	artists = Artist.objects.all()
	return render(request, 'tunr/artist_list.html', {'artists': artists})

def artist_detail(request, pk):
	artist = Artist.objects.get(id=pk)
	return render(request, 'tunr/artist_detail.html', {'artist': artist})

def song_list(request):
	songs = Song.objects.all()
	return render(request, 'tunr/song_list.html', {'songs': songs})

def song_detail(request, pk):
	song = Song.objects.get(id=pk)
	return render(request, 'tunr/song_detail.html', {'song': song})