from django.urls import path, include

from .views import codeFuryWebDevHome

urlpatterns = [
    path('accounts/', include("accounts.urls")),
    path('', codeFuryWebDevHome, name='codeFuryWebDevHome'),
]
