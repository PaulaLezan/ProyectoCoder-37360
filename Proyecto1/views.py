import datetime
from django.http import HttpResponse   #importamos http response
from django.template import Context,Template, loader 




def saludar(request): #recib un pedido
    return HttpResponse ("Hola mundo") #respondo algo

def segunda_vista (request):
    return HttpResponse ("Ya entesndi, esto es muy simple")

def dia_de_Hoy( request):
    dia=datetime.datetime.today()
    codigohtml="<h1> Hoy es: "+str(dia)+" <h1>"
    return HttpResponse (codigohtml)

def saludo_con_nombre (self, nombre):
    return("<h1> Hola mi nombre es : "+nombre+" </h1>")

def calculaAñoNacimiento(self, edad):
    return HttpResponse("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")

def probandoHtml (self):
    
    nom="Pau"               
    ape="Lezán"
    lista_de_notas=[95,9,5,8,6,3,2,14,7,2]

    diccionario={ 'nombre':nom, 'apellido':ape, 'lista':lista_de_notas}

    plantilla=loader.get_template ('template1.html') # leemos el archivo , lo convertimos en template y lo guardamos en una variable
    
    documento=plantilla.render(diccionario)
    return HttpResponse (documento)
