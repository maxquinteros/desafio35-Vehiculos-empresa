import os
import sys
import django
from datetime import date

# Configura el entorno de Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desafio35.settings")
django.setup()

from web.models import Chofer, Registrocontabilidad, Vehiculo


def crear_vehiculo():
    vehiculo = Vehiculo(patente="789012", marca="Toyota", modelo="Corolla", year=1986)
    vehiculo.save()
    print(f"Vehículo creado con la patente: {vehiculo.patente}")


crear_vehiculo()


def crear_chofer():
    vehiculo = Vehiculo.objects.get(patente="789012")
    chofer = Chofer(
        rut="200000001",
        nombre="Adam",
        apellido="Smith",
        activo=True,
        creacion_registro=date(2024, 8, 14),
        vehiculo=vehiculo,
    )
    chofer.save()
    print(f"Chofer creado con el rut: {chofer.rut} en el vehículo: {vehiculo.patente}")


crear_chofer()


def crear_registro_contable():
    vehiculo = Vehiculo.objects.get(patente="789012")
    registrocontabilidad = Registrocontabilidad(fecha_compra=date(2024, 8, 14), vehiculo=vehiculo, valor=500)
    registrocontabilidad.save()
    print(f"Registro contable creado para el vehículo: {vehiculo.patente}")


crear_registro_contable()

def deshabilitar_chofer():
    chofer = Chofer.objects.get(rut="200000001")
    chofer.activo = False
    chofer.save()
    print(f"Chofer deshabilitado con el rut: {chofer.rut}")
    

deshabilitar_chofer()

def deshabilitar_vehiculo():
    vehiculo = Vehiculo.objects.get(patente="789012")
    vehiculo.activo = False
    vehiculo.save()
    print(f"Vehiculo deshabilitado con la patente: {vehiculo.patente}")

deshabilitar_vehiculo()

def habilitar_chofer():
    chofer = Chofer.objects.get(rut="200000001")
    chofer.activo = True
    chofer.save()
    print(f"Chofer habilitado con el rut: {chofer.rut}")

habilitar_chofer()

def habilitar_vehiculo():
    vehiculo = Vehiculo.objects.get(patente="789012")
    vehiculo.activo = True
    vehiculo.save()
    print(f"Vehiculo habilitado con la patente: {vehiculo.patente}")

habilitar_vehiculo()

def obtener_vehiculo():
    vehiculo = Vehiculo.objects.get(patente="789012")
    print(f"Vehiculo obtenido con la patente: {vehiculo.patente}")

obtener_vehiculo()

def obtener_chofer():
    chofer = Chofer.objects.get(rut="200000001")
    print(f"Chofer obtenido con el rut: {chofer.rut}")

obtener_chofer()

def asignar_chofer_a_vehiculo():
    chofer = Chofer.objects.get(rut="200000001")
    vehiculo = Vehiculo.objects.get(patente="789012")
    chofer.vehiculo = vehiculo
    chofer.save()
    print(f"Chofer con rut {chofer.rut} asignado al vehiculo con la patente: {vehiculo.patente}")

asignar_chofer_a_vehiculo()

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f"Patente: {vehiculo.patente}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, year: {vehiculo.year}")

imprimir_datos_vehiculos()