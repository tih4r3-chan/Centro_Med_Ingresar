from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'web'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registra/', views.index, name='index'),
    path('home/', views.Registro, name='formulario'),
    path('lista/', views.lista_usuarios, name='listaUsuarios'),
    path('login/', views.IniciarSesion, name='iniciar_sesion'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)