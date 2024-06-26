from django.db import models

# Create your models here.
class Link(models.Model):
    key=models.SlugField(max_length=100, unique=True,verbose_name='nombre clave')
    name=models.CharField(max_length=200, verbose_name='Red social')
    url=models.URLField(max_length=100, blank=True, null=True , verbose_name='Enlace')
    created=models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name='enlace'
        verbose_name_plural='enlaces'
        ordering=['-name']
        
    def __str__(self) :
        return self.name