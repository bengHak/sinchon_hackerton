from django.shortcuts import render
from account.models import Profile
from datetime import datetime

# Create your views here.
#0이면 그날 갱신 함. 1이면 그날 갱신 안됨.
lastTime = datetime.now().day

def home(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        global lastTime
        if datetime.now().day != lastTime:
            profile.vote = 0
        level = profile.accumulate // 16
        exp = (((profile.accumulate) / 16 ) - level) * 100
        return render(request, "home.html", {"profile": profile, "level":level, "exp":exp})
    return render(request, "home.html")

