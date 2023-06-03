from django.shortcuts import render


# Create your views here.
def base_user(request):
    return render(request, 'cinema/home_page.html')


def news(request):
    return render(request, 'core/news.html')


def shares(request):
    return render(request, 'core/shares.html')


def list_pages(request):
    return render(request, 'core/list_pages.html')


def mailing(request):
    return render(request, 'core/mailing.html')

