import qrcode
from io import BytesIO
from django.http import JsonResponse
import base64
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
    usuarios = Usuario.objects.all()
    asignaturas = Asignatura.objects.all()  

    context = {
        "usuarios": usuarios,
        "asignaturas": asignaturas,        
    }

    return render(request, 'pages/index.html', context)

def generar_qr(request):
    if request.method == "POST":
        asignatura_id = request.POST.get("asignatura")
        seccion = request.POST.get("seccion")
        
        # Validar que la asignatura exista
        try:
            asignatura_obj = asignatura_obj = Asignatura.objects.get(nombreAsignatura=asignatura_id)
        except Asignatura.DoesNotExist:
            return JsonResponse({"error": "Asignatura no encontrada"}, status=404)
        
        # Generar el contenido del QR
        qr_data = f"Asig: {asignatura_obj.nombreAsignatura}, Sec: {seccion}"

        # Crear el código QR
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)
        
        # Convertir el QR a base64
        qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return JsonResponse({"qr_data": qr_base64})
    
    return JsonResponse({"error": "Método no permitido"}, status=405)
