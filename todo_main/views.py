from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task


def home(request):
    # return HttpResponse("<h2>This is my todo list</h2>")
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    context = {
        'tasks': tasks, 
    }
    print(context)
    return render(request, 'home.html', context)