from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("<h2>This is my todo list</h2>")
    return render(request, 'home.html')