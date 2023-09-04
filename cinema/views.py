from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Movies, Cinemas

# Create your views here.


def list_films_all(request):
    films = Movies.objects.all()
    context = {'films': films}
    return render(request, 'cinema/list_films_all.html', context)


def detail_film(request, pk):
    film = get_object_or_404(Movies, pk=pk)
    context = {'film': film}
    return render(request, 'cinema/detail_films.html', context)


def list_films_soon(request):
    films = Movies.objects.filter(status_movie='soon')
    context = {'films': films}
    return render(request, 'cinema/list_films_soon.html', context)


def list_cinemas(request):
    cinemas = Cinemas.objects.all()
    context = {'cinemas': cinemas}
    return render(request, 'cinema/list_cinemas.html', context)


def home_page(request):
    if request.user.is_superuser:
        return redirect('user:statistic_admin')
    else:
        return render(request, 'cinema/home_page.html')


def sessions(request):
    if request.user.is_superuser:
        raise Http404()
    else:
        return render(request, 'cinema/sessions.html')


