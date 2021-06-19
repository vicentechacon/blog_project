from django.db import models


class AbstractModel(models.Model):
    def __str__(self):
        return str(self.__dict__)
    class Meta:
        abstract = True


class PostManager(models.Manager):
    def validacion_basica(self, post_data):
        errors = {
        }
        
        if len(post_data["titulo"]) < 4:
            errors["titulo"] = "El título no puede ser menor a 4 caracteres"
        
        if len(post_data["contenido"]) == 0:
            errors["contenido"] = "El contenido no puede estar vacío"

        return errors


class Post(AbstractModel):
    titulo = models.CharField(max_length=255)
    created_by = models.ForeignKey('login_project_app.Usuario', related_name='posts', on_delete=models.CASCADE)
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()
    users_who_liked = models.ManyToManyField('login_project_app.Usuario', through= "Like")


class Comentario(AbstractModel):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    created_by = models.ForeignKey('login_project_app.Usuario', related_name='comentarios', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(AbstractModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    usuario = models.ForeignKey('login_project_app.Usuario', on_delete=models.CASCADE, related_name='likes')

    