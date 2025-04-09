from django.shortcuts import render
from uiia.templates import uiia
from django.shortcuts import redirect
import uiia.agente as ia
from uiia.models import Componente as Com
import asyncio

def vista_principal(request):
    objetos = Com.objects.all()
    return render(request, "uiia/main.html", {
        'rango': range(10),
        'objetos': reversed(objetos)    
    })

def vista_crear(request):
    if request.method == "POST":
        nom = request.POST.get('nombre')
        print(f"Nombre del proyecto es: {nom}")
        objeto = Com.objects.create(nombre=nom)
        print(objeto)

        return redirect('listado')

    return render(request, "uiia/crear.html")

def vista_generar(request, id):

    objeto = Com.objects.get(id=id)
    if request.method == 'POST':
        instanceIA = ia.ChatManager()
        prompt = request.POST.get('prompt')
        print("PROMPT:", prompt)

        instanceIA.añadir_ultima_version(objeto.codigo_generado)
        new_code = asyncio.run(instanceIA.preguntar_a_openai(prompt)) 
        objeto.codigo_generado = new_code
        objeto.save()
        del instanceIA


    return render(request, "uiia/generar.html", {
        'objeto': objeto,
    })

def vista_regenerar(request):
    return render(request, "uiia/regenerar.html")

def vista_eliminar(request, id):
    componente = Com.objects.get(id=id)
    componente.delete()
    print("Se elimino un elemento")
    return redirect('listado')


def vista_landing(request):
    return render(request, "uiia/landing.html")



###########################3
def generar_componente(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        return redirect('home')
        # aquí haces lo que necesites con ese prompt (guardar, enviar a IA, etc.)
        ...
    #return render(request, 'generar.html')
