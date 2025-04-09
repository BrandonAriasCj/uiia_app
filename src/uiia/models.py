from django.db import models

class Componente(models.Model):
    nombre = models.CharField(max_length=100)
#    historial_chat = models.JSONField(default=list)
    descripcion = models.TextField(blank=True)
    prompt = models.TextField(blank=True)
    codigo_generado = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre