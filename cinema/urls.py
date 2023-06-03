from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('sessions/', sessions, name='sessions'),
    path('list_films/', list_films, name='list_films'),
    path('list_cinemas/', list_cinemas, name='list_cinemas'),
]
