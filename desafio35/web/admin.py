from django.contrib import admin
from .models import Vehiculo, Chofer, Registrocontabilidad
# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Chofer)
admin.site.register(Registrocontabilidad)