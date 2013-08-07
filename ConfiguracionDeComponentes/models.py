from django.db import models
from django.contrib.auth.models import User
from RecursosDeEmpresa.models import Empleado

class Usuario (User):
    empleado = models.OneToOneField(Empleado)

# Create your models here.
