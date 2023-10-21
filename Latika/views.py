from django.shortcuts import render
import os
def index(request):
    return render(request, 'index.html', {})

# def galeria(request): esto cuando estaba en bbdd
#     return render(request, 'galeria.html', {})

# def galeria(request):
#     ruta_carpeta = os.path.join(os.path.dirname('static/'), )

#     imagenes = [imagen for imagen in os.listdir(ruta_carpeta) if imagen.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

#     return render(request, 'galeria.html', {'imagenes': imagenes})