from django.shortcuts import get_object_or_404, redirect, render
from .models import Publicacion
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')

        Publicacion.objects.create(
            titulo=titulo,
            contenido=contenido,
            autor=request.user  
        )
        return redirect('ver_publicaciones')  

    return render(request, 'crear_post.html')

def ver_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_publicacion')  # Obtener todas las publicaciones
    return render(request, 'ver_post.html', {'publicaciones': publicaciones})

@login_required
def detalle_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    return render(request, 'detalle_post.html', {'publicacion': publicacion})

def eliminar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('ver_publicaciones') 

    return render(request, 'eliminar_post.html', {'publicacion': publicacion})

def pagina_principal(request):
    return render(request, 'base.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada con éxito. Puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
        pass
    return render(request, 'registration/registro.html', {'form': form})