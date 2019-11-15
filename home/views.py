<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'index.html')
=======
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
>>>>>>> d83e75488d7e21a699bdcef4a917e771fc2f60d3
