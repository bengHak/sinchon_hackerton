from django.shortcuts import render,redirect
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def checkpage(request):
     return render(request, "checkbox.html")
'''
from django.shortcuts import redirect 

def checkpage(request): 
    if not request.user.is_authenticated(): 
        return redirect('home.html')
    else:
        return render(request, "checkbox.html")

'''