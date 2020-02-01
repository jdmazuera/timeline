from django.shortcuts import render
from django.views.generic import View, DetailView, UpdateView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from core.forms import RegistroForm, UserFrom
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required,permission_required
from core.models import User
from django.urls import reverse_lazy

class LoginView(View):
    template_name = 'core/login.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        if request.GET:
            next = request.GET.get('next')
        else:
            next = None
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            if next:
                return HttpResponseRedirect(next)
            return redirect('core:index')

        return render(
            request,
            self.template_name,
            {
                'next': request.GET.get('next'),
                'mostrar_error_login' : True
            }
        )


class RegistroView(View):
    template_name = 'core/registro.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('')
        return render(request,self.template_name,{
            'form' : RegistroForm()
        })
    def post(self, request, *args, **kwargs):
        usuario = RegistroForm(request.POST)
        
        if usuario.is_valid():
            usuario.save()
            return redirect('core:login')
        else:
            return render(request,self.template_name,{
                'form' : usuario
            })

@method_decorator(login_required, name='dispatch')
class IndexView(View):
    template_name = 'core/index.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        return render(request,self.template_name)

@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('core:login')

@method_decorator(login_required, name='dispatch')
class Perfil(DetailView):
    model = User

@method_decorator(login_required, name='dispatch')
class Actualizar(UpdateView):
    model = User
    success_url = reverse_lazy('core:index')
    form_class = UserFrom
