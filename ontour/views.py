from django.shortcuts import render
from .models import colegio, curso
from .models import Pagos
# Create your views here.

def genera(request):
    colegios = colegio.objects.all()
    context = {"colegios": colegios}
    
    if request.method == 'POST':
        colegio_id = request.POST.get('colegio')
        cursos = curso.objects.filter(id_colegio=colegio_id)
        context['cursos'] = cursos

        curso_id = request.POST.get('curso')  # Obtener el ID del curso seleccionado
        if curso_id:
            pagos = Pagos.objects.filter(id_curso=curso_id)
            context['pagos'] = pagos
    
    return render(request, 'ontour/genera.html', context)


def reporte(request):
    context={}
    return render(request, 'ontour/reporte.html', context)


def index(request):
    context={"index":index}
    return render(request, 'ontour/index.html', context)

def actualizar(request):
    context={}
    return render(request, 'ontour/actualizar.html', context)

def Asia(request):
    context={}
    return render(request, 'ontour/Asia.html', context)

def carga(request):
    context={}
    return render(request, 'ontour/carga.html', context)

def Chile(request):
    context={}
    return render(request, 'ontour/Chile.html', context)

def contacto(request):
    context={}
    return render(request, 'ontour/contacto.html', context)

def crear(request):
    context={}
    return render(request, 'ontour/crear.html', context)

def destinos(request):
    context={}
    return render(request, 'ontour/destinos.html', context)

def Europa(request):
    context={}
    return render(request, 'ontour/Europa.html', context)

def indexEjecutivo(request):
    context={}
    return render(request, 'ontour/indexEjecutivo.html', context)

def inicioSesion(request):
    context={}
    return render(request, 'ontour/inicioSesion.html', context)

def subir(request):
    context={}
    return render(request, 'ontour/subir.html', context)


