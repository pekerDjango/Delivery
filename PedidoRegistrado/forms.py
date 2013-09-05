from django import forms
from PedidoRegistrado.models import DomicilioSearch

class DomicilioSearchForm(forms.ModelForm):
    class Meta:
        model = DomicilioSearch
        fields = ['localidad', 'barrio', 'direccion', 'numero_direccion', 'piso', 'depto', 'codigo_postal']






    