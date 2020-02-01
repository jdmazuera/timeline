from django.urls import path,include
from post.views import PostCreate,LikeView,ComentarView,PostAPIView

app_name = 'post'

urlpatterns = [
    path('crear',PostCreate.as_view(),name='crear'),
    path('like/<int:user>/<int:post>',LikeView.as_view(),name='like'),
    path('comentar/<int:user>/<int:post>',ComentarView.as_view(),name='comentar'),
    path('comentar/<int:user>/<int:post>/<int:comentario_padre>',ComentarView.as_view(),name='comentar'),
    path('api_rest',PostAPIView.as_view(),name='api_rest')
]
