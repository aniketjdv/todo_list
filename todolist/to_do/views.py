from django.shortcuts import render
from .forms import Todoform
from api.models import TodoList
from api.urls import router
import requests
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def todo(request):
    if request.method == 'POST':
        form=Todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo') 
    else:
        form=Todoform()
    response = requests.get('http://127.0.0.1:8000/api/v1/todos/')
    data = response.json()
    return render(request,'todo.html',{'form':form,'data':data})

def delete_item(request, item_task_id):
    id=item_task_id
    if request.method == 'POST':
        item=TodoList.objects.get(pk=id)
        item.delete()
        return redirect('/todo')