
from django.urls import path
from . import views


urlpatterns = [
    path('pagina/<int:pagina_id>/', views.pagina, name='paginas'),
    # Otras URLs aquí...
]


