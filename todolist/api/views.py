from django.shortcuts import render
from api.models import TodoList
from api.serializers import TodoSerializers
from rest_framework import viewsets
# Create your views here.

class TodoViewset(viewsets.ModelViewSet):
    queryset=TodoList.objects.all()
    serializer_clas=TodoSerializers