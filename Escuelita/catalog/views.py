from django.shortcuts import render,HttpResponse, redirect
from catalog.models import Alumnos 
from catalog.models import Maestro 
from catalog.models import Carrera
from catalog.models import Horario


# Create your views here.



def index(request):

 return render(request, 'index.html')

def inicio_sesion(request):

    return render(request, 'Login.html')

def register(request):
    return render(request,'Register.html')

def crearUsuario(request):
    constrasena = ""

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
        Html = 'AlumnosPage.html'
        NombreUsuario = {
            'Nombre' : request.GET["nombre"],
            'ApellidoP' : request.GET["apellidoP"],
            'ApellidoM' : request.GET["apellidoM"]
        }
    else : Html = 'MaestrosPage.html', Maestros.save(),         
    NombreUsuario = {
            'Nombre' : request.GET["nombre"],
            'ApellidoP' : request.GET["apellidoP"],
            'ApellidoM' : request.GET["apellidoM"],
        }
        
    return render(request, Html, NombreUsuario ) 

def mostrarMaterias(request):
    CarreraS = request.GET["CarreraS"]
    if(CarreraS == "Derecho"):
        id = 1
    elif(CarreraS == "Software"):
        id = 2
    else : id = 3
    CarreraCH = Carrera.objects.get(pk = id)
    Materias = [CarreraCH.Materia1,CarreraCH.Materia2,CarreraCH.Materia3,CarreraCH.Materia4,CarreraCH.Materia5]
    context = {

        'M1' : Materias[0],
        'M2' : Materias[1],
        'M3' : Materias[2],
        'M4' : Materias[3],
        'M5' : Materias[4]
    }
    
    return render(request, 'EscogerMateria.html', context)

def CrearHorarios(request):
    HorarioU = Horario(
    Nombre = "Eder",
    ApellidoP = "Castro",
    ApellidoM = "Elizalde",
    Nombre_Carrera = "Derecho",
    Materia1H = "Penal",
    Materia2H = "Civil",
    Materia3H = "Mercantil",
    Materia4H = "Civil",
    Materia5H = "Familiar"
    )
    HorarioU.save()


    return render(request, 'MostrarHorario.html')