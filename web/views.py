from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from rest_framework.utils import json
from .forms import UserForm, LoginForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def IniciarSesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # Autenticar al usuario
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('form.html') 
            else:
                form.add_error(None, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')
    else:
        # Si la solicitud no es POST, mostrar el formulario de inicio de sesión vacío
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# mostrar inicio
def inicio(request):
    return render(request,'inicio.html')
    
# registrar
def index(request):
    response = requests.get('http://127.0.0.1:8000/usuarios').json()
    return render(request, 'index.html', {
        'response': response
    })
    

# listar usuarios
def lista_usuarios(request):
    # Realiza una solicitud GET a la API de la aplicación 'ingreso'
    response = requests.get('http://127.0.0.1:8000/usuarios')
    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        usuarios = response.json()
        return render(request, 'listaU.html', {'usuarios': usuarios})
    else:
        # Maneja el caso en que la solicitud no fue exitosa
        return render(request, 'error.html', {'mensaje': 'Error al obtener la lista de usuarios'})
    

# registrar usuarios    
def Registro(request):
    url = "http://127.0.0.1:8000/usuarios/registra/"
    form = UserForm(request.POST or None)
    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        apellido = form.cleaned_data.get("apellido")
        email = form.cleaned_data.get("email")
        tipoUsuario = form.cleaned_data.get("tipoUsuario")
        password = form.cleaned_data.get("password")
        print(nombre)
        print(apellido)
        print(email)
        print(tipoUsuario)
        print(password)
        data = {'nombre': nombre, 'apellido': apellido, 'email': email, 'tipoUsuario': tipoUsuario, 'password': password}
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        # Autenticar y logear al usuario si el registro en el servidor externo fue exitoso
        if response.status_code == 200:  # Ajusta según la lógica específica de tu servidor
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            
        return render(request, 'form.html', {
            'response': response
        })

