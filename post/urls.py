from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('post/', views.post, name='post'),
    path('queries/', views.queries, name='queries'),
    path('update/', views.update, name='update'),
]