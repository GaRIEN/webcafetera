from django.apps import AppConfig


class ServiciosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'servicios'
    #cambiar nombre en el admin
    verbose_name='gestor de servicios'
