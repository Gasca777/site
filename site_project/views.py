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


def index_tipo(request):
    tipos = Tipo.objects.all()
    return render(request, 'tipo/index.html', {
        'tipos': tipos
    })


def alta_tipo(request, id=None):
    form = TipoForm()
    mensaje = None
    delete = False

    if id:
        tipo = Tipo.objects.get(pk=id)
        form = TipoForm(instance=tipo)
        delete = True

    if request.method == 'POST':

        if id:
            form = TipoForm(request.POST, instance=tipo)
        else:
            form = TipoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('IndexTipo')
        else:
            mensaje = 'Formulario invalido'

    return render(request, 'tipo/insert_update.html', {
        'form': form,
        'mensaje': mensaje,
        'delete': delete,
    })


def eliminar_tipo(request, id):
    Tipo.objects.get(pk=id).delete()
    return redirect('IndexTipo')


def index_patch(request):
    patchs = Patch.objects.all()
    return render(request, 'patch/index.html', {
        'patchs': patchs,
    })


def alta_patch(request, id=None):
    form = PatchForm()
    mensaje = None
    delete = False

    if id:
        patch = Patch.objects.get(pk=id)
        form = PatchForm(instance=patch)
        delete = True

    if request.method == 'POST':

        if id:
            form = PatchForm(request.POST, instance=patch)
        else:
            form = PatchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('IndexPatch')
        else:
            mensaje = 'Formulario invalido'

    return render(request, 'patch/insert_update.html', {
        'form': form,
        'mensaje': mensaje,
        'delete': delete,
    })


def eliminar_patch(request, id):
    Patch.objects.get(pk=id).delete()
    return redirect('IndexPatch')


def index_switch(request):
    switchs = Switch.objects.all()
    return render(request, 'switch/index.html', {
        'switchs': switchs
    })


def alta_switch(request, id=None):
    form = SwitchForm()
    mensaje = None
    delete = False

    if id:
        switch = Switch.objects.get(pk=id)
        form = SwitchForm(instance=switch)
        delete = True

    if request.method == 'POST':

        if id:
            form = SwitchForm(request.POST, instance=switch)
        else:
            form = SwitchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('IndexSwitch')
        else:
            mensaje = 'Formulario invalido'

    return render(request, 'switch/insert_update.html', {
        'form': form,
        'mensaje': mensaje,
        'delete': delete,
    })


def eliminar_switch(request, id):
    Switch.objects.get(pk=id).delete()
    return redirect('IndexSwitch')


def index_puerto_switch(request):
    puertosSwitch = PuertoSwitch.objects.all()
    return render(request, 'puertoSwitch/index.html', {
        'puertosSwitch': puertosSwitch
    })


def alta_puerto_switch(request, id=None):
    form = PuertoSwitchForm()
    mensaje = None
    delete = False

    if id:
        puertoSwitch = PuertoSwitch.objects.get(pk=id)
        form = PuertoSwitchForm(instance=puertoSwitch)
        delete = True

    if request.method == 'POST':

        if id:
            form = PuertoSwitchForm(request.POST, instance=puertoSwitch)
        else:
            form = PuertoSwitchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('IndexPuertoSwitch')
        else:
            mensaje = 'Formulario invalido'

    return render(request, 'puertoSwitch/insert_update.html', {
        'form': form,
        'mensaje': mensaje,
        'delete': delete,
    })


def eliminar_puerto_switch(request, id):
    PuertoSwitch.objects.get(pk=id).delete()
    return redirect('IndexPuertoSwitch')
