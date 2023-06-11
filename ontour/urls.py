from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('actualizar', views.actualizar, name='actualizar'),
    path('Asia', views.Asia, name='Asia'),
    path('carga', views.carga, name='carga'),
    path('Chile', views.Chile, name='Chile'),
    path('contacto', views.contacto, name='contacto'),
    path('crear', views.crear, name='crear'),
    path('destinos', views.destinos, name='destinos'),
    path('Europa', views.Europa, name='Europa'),
    path('indexEjecutivo', views.indexEjecutivo, name='indexEjecutivo'),
    path('inicioSesion', views.inicioSesion, name='inicioSesion'),
    path('reporte', views.reporte, name='reporte'),
    path('subir', views.subir, name='subir'),
    path('genera', views.genera, name='genera')
]
