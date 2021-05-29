from django.db import models

class AbstractModel(models.Model):
    def __str__(self):
        return str(self.__dict__)
    class Meta:
        abstract = True

class Usuario(AbstractModel):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    descripcion = models.TextField()
    post_likeados = models.ManyToManyField('Post', through='Like', related_name='usuarios')

class Post(AbstractModel):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comentario(AbstractModel):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(AbstractModel):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='likes')





# Create your models here.
