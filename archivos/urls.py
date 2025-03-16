from django.urls import path
from . import views

urlpatterns = [
    path('', views.archivos, name='archivos'),  # Vista principal
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('success/', views.success, name='success'),  # Vista de éxito
]