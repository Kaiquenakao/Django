from django.forms import ModelForm
from .models import Formulario

class CustomerForm(ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'sobrenome']
