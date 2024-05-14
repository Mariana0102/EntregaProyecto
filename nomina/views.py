from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import status
from  rest_framework.response import Response
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail, EmailMessage
from .forms import  RegistroUsuario, CustomAuthenticationForm
from .extraccion import obtener_correos, obtener_usuarios

# Create your views here.

def registro(request):
    if request.method == 'GET':
        form = RegistroUsuario()
        return render(request, 'registro.html', {'form': form})
    elif request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nombre = form.cleaned_data['name']
            apellido = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            

            if password1 == password2:
                try:
                    usuario = User.objects.create_user(username=username, password=password1, 
                                                        first_name=nombre, last_name=apellido, email=email)
                    usuario.save()
                    login(request, usuario)
                    return redirect('home')
                except:
                    return render(request, 'registro.html', {'form': form, 'error': 'El nombre de usuario ya existe'})
            else:
                return render(request, 'registro.html', {'form': form, 'error': 'Las contraseñas no coinciden'})
        else:
            return render(request, 'home.html', {'form': form})
def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username =request.POST['username'], password= request.POST['password'])
        if user is None:
            return render(request, 'inicio_sesion.html',{
                    'form': AuthenticationForm,
                    'error':'username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')
def singout(request):
    logout(request)
    return redirect('inicio_sesion')       
def home(request):
    return render(request, 'home.html')
def create_tasks(request):

    if request.method == 'GET':
        form = RegistroUsuario()
        return render(request, 'create_tasks.html', {'form': form})
    elif request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nombre = form.cleaned_data['name']
            apellido = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            

            if password1 == password2:
                try:
                    usuario = User.objects.create_user(username=username, password=password1, 
                                                        first_name=nombre, last_name=apellido, email=email)
                    usuario.save()
                    login(request, usuario)
                    return redirect('create_tasks')
                except:
                    return render(request, 'create_tasks.html', {'form': form, 'error': 'El nombre de usuario ya existe'})
            else:
                return render(request, 'create_tasks.html', {'form': form, 'error': 'Las contraseñas no coinciden'})
        else:
            return render(request, 'create_tasks.html', {'form': form})
def litaEmpleados(request):
    empleados =User.objects.all()
    return render(request, 'lista_empleados.html', {
        'empleados':empleados
    })
def detalles_empleados(request, id):
    if request.method =='GET':
        empleado=get_object_or_404(User, pk=id)
        form= RegistroUsuario(instance=empleado)
        return render(request, 'detalle_empleado.html',{
            'empleado':empleado,
            'form':form
            })
    else:
        try:
            empleado=get_object_or_404(User, pk=id)
            form = RegistroUsuario(request.POST, instance=empleado)
            form.save()
            return redirect('lista_empleados')  
        except ValueError:
            return render(request, 'detalle_empleado.html',{
            'empleado':empleado,
            'form':form,
            'error':"Error updating user data"
            })
def despedir(request, id):
    empleado=get_object_or_404(User, pk=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
def contact(request):
    if request.method == "POST":
        try:
            email_api_view = EmailAPIView()
            email_api_view.post(request)
            messages.success(request, 'Correo Enviado')
        except Exception as e:
            messages.error(request, f'Error al enviar el correo: {str(e)}')
        return redirect('home')
    else:
        return render(request, 'index.html')    
class EmailAPIView(APIView):
    def post(self, request):
        try:
            correos = obtener_correos()
            nombrescompletos = obtener_usuarios()
            for persona in range(0,len(correos)):
                to_email= correos[persona]
                subject ="Pago de su Sueldo"
                message =f" Buenas noches {nombrescompletos[persona]}, has recibido el pago del dia de hoy por:--$5.000.000. Gracias por trabajar con nostros, esperamos de tu colaboracion para un futuro mejor para nuestra empreza."
                send_mail(subject, message, None,[to_email])
            return Response({'message':'correo, Enviado con Exito'}, status=status.HTTP_200_OK)
        except Exception as e:
            error_message =str(e)
            return Response({'message:',error_message}, status=status.HTTP_400_BAD_REQUEST)        