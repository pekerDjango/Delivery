from django import forms

class EmpleadoForm(forms.Form):
    Buscar   = forms.CharField(label='', initial='Buscar', widget=forms.TextInput(), required=False)
  
