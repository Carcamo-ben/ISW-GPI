from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(SOLICITUDES)
admin.site.register(Solicitud_helper)
admin.site.register(BODEGUEROS)
admin.site.register(BODEGAS)
admin.site.register(MATERIALES)
admin.site.register(PROVEEDORES)