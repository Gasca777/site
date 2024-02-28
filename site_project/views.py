from django.shortcuts import render, redirect
from .forms import *


# Creación de vistas
def home(request):
    return render(request, "index.html")


def index_empresa(request):
    empresas = Empresa.objects.all()

    return render(request, 'empresa/index.html', {
        'empresas': empresas
    })


def alta_empresa(request, id=None):
    mensaje = None
    form = EmpresaForm()

    if id:
        empresa = Empresa.objects.get(pk=id)

    if request.method == 'POST':
        form = EmpresaForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('IndexEmpresa')
        else:
            mensaje = 'Formulario invalido'

    return render(request, 'empresa/insert_update.html', {
        'mensaje': mensaje,
        'form': form
    })
