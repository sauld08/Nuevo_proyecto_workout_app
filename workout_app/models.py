from django.db import models
from django.urls import reverse

class GrupoMuscular(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='grupos_musculares/', blank=True, null=True)
    imagen_url = models.URLField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Grupos Musculares"
        ordering = ['orden']
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('grupo_muscular_detalle', kwargs={'pk': self.pk})

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE, related_name='ejercicios')
    musculos_trabajados = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='ejercicios/', blank=True, null=True)
    imagen_url = models.URLField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['grupo_muscular', 'orden']
    
    def __str__(self):
        return f"{self.nombre} - {self.grupo_muscular.nombre}"
