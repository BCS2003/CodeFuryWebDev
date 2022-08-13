from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import PostModel


class CustomUserAdmin(admin.ModelAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = PostModel
    list_display = ('startup_name', 'short_disc', 'fin_details', 'amount',
                    'equity', 'detailed_disc')
    list_filter = ('startup_name', 'short_disc', 'fin_details', 'amount',
                   'equity', 'detailed_disc')
    fieldsets = (
        (None, {'fields': ('startup_name', 'short_disc', 'fin_details', 'amount',
                           'equity', 'detailed_disc')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('startup_name', 'short_disc', 'fin_details', 'amount',
                       'equity', 'detailed_disc')}
         ),
    )
    search_fields = ('equity', 'startup_name', 'amount',)
    ordering = ('equity',)


admin.site.register(PostModel, CustomUserAdmin)
