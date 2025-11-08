from django.db import models
from django.urls import reverse
from django.conf import settings

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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ejercicios', null=True, blank=True)
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

    def get_absolute_url(self):
        return reverse('ejercicio_detalle', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='comentarios')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author} on {self.ejercicio}"
