from django.contrib import admin
from .models import GrupoMuscular, Ejercicio

@admin.register(GrupoMuscular)
class GrupoMuscularAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden']
    list_editable = ['orden']
    prepopulated_fields = {'descripcion': ['nombre']}

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'grupo_muscular', 'orden']
    list_filter = ['grupo_muscular']
    list_editable = ['orden']
    search_fields = ['nombre', 'descripcion']   
