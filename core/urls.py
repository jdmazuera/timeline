from django.urls import path,include
from core.views import LoginView,IndexView,LogoutView,Perfil,Actualizar,RegistroView

app_name = 'core'

urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('registro',RegistroView.as_view(),name='registro'),
    path('',IndexView.as_view(),name='index'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('perfil/<int:pk>',Perfil.as_view(),name='perfil'),
    path('actualizar/<int:pk>',Actualizar.as_view(),name='actualizar')
]
