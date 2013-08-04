from django import forms
from RecursosDeEmpresa.models import Empleado

class EmpleadoForm(forms.Form):
    Buscar   = forms.CharField(label='', initial='Buscar', widget=forms.TextInput(), required=False)
    
class addEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
  
