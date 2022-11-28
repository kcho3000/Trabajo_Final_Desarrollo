from django.shortcuts import render,HttpResponse, redirect
from catalog.models import Alumnos 
from catalog.models import Maestro 


# Create your views here.



def index(request):

 return render(request, 'index.html')

def inicio_sesion(request):

    return render(request, 'Login.html')

def register(request):
    return render(request,'Register.html')

def crearUsuario(request):

    if(request.GET["contraseña"] == request.GET["contraseñar"]):
        constrasena = request.GET["contraseña"]
    Alumno = Alumnos(
    Nombre = request.GET["nombre"],
    ApellidoP = request.GET["apellidoP"],
    ApellidoM = request.GET["apellidoM"],
    Correo = request.GET["correo"],
    Contraseña = constrasena
    )
    Maestros = Maestro(
    Nombre = request.GET["nombre"],
    ApellidoP = request.GET["apellidoP"],
    ApellidoM = request.GET["apellidoM"],
    Correo = request.GET["correo"],
    Contraseña = constrasena
    )
    if(request.GET["MoA"] == "Alumno"):
        Alumno.save()
    else : Maestros.save()

    return HttpResponse("Se creo Usuario" , constrasena)