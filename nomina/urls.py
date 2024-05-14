from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_sesion, name="inicio_sesion" ),
    path('registro/', views.registro, name="registro" ),
    path('logout/', views.singout, name='logout'),
    path('home/', views.home, name='home'),
    path('create_tasks/', views.create_tasks, name='create_tasks'),
    path('lista_empleados/', views.litaEmpleados, name='lista_empleados'),
    path('lista_empleados/<int:id>',views.detalles_empleados, name='detalle_empleado'),
    path('lista_empleados/<int:id>/despedir',views.despedir, name='despedir'),
    path('index/', views.contact, name='contact'),
    path('send-email', views.EmailAPIView.as_view(), name='send-email')
    

    
]
