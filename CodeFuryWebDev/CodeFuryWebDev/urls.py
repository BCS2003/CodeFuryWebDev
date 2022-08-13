from django.urls import path, include

from .views import codeFuryWebDevHome

urlpatterns = [
    path('accounts/', include("accounts.urls")),
    path('chats/', include("chats.urls")),
    path('', codeFuryWebDevHome, name='codeFuryWebDevHome'),
]
