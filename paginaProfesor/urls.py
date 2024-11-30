from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  
    path('index/', views.index, name='index'),  
    path('generar_qr/', views.generar_qr, name='generar_qr'), 
]
