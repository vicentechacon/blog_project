from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def nuevo(request):
    errores = Usuario.objects.validaciones_basicas(request.POST)
    if len(errores) > 0:
        for key, value in errores.items():
            messages.error(request, value)
        return redirect('/auth')
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        newusuario = Usuario.objects.create(first_name=request.POST['first_name'],last_name= request.POST['last_name'], email= request.POST['email'], password= hash1)

        request.session['id']= newusuario.id

    return redirect('/')

def success(request):
    if 'id' not in request.session:
        return redirect('/')
    usuario = Usuario.objects.get(id=request.session['id'])
    context = {
        'usuario' : usuario
    }
    return render(request, 'success.html', context)

def login(request):
    login_validator = Usuario.objects.login_validaciones(request.POST)
    if len(login_validator) > 0:
        for key, value in login_validator.items():
            messages.error(request, value)
        return redirect('/auth/')
    else:
        usuario = Usuario.objects.filter(email = request.POST['email'])[0]
        request.session['id'] = usuario.id
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/auth')

# def getUsuario(idUsuario = None, email= None):
# try:   
#     if idUsuario: 
#         usuario = Usuario.objects.get(id=idUsuario)
#     elif email:
#         usuario = Usuario.objects.get(email = email)
#     return usuario
# except:
#     return None