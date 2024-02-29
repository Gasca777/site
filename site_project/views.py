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
    delete = False

    if id:
        empresa = Empresa.objects.get(pk=id)
        form = EmpresaForm(instance=empresa)
        delete = True

    if request.method == 'POST':

        if id:
            form = EmpresaForm(request.POST, instance=empresa)
        else:
            form = EmpresaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('IndexEmpresa')
        else:
            mensaje = 'Formulario invalido'

    return render(request, 'empresa/insert_update.html', {
        'mensaje': mensaje,
        'form': form,
        'delete': delete,
    })


def eliminar_empresa(request, id):
    Empresa.objects.get(pk=id).delete()
    return redirect('IndexEmpresa')


def index_area(request):
    areas = Area.objects.all()
    return render(request, 'area/index.html', {
        'areas': areas
    })


def alta_area(request, id=None):
    form = AreaForm()
    mensaje = None
    delete = False

    if id:
        area = Area.objects.get(pk=id)
        form = AreaForm(instance=area)
        delete = True

    if request.method == 'POST':

        if id:
            form = AreaForm(request.POST, instance=area)
        else:
            form = AreaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('IndexArea')
        else:
            mensaje = 'Formulario invalido'

    return render(request, 'area/insert_update.html', {
        'form': form,
        'mensaje': mensaje,
        'delete': delete,
    })


def eliminar_area(request, id):
    Area.objects.get(pk=id).delete()
    return redirect('IndexArea')
