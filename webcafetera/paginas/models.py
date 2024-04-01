from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

class Paginas(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo')
    content = RichTextUploadingField(verbose_name='contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['-title']
        
    def __str__(self):
        return self.title
