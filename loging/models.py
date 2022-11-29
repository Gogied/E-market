from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estado_producto(models.Model):
    estado_id = models.AutoField(primary_key= True, verbose_name='estado_id')
    descripcion = models.CharField(max_length= 20, verbose_name='descripcion')

    def __str__(self):
        return self.descripcion

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key= True, verbose_name='categoria_id')
    descripcion = models.CharField(max_length= 20, verbose_name='descripcion')

    def __str__(self):
        return self.descripcion
    
class Envio(models.Model):
    envio_id = models.AutoField(primary_key= True, verbose_name='envio_id')
    descripcion = models.CharField(max_length= 20, verbose_name='descripcion')

    def __str__(self):
        return self.descripcion



class Producto(models.Model):
    id = models.AutoField(primary_key= True, verbose_name='id')
    titulo = models.CharField(max_length=30, verbose_name='titulo')
    descripcion = models.TextField(max_length= 255, verbose_name='descripcion')
    precio = models.IntegerField(verbose_name='precio')
    contacto = models.CharField(max_length=12, verbose_name='contacto')
    created= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    estado_id = models.ForeignKey(Estado_producto, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    envio_id = models.ForeignKey(Envio, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.titulo

        


# diego perrotermita24
# admi administrador12