from django.shortcuts import render, redirect
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages


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

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})

def consultarComentarioIndividual(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request, "registros/formEditarComentario.html", {'comentario': comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    return render(request, "registros/formEditarComentario.html", {'comentario': comentario})

def consultar1(request):
 alumnos=Alumnos.objects.filter(carrera="TI")
 return render(request,"registros/consultas.html", {'alumnos':alumnos})

def consultar2(request):
 alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
 return render(request,"registros/consultas.html", {'alumnos':alumnos})

def consultar3(request):
 alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
 return render(request,"registros/consultas.html", {'alumnos':alumnos})

def consultar4(request):
 alumnos=Alumnos.objects.filter(turno__contains="Vesp")
 return render(request,"registros/consultas.html", {'alumnos':alumnos})


def consultar4(request):
 alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
 return render(request,"registros/consultas.html", {'alumnos':alumnos})

def consultar6(request):
   fechaInicio= datetime.date(2025,6,20)
   fechaFin = datetime.date(2025,7,9)
   alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
   return render(request,"registros/consultas.html", {"alumnos":alumnos})

def consultar7(request):
 alumnos=Alumnos.objects.filter(comentario__coment__contains="No inscrito")
 return render(request,"registros/consultas.html", {'alumnos':alumnos})

def consultar8(request):
    fecha_inicio = datetime.date(2025, 7, 8)
    fecha_fin = datetime.date(2025, 7, 9)
    comentarios = ComentarioContacto.objects.filter(created__range=(fecha_inicio, fecha_fin))
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def consultar9(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__contains="hola")
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def consultar10(request):
    comentarios = ComentarioContacto.objects.filter(usuario__exact="Juan")
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def consultar11(request):
    lista_mensajes = ComentarioContacto.objects.values_list('mensaje', flat=True)
    for mensaje in lista_mensajes:
        print(mensaje)
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def consultar12(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__startswith="Ho")
    return render(request, "registros/consultas.html", {'comentarios': comentarios})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Archivo guardado exitosamente.")
            return redirect('Subir')  
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        form = FormArchivos()

    archivos = Archivos.objects.all()
    return render(request, "registros/archivos.html", {
        'form': form,
        'archivos': archivos
    })

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html", {'nombre':nombre})