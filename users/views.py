from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from users.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('polls:index')
    else:
        form = UserForm()

    return render(request, 'users/signup.html', {'form': form})

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('polls:index')
        else:
            return render(request, 'users/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('polls:index')