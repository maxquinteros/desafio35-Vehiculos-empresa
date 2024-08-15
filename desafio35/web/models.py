from django.db import models


# Create your models here.
class Chofer(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(blank=True, null=True)
    creacion_registro = models.DateField(blank=True, null=True)
    vehiculo = models.OneToOneField('Vehiculo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chofer'


class Registrocontabilidad(models.Model):
    fecha_compra = models.DateField()
    valor = models.FloatField()
    vehiculo = models.OneToOneField('Vehiculo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrocontabilidad'


class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vehiculo'