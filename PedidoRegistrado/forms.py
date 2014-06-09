from django import forms
from django.forms import Textarea, TextInput
from PedidoRegistrado.models import DomicilioSearch, Pedido


class DomicilioSearchForm(forms.ModelForm):
    class Meta:
        model = DomicilioSearch
        fields = ['localidad', 'barrio', 'direccion', 'numero_direccion',
                  'piso', 'depto', 'codigo_postal', 'servicio']
        widgets = {
            "numero_direccion": TextInput(attrs={'class': 'cajaschicas'}),
            "piso": TextInput(attrs={'class': 'cajaschicas'}),
            "depto": TextInput(attrs={'class': 'cajaschicas'}),
            "codigo_postal": TextInput(attrs={'class': 'cajaschicas'}),
        }


class PagoForm(forms.Form):
    importePagar = forms.FloatField(label='', required=True,
                                    widget=forms.TextInput(
                                        attrs={'class': 'cajaschicas'}))

    def __init__(self, *args, **kwargs):
        self.precioTotal = kwargs.get('precioTotal', None)
        if kwargs['precioTotal'] is not None:
            del kwargs['precioTotal']
        super(PagoForm, self).__init__(*args, **kwargs)

    def clean_importePagar(self):
        importePagar = self.cleaned_data['importePagar']
        if importePagar >= self.precioTotal:
            pass
        else:
            raise forms.ValidationError('Su importe es menor al total')
        return importePagar


class HoraPedidoForm(forms.Form):
    horaPedir = forms.TimeField(label='', help_text="Hora : hh:mm",
                                widget=forms.TextInput(
                                    attrs={'class': 'cajaschicas'}))
