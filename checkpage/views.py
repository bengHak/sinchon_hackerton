from django.shortcuts import render,redirect
from django.shortcuts import render
'''
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
'''
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import Profile
# now = datetime.datetime.now().strftime('%H:%M:%S')

# Create your views here.

def checkpage(request):
     return render(request, "checkbox.html")

from django.shortcuts import redirect


def sum(request):
    if request.method == 'POST':
        tumbler=request.POST['tumbler']
        public_transportation=request.POST['public_transportation']
        ecobag=request.POST['ecobag']
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            profile.vote += int(tumbler) + int(public_transportation)*6 + int(ecobag)
            profile.accumulate += int(tumbler) + int(public_transportation)*6 + int(ecobag)
            profile.save()
            return redirect("home")
    return redirect("home")