from django import forms
from .models import Formulario, Profile

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'sobrenome']


class ProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ['name', 'email', 'bio']

