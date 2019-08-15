from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def dashboard(request):
    form = TodoForm
    user = request.user
    todo_list = Todo.objects.filter(user=user).order_by('completed')
    context = {
    'todo_list': todo_list,
    'form': form
    }
    return render(request, 'todos/dashboard.html', context)


@login_required
def add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()  
            messages.success(request, 'Item has been Added to List')
            return redirect('dashboard')
    else:
        form = TodoForm    
    return render(request, 'todos/add_todo.html', {'form': form})


@login_required
def delete(request, list_id):
    item = Todo.objects.get(id=list_id)
    item.delete()
    messages.success(request, 'Item has been deleted!')
    return redirect('dashboard')  


@login_required
def complete(request, list_id):
    item = Todo.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('dashboard')


@login_required
def my_details(request):
    user = request.user
    details = User.objects.filter(username=user)
    return render(request, 'todos/my_details.html', {'details': details})   
