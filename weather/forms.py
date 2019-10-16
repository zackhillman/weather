from django import forms
from .models import User
from dal import autocomplete


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'location']
        widgets = {
            'location': autocomplete.ModelSelect2(url='select2_fk') #for autocomplete view
        }