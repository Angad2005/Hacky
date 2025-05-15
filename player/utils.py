import requests
from django.conf import settings

def get_video_details(video_id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "id": video_id,
        "key": settings.YOUTUBE_API_KEY,
        "part": "snippet"
    }
    res = requests.get(url, params=params).json()
    return res["items"][0]["snippet"] if res.get("items") else None

def get_playlist_videos(playlist_id):
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        "playlistId": playlist_id,
        "key": settings.YOUTUBE_API_KEY,
        "part": "snippet",
        "maxResults": 20
    }
    res = requests.get(url, params=params).json()
    return res.get("items", [])
