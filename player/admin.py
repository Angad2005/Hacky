from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import YouTubeVideo, YouTubePlaylist

@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ("title", "video_id")
    search_fields = ("title", "video_id")

@admin.register(YouTubePlaylist)
class YouTubePlaylistAdmin(admin.ModelAdmin):
    list_display = ("title", "playlist_id")
    search_fields = ("title", "playlist_id")
