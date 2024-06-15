from django.shortcuts import get_object_or_404, render,redirect
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
    return render(request,'tareas.html',{"objeto":proyecto})

def actualizar_item(request, item_id):
    item = get_object_or_404(TareaDb, id=item_id)
    if request.method == 'POST':
        # Actualizamos el dato, por ejemplo incrementando la cantidad
        item.done = True
        item.save()
        return redirect(IndexReview)
    return HttpResponse(status=405)