from django.urls import path
from .views import signup_view, login_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    
]

