from django.shortcuts import render, redirect
from .models import Usuario, Post, Like, Comentario

def index(request):
    context = {
        'posts' : Post.objects.all().order_by('created_at')
        }
        
    return render(request, 'blog_app/index.html', context)

def crear_post(request):
    if request.method == "POST":
        errors = Post.objects.validacion_basica(request.POST)
        print(errors)
        if len(errors) > 0:  #esto significa que hay un error
            context = {
                "errors" : errors
            }
            return render(request, 'blog_app/crear_post.html',context)

        titulo = request.POST["titulo"]
        contenido = request.POST["contenido"]
        
        nueva_entrada = Post(titulo = titulo, contenido = contenido)
        nueva_entrada.save()

        return redirect ('/')
    
    context = {}

    return render (request, 'blog_app/crear_post.html', context)

    
