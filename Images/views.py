from django.shortcuts import render
from .models import Image
import os

# Esto creado para sacar de la base de datos
# def galeria(request):
#     images = Image.objects.all()
#     return render(request, 'galeria.html', {'images': images})
def galeria(request):
    ruta_carpeta = os.path.join(os.path.dirname('static/imgs/'), )

    imagenes = [imagen for imagen in os.listdir(ruta_carpeta) if imagen.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    return render(request, 'galeria.html', {'imagenes': imagenes})