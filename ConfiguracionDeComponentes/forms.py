#encoding:utf-8
from django import forms
from ConfiguracionDeComponentes.models import Cliente, ExUserProfile
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class ClienteForm(forms.ModelForm):
    class Meta: 
        model = Cliente

from registration.forms import RegistrationForm
 
class ExRegistrationForm(RegistrationForm):
    is_human = forms.BooleanField(label = "Are you human?:")
