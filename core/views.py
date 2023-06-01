from django.shortcuts import render


# Create your views here.
def base_user(request):
    return render(request, 'cinema/home_page.html')


def base_admin(request):
    return render(request, 'core/base_admin_page.html')
