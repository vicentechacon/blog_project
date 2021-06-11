# Generated by Django 2.2.4 on 2021-06-10 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_app', '0001_initial'),
        ('login_project_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='login_project_app.Usuario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog_app.Post'),
        ),
    ]