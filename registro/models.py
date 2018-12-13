from django.db import models

class Clientes(models.Model):
    nombrecli = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

    def __str__(selft):
        return self.nombrecli

class Cuentas(models.Model):
    nombre = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    againcontraseña = models.CharField(max_length=50)


    def __str__(selft):
        return self.nombre 
       
