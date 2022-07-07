from django.db import models
from django.conf import settings
from django.utils import timesince

# Create your models here.

class persona(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    generos = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro")
    )
    genero = models.CharField(max_length=50, choices=generos)
    identificacion = models.CharField(max_length=100, null=False)
    select_tipo_identificacion = (
        ("C", "Cedula"),
        ("R", "RUC"),
        ("P", "Pasaporte")
    )
    tipo_identificacion = models.CharField(max_length=50, choices= select_tipo_identificacion)
    tipo_estado_civil = (
        ("S", "Soltero"),
        ("C", "Casado"),
        ("D", "Divorciado"),
        ("V", "Viudo")
    )
    estado_civil = models.CharField(max_length=50, choices= tipo_estado_civil)

    class Meta:
        abstract = True

class cliente(persona):
    id_persona = models.IntegerField()
    numero_carga_familiares = models.IntegerField()
    fecha_residencia =  models.DateTimeField(auto_now=True)
    lista_tipo_cliente = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    )
    tipo_cliente = models.CharField(max_length=50, choices= lista_tipo_cliente)