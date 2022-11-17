# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'nome': "Everton"
    })


def contact(request):
    return render(request, 'teste.html')


def about(request):
    return render(request, 'recipes/about.html')
