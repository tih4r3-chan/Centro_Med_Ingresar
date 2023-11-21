from django.urls import path,include
from . import views
from .views import UserRegisterView, UserLoginView

urlpatterns =[
    path('',views.UsuariosLista, name='usuarios'),
    path('registra/', views.CrearUsuarios, name='registra'),
    path('eliminar/<str:pk>/', views.EliminarUsuarios, name='eliminar'),
    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('web/', include('web.urls'))
]