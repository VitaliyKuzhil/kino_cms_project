from django.shortcuts import render

# Create your views here.


def list_films(request):
    return render(request, 'cinema/list_films.html')


def list_cinemas(request):
    return render(request, 'cinema/list_cinemas.html')


def home_page(request):
    return render(request, 'cinema/home_page.html')


def sessions(request):
    return render(request, 'cinema/sessions.html')


