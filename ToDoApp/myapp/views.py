from django.shortcuts import render
from .models import TodoModel
# Create your views here.

def ToDoList(request):
    todo = TodoModel.objects.all
    contex = {
        'todo ' : todo
    }
    return render(request, 'index.html', contex) 