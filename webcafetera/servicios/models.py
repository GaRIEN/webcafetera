from django.db import models

# Create your models here.

class Service(models.Model):
    title=models.CharField(max_length=200, verbose_name='titulo')
    subtitle=models.CharField(max_length=200, verbose_name='subtitulo')
    content=models.CharField(verbose_name='contenido')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='servicio'
        verbose_name='servicios'
        
    def __str__(self):
        return self.title