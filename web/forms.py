from django import forms

class UserForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    tipoUsuario = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    
    

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)