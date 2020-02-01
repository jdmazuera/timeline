from django.db import models
from django.contrib.auth.models import AbstractUser,Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now

class User(AbstractUser):

    mobile = models.CharField(max_length=40,blank=True,null=True,verbose_name='Celular')
    imagen_perfil = models.ImageField(upload_to = 'imagenes/',default='',verbose_name='Foto de Perfil',blank=False)
    descripcion = models.TextField(verbose_name='Descripción',default='',blank=False)
    fecha_nacimiento = models.DateField(verbose_name='Fecha Nacimiento',default=now)

    def __str__(self):
        return self.email

    @property
    def get_absolute_detail_url(self):
        from django.urls import reverse_lazy
        return reverse_lazy('core:detail', args=[str(self.id)])

    @property
    def get_absolute_edit_url(self):
        from django.urls import reverse_lazy
        return reverse_lazy('core:update', args=[str(self.id)])

    @property
    def get_absolute_delete_url(self):
        from django.urls import reverse_lazy
        return reverse_lazy('core:delete', args=[str(self.id)])

    def __str__(self):
        return self.get_full_name()

User._meta.get_field('username').verbose_name = 'Nombre De Usuario'
User._meta.get_field('username').help_text = 'Sin espacios ni caracteres especiales'
User._meta.get_field('username').error_messages = {
    'blank' : 'El Campo No Puede Estar En Blanco',
    'invalid' : 'El Valor No Es Valido',
    'invalid_choice' : 'Opcion No Valida',
    'unique' : 'El Usuario Debe Ser Unico'
}

User._meta.get_field('email').verbose_name = 'Correo Electronico'
User._meta.get_field('first_name').verbose_name = 'Nombre'
User._meta.get_field('first_name').blank = False
User._meta.get_field('last_name').verbose_name = 'Apellido'
User._meta.get_field('last_name').blank = False
User._meta.get_field('is_active').verbose_name = 'Activo'
User._meta.get_field('is_active').help_text = 'Desactiva el acceso al usuario a las caracteristicas del sistema'