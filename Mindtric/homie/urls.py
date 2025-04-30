from django.urls import path
from .views import home_view,inder,about,games_index,shells,lock,finder,reset,sym,needle,Team,Music,Self,Book
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('index/', inder, name='inder'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', about, name='about'),
    path('games_index/', games_index, name='games_index'),
    path('shells/', shells, name='shells'),
    path('lock/', lock, name='lock'),
    path('finder/', finder, name='finder'),
    path('reset/', reset, name='reset'),
    path('sym/', sym, name='sym'),
    path('needle/', needle, name='needle'),
    path('Team/', Team, name='Team'),
    path('Music/', Music, name='Music'),
    path('Self/', Self, name='Self'),
    path('Book/', Book, name='Book'),
]
