from django.contrib import admin
from .models import Paginas


# Register your models here.

class PaginaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
    
admin.site.register(Paginas,PaginaAdmin)