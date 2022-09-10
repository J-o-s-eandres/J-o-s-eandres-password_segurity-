from django.shortcuts import render
import random 


#funciones de prueba 
def about(request):
    return render(request,"generator/about.html")
# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def password(request):

    characters=list('abcdgharuopghuotsúghovhyonnóiuvíoyérpuióvuyenuuvuiuywvnpiuerynipvunuihvpwnxeorth')
    generated_password=""

    length= int(request.GET.get('length'))
 #-------------CONDICIONES PARA EL AGREGADO DE CARACTERES ESPECIALES,NUMEROS Y MAYUSCULAS AL PASSWORD-----------------------
    
    if request.GET.get('uppercase'):#Agg letras Mayusculas
        characters.extend(list('ABCDGHARUOPGHUOTSÚGHOVHYONNÓIUVÍOYÉRPUIÓVUYENUUVUIUYWVNPIUERYNIPVUNUIHVPWNXEORTH'))

    if request.GET.get('special'):#Agg caracteres especiales
        characters.extend(list('!"#$%&/()=?¡¨*][_:;-'))

    if request.GET.get('numbers'):#agg numeros
        characters.extend(list('0147852369'))
    #-------------------------------FIN DE LAS CONDICIONES---------------------------------------------------------
    
    for x in range(length):#recorre la lista de posibles letras para el password y las coloca de forma aleatoria y guarada en variable
        generated_password += random.choice(characters)

    return render(request, "generator/password.html",{'password':generated_password})