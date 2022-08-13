from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Message


class CustomUserAdmin(admin.ModelAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = Message
    list_display = ('username', 'room', 'content')
    list_filter = ('username', 'room', 'content')
    fieldsets = (
        (None, {'fields': ('username', 'room', 'content')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'room', 'content')}
         ),
    )
    search_fields = ('username', 'room')
    ordering = ('username', 'room')


admin.site.register(Message, CustomUserAdmin)
