import json

from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoginForm, CustomUserChangeForm
from django.contrib.auth.decorators import permission_required, login_required
from .models import CustomUser
from cinema.models import Movies, Seo
from .forms import EditFilmPageForm
from cinema.forms import SeoForm
from core.models import HomeBanner, HomeNewsSharesBanner, BackgroundBanner


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('user:statistic_admin')
                else:
                    return redirect('cinema:home_page')
            else:
                error_message = 'Invalid email or password.'
                return render(request, 'user/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('cinema:home_page')


@permission_required('is_superuser')
def base_admin(request):
    return render(request, 'core/statistic.html')


@permission_required('is_superuser')
def banners_view(request):
    home_banner = get_object_or_404(HomeBanner)
    home_news_shares_banner = get_object_or_404(HomeNewsSharesBanner)
    background_banner = get_object_or_404(BackgroundBanner)
    context = {'home_banner': home_banner,
               'home_news_shares_banner': home_news_shares_banner,
               'background_banner': background_banner}
    return render(request, 'core/banners.html', context)


@permission_required('is_superuser')
def list_users(request):
    users = CustomUser.objects.filter(is_superuser=False)

    context = {'users': users}
    return render(request, 'user/list_users.html', context)


@permission_required('is_superuser')
def edit_user(request, pk):
    user = CustomUser.objects.get(pk=pk)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = CustomUserChangeForm(instance=user)
    context = {'user_form': user_form, 'pk': pk}
    return render(request, 'user/edit_user.html', context)


@permission_required('is_superuser')
def delete_user(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user.delete()
    return redirect('user:list_users_admin')


@permission_required('is_superuser')
def list_films(request):
    films_old = Movies.objects.filter(status_movie='old')
    films_soon = Movies.objects.filter(status_movie='soon')
    context = {'films_old': films_old, 'films_soon': films_soon}
    return render(request, 'cinema/list_films.html', context)


@permission_required('is_superuser')
def edit_films(request, pk):
    film = get_object_or_404(Movies, pk=pk)
    if request.method == 'POST':
        film_form = EditFilmPageForm(request.POST or None, instance=film)
        seo_form = SeoForm(request.POST or None, instance=film.seo_movie)
        if film_form.is_valid() and seo_form.is_valid():
            film_form.save()
            seo_form.save()
            return redirect('user:list_films_admin')
    else:
        film_form = EditFilmPageForm(instance=film)
        seo_form = SeoForm(instance=film.seo_movie)

    context = {'film_form': film_form, 'seo_form': seo_form, 'film': film}
    return render(request, 'user/edit_films.html', context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {'form': form}
    return render(request, 'user/profile.html', context)
