from django import forms
from .models import *


# Creación de formularios
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'


class PatchForm(forms.ModelForm):
    class Meta:
        model = Patch
        fields = "__all__"
