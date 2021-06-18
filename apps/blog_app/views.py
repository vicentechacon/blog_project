from django.http.request import RAISE_ERROR
from django.shortcuts import render, redirect
from .models import Post, Like, Comentario
from apps.login_project_app.models import Usuario
from .utils import login_required
from django.core.exceptions import PermissionDenied

def index(request):
    context = {
        'posts' : Post.objects.all().order_by('created_at'),
        }
    if "id" in request.session:
        usuario = Usuario.objects.get(id = request.session["id"])
        context["usuario"] = usuario

    return render(request, 'blog_app/index.html', context)

@login_required
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
        
        nueva_entrada = Post(titulo = titulo, contenido = contenido, created_by_id=request.session['id'])
        nueva_entrada.save()

        return redirect ('/')
    
    context = {}

    return render (request, 'blog_app/crear_post.html', context)

@login_required
def ver_detalle(request, id_post):
    if request.method == "GET":
        post = Post.objects.get(id=id_post)
        context = {
            'post': post 
        }
        return render(request,"blog_app/ver_detalle.html",context)

@login_required
def editar(request, id_post):
    post = Post.objects.get(id=id_post)
    if post.created_by_id != request.session['id']:
        raise PermissionDenied()

    if request.method == 'GET':
        context = {
            'post' : post
        }
        return render(request, 'blog_app/editar.html', context)
    if request.method == "POST":
        errors = Post.objects.validacion_basica(request.POST)
        print(errors)
        if len(errors) > 0:  #esto significa que hay un error
            context = {
                "errors" : errors,
                'post': post
            }
            return render(request, 'blog_app/editar.html',context)

        post.titulo = request.POST["titulo"]
        post.contenido = request.POST["contenido"]
        
        post.save()

        return redirect ('/')

@login_required
def eliminar(request, id_post):
    post = Post.objects.get(id=id_post)
    if post.created_by_id != request.session['id']:
        raise PermissionDenied()
    post.delete()
    return redirect('/')

@login_required
def like(request, id_post):
    user = Usuario.objects.get(id = request.session["id"])
    post = Post.objects.get(id = id_post)
    like = Like.objects.get_or_create(post = post,usuario = user)

    return redirect("/")

@login_required
def unlike(request, id_post):
    user = Usuario.objects.get(id = request.session["id"])
    post = Post.objects.get(id = id_post)
    like = Like.objects.get(post = post,usuario = user)
    like.delete()

    return redirect("/")


    

    
    