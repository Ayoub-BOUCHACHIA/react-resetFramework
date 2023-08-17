from django.shortcuts import render
from .serializers import TodoSerializer , EurUsdSerializer
from rest_framework import viewsets

from .models import Todo , EurUsd 
# Create your views here.


def index(request):
    return render(request, 'appreact/index.html')


def index_react(request):
    return render(request, 'index.html')


class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer   
    queryset = Todo.objects.all()

class EurUsdView(viewsets.ModelViewSet):  
    serializer_class = EurUsdSerializer   
    queryset = EurUsd.objects.all()