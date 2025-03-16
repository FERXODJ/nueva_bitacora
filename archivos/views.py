from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario

def archivos(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirigir a una página de éxito
    else:
        form = UsuarioForm()
    return render(request, 'index.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirigir a una página de éxito
    else:
        form = UsuarioForm()
    return render(request, 'index.html', {'form': form})

def success(request):
    usuarios = Usuario.objects.all()
    return render(request, 'success.html', {'usuarios': usuarios})