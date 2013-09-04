from django.contrib import admin
from PedidoRegistrado.models import Servicio
from form_utils.widgets import ImageWidget
from django.db import models
from django.forms import TextInput, Textarea

class ServicioAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.ImageField: {'widget': ImageWidget},     
    } 

admin.site.register(Servicio, ServicioAdmin)