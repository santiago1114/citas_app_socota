from django.contrib import admin
from .models import Paciente, Cita, Turno, Media
from django.utils.safestring import mark_safe


def marcar_en_sala(instance):
    return f'''
        <a href="/cita/turno/save/{instance.pk}">Asignar turno</a>
    '''


def llamar_o_cerrar(instance):
    return f'''
        <a href="/turno/call/{instance.pk}" style="display: block; margin-bottom: 10px;">Llamar</a>
        <a href="/turno/close/{instance.pk}" style="display: block; margin-bottom: 10px;">Cerrar</a>
    '''
    
    
admin.site.register(Media)


class CitaInline(admin.StackedInline):
    model = Cita
    extra = 0 


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'tipo_documento', 'numero_documento', 'celular', 'fecha_de_registro')
    list_filter = ('nombres', 'apellidos', 'numero_documento')
    inlines = [CitaInline]
    
    
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'get_full_names', 'get_document', 'confirmado', 'links')
    list_filter = ('fecha', 'paciente__numero_documento')
    
    @admin.display(description='Acciones')
    def links(self, obj):
        return mark_safe(marcar_en_sala(obj))
    
    @admin.display(description='Paciente')
    def get_full_names(self, obj):
        return f"{obj.paciente.nombres} {obj.paciente.apellidos}"
    
    
    @admin.display(description='Número de documento')
    def get_document(self, obj):
        return obj.paciente.numero_documento
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(asistio=False)
        return queryset
    
    
@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_names', 'get_document', 'en_espera', 'llamar_o_cerrar')
    list_filter = ('cita__paciente__numero_documento',)
    
    @admin.display(description='Paciente')
    def get_full_names(self, obj):
        return f"{obj.cita.paciente.nombres} {obj.cita.paciente.apellidos}"
    
    
    @admin.display(description='Número de documento')
    def get_document(self, obj):
        return obj.cita.paciente.numero_documento

    @admin.display(description='Acciones')
    def llamar_o_cerrar(self, obj):
        return mark_safe(llamar_o_cerrar(obj))
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(en_espera=True)
        return queryset