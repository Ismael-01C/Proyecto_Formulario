from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def principal(request):
    return render(request, 'principal.html')

def registro(request):
    return render(request, 'registro.html')

def doctor(request):
    return render(request, 'doctor.html')

# def tablas(request):
#     return render(request, 'tablas-registro.html')