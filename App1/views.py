from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
#para hacer consulta a las bases de datos
from .models import ProyectoDb,TareaDb
# Create your views here.
def IndexReview(request):
    """ respuesta http"""
    #return HttpResponse("Hola mundo estamos bien ")
    objeto = ProyectoDb.objects.all().order_by('-id')
    return render(request,'index.html',{"objeto":objeto})#pasamos la consulta al html

def ProyectoView(request,id):
    proyecto = get_object_or_404(ProyectoDb,id=id)
    return render(request,'proyectos.html',{"objeto":proyecto})

