from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Peliculas(models.Model):
    peliculas_a_Seleccion = (('comedias','Comedias'),('terror', 'Terror'),('accion','Accion'),
                             ('romanticas','Romanticas'),('suspenso','Suspenso')
                            ,('otras', 'Otras'),)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=15, choices=peliculas_a_Seleccion, default='Seleccione aqui el tipo')
    region = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    duracion = models.DecimalField(max_digits=10, decimal_places=2)
    anio_extreno = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenPeliculas = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-anio_extreno']

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    comentario = models.ForeignKey(Peliculas, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    