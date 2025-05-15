from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('inder/', inder, name='inder'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', about, name='about'),
    path('games_index/', games_index, name='games_index'),
    path('Team/', Team, name='Team'),
    path('Music/', Music, name='Music'),
    path('Self/', Self, name='Self'),
    path('Book/', Book, name='Book'),
    #OCD
    path('Shells/', Shells, name='Shells'),
    path('Lock/', Lock, name='Lock'),
    path('Finder/', Finder, name='Finder'),
    path('Reset/', Reset, name='Reset'),
    path('Sym/', Sym, name='Sym'),
    path('needle/', needle, name='needle'),
    #Dyslexic
    path('wordpuzzle/', wordpuzzle, name='wordpuzzle'),
    path('wordbuilder/', wordbuilder, name='wordbuilder'),
    path('voyager/', voyager, name='voyager'), 
    path('symphony/', symphony, name='symphony'), 
    path('memmatch/', memmatch, name='memmatch'),   
    #Anxiety
    path('zengarden/', zengarden, name='zengarden'),   
    path('breath/', breath, name='breath'),   
    path('soundscape/', soundscape, name='soundscape'),
    path('gentlepuzzle/', gentlepuzzle, name='gentlepuzzle'),
    path('jigsaw/', jigsaw, name='jigsaw'),
    #Depression
    path('metaphor/', metaphor, name='metaphor'),
    path('constellation/', constellation, name='constellation'),
    path('shadowwalk/', shadowwalk, name='shadowwalk'),
    path('growthgarden/', growthgarden, name='growthgarden'),
    path('thoughtfilter/', thoughtfilter, name='thoughtfilter'),
    #Stress
    path('bubbleshooter/', bubbleshooter, name='bubbleshooter'),
    path('hexaflow/', hexaflow, name='hexaflow'),
    path('colortherapy/', colortherapy, name='colortherapy'),
    path('pattern/', pattern, name='pattern'),
    path('tetris/', tetris, name='tetris'),
#something
]
