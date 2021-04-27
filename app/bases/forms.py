from django import forms
from django.forms import ModelForm
from .models import Contacto

        
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model=Contacto
        fields=["nombre", "email", "telefono", "mensaje"]