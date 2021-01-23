
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def plantilla(request):
    #Abrimos el documento que contiene a la plantilla
    plantilla_Externa = open("C:/Users/Dell/Desktop/facebook9/facebook/plantilla/plantilla1.html")
    template = Template(plantilla_Externa.read())
    plantilla_Externa.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)