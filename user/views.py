from django.shortcuts import render, redirect


def login(request):
    return render(request, 'user/login.html')


def register(request):
    return render(request, 'user/register.html')


def profile(request):
    return render(request, 'user/profile.html')
