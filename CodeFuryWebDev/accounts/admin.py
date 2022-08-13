from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active', 'f_name', 'l_name', 'gender', 'dob')
    list_filter = ('username', 'email', 'is_staff', 'is_active', 'f_name', 'l_name', 'gender', 'dob')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'f_name', 'l_name', 'gender', 'dob')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active',
                       'f_name', 'l_name', 'gender', 'dob')}
         ),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)
