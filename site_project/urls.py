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
]
