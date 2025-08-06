"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from inicio import views as views_inicio
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name="Principal"),
    path('contacto/', views_registros.contacto, name="Contacto"),
    path('formulario/', views_inicio.formulario, name="Formulario"),
    path('ejemplo/', views_inicio.ejemplo, name="Ejemplo"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('consultar_comentarios/', views_registros.consultar_comentarios, name='consultar_comentarios'),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('formEditarComentario/<int:id>/', views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='Editar'),
    path('consultar1/', views_registros.consultar1, name="Consultas"),
    path('consultar2/', views_registros.consultar2, name="Consultas"),
    path('consultar3/', views_registros.consultar3, name="Consultas"),
    path('consultar4/', views_registros.consultar4, name="Consultas"),
    path('consultar6/', views_registros.consultar6, name="Consultas"),
    path('consultar7/', views_registros.consultar7, name="Consultas"),
    path('consultar8/', views_registros.consultar8, name="Consultas8"),
    path('consultar9/', views_registros.consultar9, name="Consultas9"),
    path('consultar10/', views_registros.consultar10, name="Consultas10"),
    path('consultar11/', views_registros.consultar11, name="Consultas11"),
    path('consultar12/', views_registros.consultar12, name="Consultas12"),
    path('subir',views_registros.archivos,name="Subir"),
    path('seguridad', views_registros.seguridad, name="Seguridad"),
]




if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)