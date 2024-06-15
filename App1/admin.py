from django.contrib import admin
# importamos los modelos
from .models import ProyectoDb, TareaDb,UsuarioDb

# Register your models here.

admin.site.site_header="Administración de Proyectos"
admin.site.index_title="Proyectos y tareas"
admin.site.site_title ="Tareas"
class TareasUsuario(admin.TabularInline):
    model = UsuarioDb
    extra = 1

class ProyectoTareas(admin.TabularInline):
    model = TareaDb
    extra = 1

class ProyectoAdmin(admin.ModelAdmin):
    # agregamos los campos
    fields = ['nombreP','descripcionP','fechaI','fechaF','responsable','estado']
    list_display = ['nombreP','descripcionP','fechaI','fechaF','responsable','estado']
    list_filter = ['fechaI','estado']
    search_fields = ['nombreP']
    search_help_text = 'Busqueda por Nombre'
    ordering = ['fechaI']
    inlines = [ProyectoTareas]

    # realizar operaciones propias
    def actualizar_o(self, request, queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                nombre1 = obj.nombre
                obj.nombre = nombre1.replace("O", "o")
                obj.save()
        self.message_user(request, "Exitosamente")
    actualizar_o.short_description = "Actualizar letras O"
    actions = ["actualizar_o"]#llamada a la funcion actualizar_o

admin.site.register(ProyectoDb, ProyectoAdmin)

@admin.register(TareaDb)
class TareaAdmin(admin.ModelAdmin):
    fields = ['nombreT', 'fecha_inicio',
              'fecha_fin', 'asignado', 'proyecto_fk','done']
    list_display = ['nombreT', 'fecha_inicio',
                    'fecha_fin', 'asignado', 'proyecto_fk','done']
    list_filter = ['proyecto_fk']
    search_fields = ['nombreT']
    search_help_text = 'Busqueda por Nombre'
    ordering = ['proyecto_fk']

    
@admin.register(UsuarioDb)   
class UsuarioAdmin(admin.ModelAdmin):
    fields = ['nombreU','email','telefono']
    list_display = ['nombreU']
    list_filter = ['email']
    