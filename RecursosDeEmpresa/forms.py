from django import forms

class EmpleadoForm(forms.Form):
    Buscar   = forms.CharField(widget=forms.TextInput(), required=False)
  
