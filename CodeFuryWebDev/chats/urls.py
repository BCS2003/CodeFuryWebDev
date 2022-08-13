from django.urls import path

from .views import home, room

urlpatterns = [
    path('', home, name='chatsHome'),
    path('room/', room, name='room'),
]
