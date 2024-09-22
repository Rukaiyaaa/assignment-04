from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel
from . import forms

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'add_task.html', {'form': form})


def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')


def complete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('homepage')
