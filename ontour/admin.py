from django.contrib import admin
from .models import Pagos, Tipo_pago, paquete_turistico, colegio, curso, estado_pago, Alumno, Genero, Apoderado, contrato

# Register your models here.

admin.site.register(Pagos)
admin.site.register(Tipo_pago)
admin.site.register(paquete_turistico)
admin.site.register(colegio)
admin.site.register(curso)
admin.site.register(estado_pago)
admin.site.register(Alumno)
admin.site.register(Genero)
admin.site.register(Apoderado)
admin.site.register(contrato)


