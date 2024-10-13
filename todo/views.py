from django.shortcuts import render, redirect
from .models import TodoModel
from api.models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {"todos": todos}

    return render(request, "index.html", context=context)

def createTodo(request):
    if request.method == 'POST':
        body = request.POST.get('body')
        todo = Todo.objects.create(body=body)
        todo.save()

        return redirect('todo:index')
    

def updateTodo(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        todo = Todo.objects.get(id=todo_id)

        todo.completed = True
        todo.save()

        return redirect('todo:index')
    
def deleteTodo(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        
        return redirect('todo:index')