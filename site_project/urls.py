from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('empresa/', views.index_empresa, name='IndexEmpresa'),
    path('empresa/insert_update', views.alta_empresa, name='AltaEmpresa'),
    path('empresa/insert_update/<int:id>',
         views.alta_empresa, name='EditarEmpresa'),
    path('empresa/delete/<int:id>', views.eliminar_empresa, name='EliminarEmpresa'),
    path('area/', views.index_area, name='IndexArea'),
    path('area/insert_update', views.alta_area, name='AltaArea'),
    path('area/insert_update/<int:id>', views.alta_area, name='EditarArea'),
    path('area/delete/<int:id>', views.eliminar_area, name='EliminarArea'),
    path('tipo', views.index_tipo, name='IndexTipo'),
    path('tipo/insert_update', views.alta_tipo, name='AltaTipo'),
    path('tipo/insert_update/<int:id>', views.alta_tipo, name='EditarTipo'),
    path('tipo/delete/<int:id>', views.eliminar_tipo, name='EliminarTipo'),
    path('patch', views.index_patch, name='IndexPatch'),
    path('patch/insert_update', views.alta_patch, name='AltaPatch'),
    path('patch/insert_update/<int:id>', views.alta_patch, name='EditarPatch'),
    path('patch/delete/<int:id>', views.eliminar_patch, name='EliminarPatch'),
    path('switch', views.index_switch, name='IndexSwitch'),
    path('switch/insert_update', views.alta_switch, name='AltaSwitch'),
    path('switch/insert_update/<int:id>',
         views.alta_switch, name='EditarSwitch'),
    path('switch/delete/<int:id>', views.eliminar_switch, name='EliminarSwitch'),
]
