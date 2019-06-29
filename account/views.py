from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile

# Create your views here.

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            profile = Profile(user=user)
            profile.save()
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            profile = Profile.objects.get(user=user)
            auth.login(request, user)
            print(profile.vote)
            vote_num = profile.vote
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout(request):
    print('Loggin out {}'.format(request.user))
    auth.logout(request)
    return redirect('home')

'''
from django.http import HttpResponseRedirect
from django.contrib import messages
def checkpage(request):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:    #로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseForbidden()
        else:
            return render(request, "checkbox.html")
'''

    