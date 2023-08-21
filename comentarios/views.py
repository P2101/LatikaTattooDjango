from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.


def test(request):
    return HttpResponse('hola')


def create(request):
    # comment = Comment(name="Pepe", score=5, comment='El Barça és el millor equip del món')
    # comment.save()

    # comment = Comment.objects.create(name="Juan", score=10, comment='El Barça és el millor equip del món')
    return HttpResponse('hola')


def delete(request):
    # comment = Comment.objects.get(id=1)
    # comment.delete()

    # Comment.objects.filter(id=2).delete()
    return HttpResponse('Elemento eliminado')
