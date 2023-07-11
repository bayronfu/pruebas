from django.shortcuts import render
from .models import colegio, curso, Pagos, estado_pago, contrato, paquete_turistico, Apoderado, Pagos

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
            curso_seleccionado = curso.objects.get(id_curso=curso_id)  # Obtener el curso seleccionado
            pagos = Pagos.objects.filter(id_curso=curso_seleccionado)  # Filtrar los pagos por el curso seleccionado
            # Obtener los objetos estado_pago relacionados con los pago del curso seleccionado
            estado_pagos = estado_pago.objects.filter(id_pago__in=pagos.values('id_pago'))
            
            context['pagos'] = pagos
            context['curso_seleccionado'] = curso_seleccionado
            context['estado_pagos'] = estado_pagos
        
    
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

def reporte_dos(request):
    contratos = contrato.objects.all()
    context={"contratos":contratos}
    
    return render(request, 'ontour/reporte_dos.html', context)

def reporte_generado(request,pk):
    if pk != "":
        contratos = contrato.objects.get(id_contrato=pk)
        paquetes = paquete_turistico.objects.all()
        cuentas   = estado_pago.objects.all()
        apoderados  = Apoderado.objects.all()
        cursos      = curso.objects.all()
        
                
        context={"contratos":contratos, 'paquetes':paquetes, 'cuentas':cuentas, 'apoderados':apoderados, 'cursos':cursos}

        if contratos:
            pagos = Pagos.objects.filter(id_cuenta_viaje=estado_pago.id_cuenta_viaje)
            context={'pagos':pagos}
            return render(request, 'ontour/reporte_generado.html', context)
        else:
            context={'mensaje': "Error, Atencion no existe."}
            return render(request,'ontour/reporte_dos.html', context )

