from django.shortcuts import render
from django.shortcuts import render
#from .models import Choice

# Create your views here.
'''
def checkpage(request):
    return render(request,'checkbox.html')

from django.shortcuts import render
from .models import Choice
#같은 폴더에 위치한 models에서 정의한 Question과 Choice를 사용하기 위한 선언
def index(request): #함수 정의
    a = Question.objects.all() #a라는 변수에 Question 객체(Question의 모든 변수)
    return render(request, 'vote/index.html',{'a':a}) 
#template 폴더 밑의 vote/detail.html에 가공된 데이터를 전송해라.
#전송 시, 앞서만든 변수 a는 'a'(실제로는 a)라는 이름으로 전송해라.
'''