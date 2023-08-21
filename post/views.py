from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse

# Create your views here.
# def post(request):
#     # name = Author.objects.create(name='Juan Gomez Jurado', email='jgj@gmail.com')
#     # name.save()
#     pass

def queries(request):
    # Todos
    authors = Author.objects.all()
    # Filtrados
    filtered = Author.objects.filter(email='lopezeddie@example.com') # Para verlo, hay que recorrer, ya que puede haber más de uno
    # Obtener un único objeto
    author = Author.objects.get(id=1)
    # 5 primers
    limits = Author.objects.all()[:5]
    # 5 a partir des 5 primers 
    antilimits = Author.objects.all()[5:10]
    # Ordenar
    orders = Author.objects.all().order_by('email')
    # Obtener todos con id <= 10
    filtered2 = Author.objects.filter(id__lte= 10) # lower than equals, __gtl= IMPORTANT (greater than equal)
    # Obtener todos los autores que contienen la palabra hotel
    filtered3 = Author.objects.filter(name__contains="hotel")

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'antilimits': antilimits, 'orders': orders, 'filtered2': filtered2, 'filtered3': filtered3})

def update(request):
    author = Author.objects.get(id=2)
    author.name = 'Pepe'
    author.email = 'pepepapolte@gmail.com'
    author.save()
    return HttpResponse('usuario actualizado')