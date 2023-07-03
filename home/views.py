from django.shortcuts import render
from users.models import User

# Create your views here.

def mainpage(request):
    users = User.objects.all() #사용자 모델에서 모든 사용자 가져오기
    return render(request, "home/mainpage.html",{'users':users})