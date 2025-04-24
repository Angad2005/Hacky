from django.urls import path
from .views import home_view,inder,about,games_index,Shells,Lock,Finder,Reset,Sym,needle,Team,Music,Self,Book
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('index/', inder, name='inder'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', about, name='about'),
    path('games_index/', games_index, name='games_index'),
    path('Shells/', Shells, name='Shells'),
    path('Lock/', Lock, name='Lock'),
    path('Finder/', Finder, name='Finder'),
    path('Reset/', Reset, name='Reset'),
    path('Sym/', Sym, name='Sym'),
    path('needle/', needle, name='needle'),
    path('Team/', Team, name='Team'),
    path('Music/', Music, name='Music'),
    path('Self/', Self, name='Self'),
    path('Book/', Book, name='Book'),
]
