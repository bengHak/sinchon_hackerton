from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def checkpage(request):
    return render(request, "checkbox.html")