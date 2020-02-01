from django.db import models
from django.contrib.auth.models import AbstractUser,Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now
from django.conf import settings

class Post(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='Propietario',null=True,blank=True)
    descripcion = models.TextField(verbose_name='Descripcion',blank=False)
    imagen = models.ImageField(upload_to = 'imagenes/',default='',verbose_name='Imagen',blank=False)
    privado = models.BooleanField(verbose_name='Privado',default=False)

class Like(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='Propietario',null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name='Post',null=True,blank=True)

class Comentario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='Propietario',null=True,blank=True)
    comentario_padre = models.ForeignKey('post.comentario',on_delete=models.CASCADE,verbose_name='Respuesta',null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name='Post',null=True,blank=True)
    mensaje = models.TextField(verbose_name='Comentario',default='')