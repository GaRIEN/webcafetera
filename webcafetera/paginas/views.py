from django.shortcuts import render,get_object_or_404
from .models import Paginas

# Create your views here.
def pagina(request, pagina_id):
    page=get_object_or_404(Paginas,id=pagina_id)
    return render(request,'paginas/ejemplo.html',{'page':page})