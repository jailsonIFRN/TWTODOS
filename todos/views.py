from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# serve para redenrisa o template
def home(request):
    return render(request, "todos/home.html")


