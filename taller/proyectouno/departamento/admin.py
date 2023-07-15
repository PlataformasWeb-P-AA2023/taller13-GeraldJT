from django.contrib import admin

from departamento.models import *

class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion')

admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('nombre_Propietario', 'costo', 'numero_cuartos', 'edificio')

    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)