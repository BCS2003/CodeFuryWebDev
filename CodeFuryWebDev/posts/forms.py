from .models import PostModel
from django import forms


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('startup_name', 'short_disc', 'fin_details', 'amount',
                  'equity', 'detailed_disc')
