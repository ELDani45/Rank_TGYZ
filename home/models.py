from django.db import models

# Create your models here.


class Puntos(models.Model):
    puntos_totales = models.IntegerField(default=0)

    def mostrar_puntos(self):
        return str(self.puntos_totales)

    def ganar_puntos(self,  cantidad: int) -> int:
        suna = self.puntos_totales + cantidad
        return suna


class Usuario(models.Model):
    name = models.TextField(max_length=100)


class Progreso(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nivel = models.IntegerField(default=1)
    Puntos = models.IntegerField(default=0)
