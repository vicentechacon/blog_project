from django.shortcuts import render
from .models import Usuario, Post, Like, Comentario

def index(request):
    context = {
        'posts' : Post.objects.all().order_by('created_at')
        }
        
    return render(request, 'blog_app/index.html', context)

# Create your views here.
