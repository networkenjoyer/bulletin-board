from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .models import *
def index(request):
    #posts = Board.objects.all()

    search_query = request.GET.get('q', '')

    if search_query:
        posts = Board.objects.filter(name__contains=search_query)
    else:
        posts = Board.objects.all()

    return render(request, 'board/index.html', {'posts': posts, 'title': 'Главная страница'})

def addadv(request):
    return render(request, 'board/addadv.html', {'title': 'Добавление обьявления'})

def pageNotFound(request, exception):
    return HttpResponse('<h1>404 Страница не найдена</h1>')