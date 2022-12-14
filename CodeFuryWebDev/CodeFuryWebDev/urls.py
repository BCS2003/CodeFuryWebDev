from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from .views import home

urlpatterns = [
    path('accounts/', include("accounts.urls")),
    path('chats/', include("chats.urls")),
    path('', home, name='codeFuryWebDevHome'),
    path('posts/', include("posts.urls"))
]
urlpatterns += staticfiles_urlpatterns()
