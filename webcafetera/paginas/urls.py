
from django.urls import path
from . import views


urlpatterns = [
  path('<int:pagina_id>/',views.pagina, name='paginas')

]

