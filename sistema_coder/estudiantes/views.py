from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludar(request):
    return HttpResponse(f"Hola Soy Mauro Pisani y hoy es: {datetime.now()}")

def listar_estudiantes(request):
    contexto = {
        "estudiantes": ["Lervin", "Nazareno", "Mauro", "Eugenio"]
    }
    return render(
        request=request, 
        template_name="estudiantes/Lista_estudiantes.html",
        context=contexto
        )

def listar_profesores(request):
    return render(request=request, template_name="estudiantes/lista_profesores.html")    

# Create your views here.
