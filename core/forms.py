from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from core.models import User

class UserFrom(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserFrom, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs.update({'class':'col-md-4'})
        #self.fields['email'].widget.attrs.update({'class':'col-md-4'})
        #self.fields['password'].widget.attrs.update({'class':'col-md-4'})
        self.helper = FormHelper()
        self.helper.form_action = '#'
        self.helper.layout = Layout(
            Fieldset(
                'Informacion Personal',
                Row(
                    Div(
                        Field('username'),
                        css_class='col-md-3'
                    ),
                    Div(
                        Field('first_name'),
                        css_class='col-md-3'
                    ),
                    Div(
                        Field('last_name'),
                        css_class='col-md-3'
                    ),
                    Div(
                        Field('password'),
                        css_class='col-md-3'
                    )
                ),
                Row(
                    Div(
                        Field('mobile'),
                        css_class='col-md-3'
                    ),
                    Div(
                        Field('is_active'),
                        css_class='col-md-3'
                    ),
                    Div(
                        Field('email'),
                        css_class='col-md-3'
                    ),
                    Div(
                        Field('imagen_perfil'),
                        css_class='col-md-3'
                    )
                ),
                Row(
                    Div(
                        Field('fecha_nacimiento'),
                        css_class='col-md-3'
                    ),
                    Div(
                        Field('descripcion'),
                        css_class='col-md-9'
                    )
                )               
            ),
            ButtonHolder(
                Submit('submit', 'Guardar', css_class='button white'),
                HTML('<a class="btn btn-secondary" href={% url \'core:index\' %}>Cancelar</a></button>')
            )
        )
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput)

    def save(self, *args, **kwargs):
        self.instance.set_password(self.instance.password)
        return super(UserFrom, self).save(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','mobile','is_active','imagen_perfil','descripcion','fecha_nacimiento']

class RegistroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                None,
                Field('username'),
                Field('first_name'),
                Field('last_name'),
                Field('email'),
                Field('password'),
                Field('fecha_nacimiento')
            ),
            ButtonHolder(
                Submit('submit', 'Guardar', css_class='button white'),
                HTML('<a class="btn btn-secondary" href={% url \'core:login\' %}>Cancelar</a></button>')
            )
        )

        self.fields['password'] = forms.CharField(widget=forms.PasswordInput)
    
    def save(self, *args, **kwargs):
        self.instance.set_password(self.instance.password)
        return super(RegistroForm, self).save(*args, **kwargs)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','mobile','fecha_nacimiento']