from django.shortcuts import render
from task.models import TaskModel

def show_tasks(request):
    tasks = TaskModel.objects.prefetch_related('categories').all()
    return render(request, 'home.html', {'tasks': tasks})