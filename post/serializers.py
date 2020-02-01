from rest_framework import serializers
from django.contrib.sites.models import Site
from post.models import Post

class PostSerializer(serializers.ModelSerializer):

    usuario = serializers.SerializerMethodField()
    descripcion = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()
    privado = serializers.SerializerMethodField()

    def get_usuario(self,obj):
        return obj.usuario.first_name

    def get_descripcion(self,obj):
        return obj.descripcion
    
    def get_imagen(self,obj):
        return obj.imagen.url
    
    def get_privado(self,obj):
        return obj.privado

    class Meta:
        model = Post
        fields = ('usuario', 'descripcion', 'imagen', 'privado')