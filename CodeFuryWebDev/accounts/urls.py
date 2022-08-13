from django.contrib import admin
from django.urls import path

from .views import accountsHome, loginPage, logoutPage, signupPage

urlpatterns = [
    path('', accountsHome, name='accountsHome'),
    path('admin/', admin.site.urls),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('signup/', signupPage, name='signup'),
]
