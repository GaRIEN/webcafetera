from .models import Link
#creamos para que puedan extender todas las paginas
def ctx_dict(request):
    ctx={}
    links=Link.objects.all()
    for link in links:
        ctx[link.key]=link.url
    return ctx