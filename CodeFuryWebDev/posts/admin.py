from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import PostModel


class CustomUserAdmin(admin.ModelAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = PostModel
    list_display = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ()}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ()}
         ),
    )
    search_fields = ()
    ordering = ()


admin.site.register(PostModel, CustomUserAdmin)
