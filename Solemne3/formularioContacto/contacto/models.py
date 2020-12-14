from django.db import models

# Create your models here.

class Contacto(models.Model):
    titulo = models.CharField("Titulo", max_length=100)
    nombre = models.CharField("Nombre", max_length=100)
    email = models.CharField("Email", max_length=50)
    numeroTelefono = models.CharField("Numero de Contacto", max_length=10)
    mensaje = models.TextField("Motivo de Contacto")
    estado = models.CharField("Estado", max_length=20)

    def __str__(self):
        return '#'+str(self.id)+' '+self.titulo + ' ('+ self.email+')'



class Plan(models.Model):
    nombre = models.CharField(max_length=50)
    minutos = models.CharField(max_length=50)
    internet = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


    def generarDescuento(self):
        if (self.precio <= 15990):
            return 0.05
        if (self.precio <= 22990):
            return 0.1
        if (self.precio <= 29990):
            return 0.2
        if (self.precio <= 35990):
            return 0.4
        
        return 0.5

    def calcularPrecioFinal(self):
        return self.precio * (1.0 - self.generarDescuento())