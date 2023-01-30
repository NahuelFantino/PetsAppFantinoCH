from django.shortcuts import render, redirect
from . models import Servicio, Mascota, Persona

# Create your views here.
def inicio(request):
    servicios = Servicio.objects.all()
    mascotas = Mascota.objects.all()
    persona = Persona.objects.all()
    return render(request, 'inicio.html', {'servicios' : servicios, 'mascotas' : mascotas, 'personas' : persona})

#----------------------------------SERVICIOS----------------------------------------
def servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios' : servicios})

def regServicio(request):
    servicio = request.POST['txtServicio']
    precio = request.POST['txtPrecio']
    ciudad = request.POST['txtCiudad']
    Servicio.objects.create(servicio= servicio, precio= precio, ciudad= ciudad)
    return redirect('/servicios')

def editarServicio(request, servicio):
    servicio = Mascota.objects.get(servicio = servicio)
    return render(request, '/editarServicio', {'servicio' : servicio})

def eliminarServicio(request, servicio):
    servicio = Servicio.objects.get(servicio = servicio)
    servicio.delete()
    return redirect('/servicios')

#----------------------------------PERSONAS--------------------------------------------
def persona(request):
    persona = Persona.objects.all()
    return render(request, 'personas.html', {'personas' : persona})

def regPersona(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    direccion = request.POST['txtDireccion']
    Persona.objects.create(nombre= nombre, apellido= apellido, direccion= direccion)
    return redirect('/personas')

def editarPersona(request, nombre):
    persona = Mascota.objects.get(nombre = nombre)
    return render(request, '/editarPersona', {'nombre' : nombre})

def eliminarPersona(request, nombre):
    persona = Persona.objects.get(nombre = nombre)
    persona.delete()
    return redirect('/personas')

#----------------------------------MASCOTAS---------------------------------------------
def mascota(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas.html', {'mascotas' : mascotas})

def regMascota(request):
    especie = request.POST['txtEspecie']
    nombre = request.POST['txtNombre']
    datos = request.POST['txtDatos']
    Mascota.objects.create(especie= especie, nombre= nombre, datos= datos)
    return redirect('/mascotas')

def editarMascota(request, codigo):
    mascota = Mascota.objects.get(nombre = codigo)
    return render(request, '/editarMascota', {'mascota' : mascota})

def editandoMascota(request):
    especie = request.POST['txtEspecie']
    nombre = request.POST['txtNombre']
    datos = request.POST['txtDatos']

    mascota = Mascota.objects.get(nombre = nombre)
    mascota.nombre = nombre
    mascota.datos = datos
    mascota.especie = especie
    mascota.save()
    return redirect('/mascotas')


def eliminarMascota(request, nombre):
    mascota = Mascota.objects.get(nombre = nombre)
    mascota.delete()
    return redirect('/mascotas')

#----------------------------------BUSCAR---------------------------------------------
