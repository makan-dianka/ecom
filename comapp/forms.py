from django import forms
from django.forms import ModelForm
from . models import client

# cette class n'est pas en service 
class ClientForm(ModelForm):
    class Meta:
        model = client
        fields = ['item', 'votre_nom']

        # widgets = {
        #     'votre_nom': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'author', 'type':'hidden', 'placeholder': 'Nom d\'utilisateur'}),
        #     'item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id arcticle', 'id':'article'}),
        
        # }