from django import forms
from .models import *


# Creación de formularios
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
