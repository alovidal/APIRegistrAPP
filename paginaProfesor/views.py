from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from api.models import *

# Vista de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  # Redirigir al índice si la autenticación es exitosa
        else:
            return render(request, 'pages/login.html', {'mensaje': 'Usuario o contraseña incorrectos.'})
    return render(request, 'pages/login.html')

# Vista protegida
@login_required
def index(request):
    usuarios = usuario.objects.all()

    context = {
        "usuarios": usuarios,
    }

    return render(request, 'pages/index.html', context)
