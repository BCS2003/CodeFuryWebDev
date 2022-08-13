from django.urls import path

from .views import home, creatPost

urlpatterns = [
    path('', home, name='postsHome'),
    path('create/', creatPost, name='postCreate'),
]
