from django.db import models
from django.conf import settings
import requests

class YouTubeVideo(models.Model):
    video_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.title:
            url = "https://www.googleapis.com/youtube/v3/videos"
            params = {
                "id": self.video_id,
                "key": settings.YOUTUBE_API_KEY,
                "part": "snippet"
            }
            res = requests.get(url, params=params).json()
            if res.get("items"):
                self.title = res["items"][0]["snippet"]["title"]
        super().save(*args, **kwargs)

class YouTubePlaylist(models.Model):
    playlist_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.title:
            url = "https://www.googleapis.com/youtube/v3/playlists"
            params = {
                "id": self.playlist_id,
                "key": settings.YOUTUBE_API_KEY,
                "part": "snippet"
            }
            res = requests.get(url, params=params).json()
            if res.get("items"):
                self.title = res["items"][0]["snippet"]["title"]
        super().save(*args, **kwargs)
