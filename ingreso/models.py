from django.db import models

# Create your models here.
class Users(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tipoUsuario = models.CharField(max_length=60)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.nombre
    