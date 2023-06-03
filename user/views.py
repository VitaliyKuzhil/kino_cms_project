from django.shortcuts import render, redirect


def login(request):
    return render(request, 'user/login.html')


def register(request):
    return render(request, 'user/register.html')


def base_admin(request):
    return render(request, 'core/statistic.html')


def banners(request):
    return render(request, 'core/banners.html')


def list_users(request):
    return render(request, 'user/list_users.html')


def profile(request):
    return render(request, 'user/profile.html')
