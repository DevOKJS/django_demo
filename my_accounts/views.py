from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def sign_up(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        if (username and password and password == password_check):
            try:
                new_user = User.objects.create_user(username=username, password=password)
                auth.login(request, new_user)
                return redirect('blog:home')
            except:
                context['error'] = '이미있음 딴거하샘'
        else: 
            context['error'] = '제대로 입렫 하세용'


    return render(request, 'my_accounts/sign_up.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('landing:home')
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username and password):
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('blog:home')
            else:
                context['error'] = '아이디 비번 틀렸어용'
        else:
            context['error'] = '아이디 비번 입력하세용'
    return render(request, 'my_accounts/login.html', context)

def naver_test(request):
    return render(request, 'my_accounts/naver_test.html')