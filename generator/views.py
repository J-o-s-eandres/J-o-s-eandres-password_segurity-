from django.shortcuts import render
import random 

def about(request):
    return render(request,"generator/about.html")
# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def password(request):

    characters=list('abcdgharuopghuotsúghovhyonnóiuvíoyérpuióvuyenuuvuiuywvnpiuerynipvunuihvpwnxeorth')
    generated_password=""

    length= int(request.GET.get('length'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, "generator/password.html",{'password':generated_password})