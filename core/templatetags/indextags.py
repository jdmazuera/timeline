import datetime
from django import template
from post.models import Post,Comentario

register = template.Library()

@register.simple_tag
def likes_counter(post_id):
    post = Post.objects.get(pk=post_id)
    return post.like_set.all().count()

@register.filter('obtener_comentarios')
def obtener_comentarios(post_id):
    post = Post.objects.get(pk=post_id)
    return post.comentario_set.filter(comentario_padre__isnull=True)

@register.filter('obtener_respuestas')
def obtener_respuestas(comentario_id):
    comentario = Comentario.objects.get(pk=comentario_id)
    return Comentario.objects.filter(comentario_padre=comentario)