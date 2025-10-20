from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import YouTubeVideo, YouTubePlaylist
from .utils import get_playlist_videos

def player(request):
    videos = YouTubeVideo.objects.all()
    playlists = YouTubePlaylist.objects.all()
    playlist_items = {p.playlist_id: get_playlist_videos(p.playlist_id) for p in playlists}
    return render(request, "player/home.html", {"videos": videos, "playlists": playlist_items})
