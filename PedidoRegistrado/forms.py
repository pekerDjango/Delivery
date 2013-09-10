from django import forms
from django.forms import Textarea, TextInput
from PedidoRegistrado.models import DomicilioSearch

class DomicilioSearchForm(forms.ModelForm):
    class Meta:
        model = DomicilioSearch
        fields = ['localidad', 'barrio', 'direccion', 'numero_direccion', 'piso', 'depto', 'codigo_postal']
        widgets = {
                  "piso": TextInput(attrs={'width':'40px'}),
                  "depto":TextInput(attrs={'size':'50'})
                  }
#        piso = forms.CharField(widget=forms.TextInput(attrs={'size':'60','maxlength':'70'})) 






    