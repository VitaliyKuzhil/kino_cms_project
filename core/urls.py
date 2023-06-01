from django.urls import path, include
from .views import *

urlpatterns = [
    path('', base_user, name='base_user'),
    path('user/', include(('user.urls', 'user'), namespace='user'), name='user'),  # Include urls with users.urls
    path('adminlte/', base_admin, name='base_admin'),
]
