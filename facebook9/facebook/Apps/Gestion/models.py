from django.db import models

# Create your models here.

class Usuario(models.Model):
    Apellidos = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    Telefono = models.CharField(max_length=12)
    Fecha_Nacimiento = models.DateField()
    SEXOS = (('F','Femenino'),('M', 'Masculino'))
    genero = models.CharField(max_length=1,choices=SEXOS,default='M')

    def Nombre_Completo(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.Apellidos, self.Nombres,self.Telefono)

    def __str__(self):
        return self.Nombre_Completo()

class Publicaciones(models.Model):
    Usuario = models.ForeignKey(Usuario,null=False, blank=False, on_delete=models.CASCADE) 
    Titulo = models.CharField(max_length=35)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='albums/images/')

    def Mostrar_Publicacion(self):
        cadena = "{0} {1}, {2}" 
        return cadena.format(self.Titulo, self.descripcion, self.imagen)

    def __str__(self):
        return self.Mostrar_Publicacion()

