from django.shortcuts import render
from django.views.generic import View
from post.forms import PostForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from post.models import Post,Like,Comentario
from core.models import User
from post.serializers import PostSerializer
from rest_framework.generics import ListAPIView

class PostCreate(View):
    def get(self,request,*args,**kwargs):
        form = PostForm()
        return render(request,'post/post_form.html',{'form':form})

    def post(self,request,*args,**kwargs):
        post = PostForm(request.POST,request.FILES)
        if post.is_valid():
            post.instance.usuario = request.user
            post.save()

        return redirect('core:index')

class LikeView(View):
    def get(self,request,*args,**kwargs):
        user_pk = kwargs.get('user')
        post_pk = kwargs.get('post')
        try:
            like = Like.objects.get(usuario__id=user_pk,post__id=post_pk)
            like.delete()
        except:
            usuario = User.objects.get(pk=user_pk)
            post = Post.objects.get(pk=post_pk)
            like = Like()
            like.usuario = usuario
            like.post = post
            like.save()
        return redirect('core:index')

class ComentarView(View):
    def post(self,request,*args,**kwargs):
        usuario = kwargs.get('user')
        post = kwargs.get('post')
        comentario_padre = kwargs.get('comentario_padre')

        comentario = Comentario()

        print(kwargs)

        usuario = User.objects.get(pk=usuario)
        post = Post.objects.get(pk=post)

        comentario.usuario = usuario
        comentario.post = post
        comentario.mensaje = request.POST.get('mensaje')

        if comentario_padre:
            comentario_padre = Comentario.objects.get(pk=comentario_padre)
            comentario.comentario_padre = comentario_padre

        comentario.save()

        return redirect('core:index')

class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

        



