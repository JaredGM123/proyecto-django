from django.shortcuts import render, redirect
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404


# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/principal.html",{"alumnos":alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():  # Si los datos recibidos son correctos
            form.save()  # Inserta
            return redirect('consultar_comentarios')
    else:
        form = ComentarioContactoForm()
    
    # Si algo sale mal se reenvían al formulario los datos ingresados
    return render(request, 'registros/contacto.html', {'form': form})

def contacto(request):
 return render(request,"registros/contacto.html")

def consultar_comentarios(request):
  comentarios = ComentarioContacto.objects.all()
  return render(request, 'registros/consultar_comentarios.html', {'comentarios': comentarios})


def editar_comentario(request, pk):
    comentario = get_object_or_404(ComentarioContacto, pk=pk)
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('consultar_comentarios')
    else:
        form = ComentarioContactoForm(instance=comentario)
    return render(request, 'registros/editar_comentario.html', {'form': form})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})
