from django.urls import path, include

from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/',  login, name='login'),
    path('register/',  register, name='register'),
]
