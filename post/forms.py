from post.models import Post,Comentario
from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                None,
                Field('imagen'),
                Field('descripcion'),
                Field('privado')
            ),
            ButtonHolder(
                Submit('submit', 'Guardar', css_class='button white'),
                HTML('<a class="btn btn-secondary" href={% url \'core:index\' %}>Cancelar</a></button>')
            )
        )

    def save(self, *args, **kwargs):
        return super(PostForm, self).save(*args, **kwargs)
    
    class Meta:
        model = Post
        fields = ['imagen','descripcion','privado']


class ComentarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                None,
                Field('mensaje')
            ),
            ButtonHolder(
                Submit('submit', 'Guardar', css_class='button white'),
                HTML('<a class="btn btn-secondary" href={% url \'core:index\' %}>Cancelar</a></button>')
            )
        )

    def save(self, *args, **kwargs):
        return super(ComentarioForm, self).save(*args, **kwargs)
    
    class Meta:
        model = Comentario
        fields = ['mensaje']