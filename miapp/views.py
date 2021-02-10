from django.shortcuts import render, HttpResponse

# Create your views here.

def layout(request):
    return render(request, 'layout.html')
    

def index(request):
    return render(request, 'index.html')
       

def hola_mundo(request):
    return render(request, 'hola_mundo.html')
   

def pagina(request):
    return render(request, 'pagina.html')
