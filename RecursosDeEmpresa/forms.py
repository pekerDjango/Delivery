from django import forms
from RecursosDeEmpresa.models import Empleado, Sucursal
from django.forms import TextInput

#class EmpleadoForm(forms.Form):
#    Buscar   = forms.CharField(label='', initial='Buscar', widget=forms.TextInput(), required=False)
    
class addEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        exclude = {'legajo',}
        
class DeleteEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = []
        
class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        widgets = {                  
                  "codigo_postal":TextInput(attrs={'class':'input-mini'})
                  }
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model =  Empleado
        widgets = {                  
                  "depto":TextInput(attrs={'class':'input-mini'}),
                  "codigo_postal":TextInput(attrs={'class':'input-mini'})
                  }
  
