from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddAdvForm


from .models import *
def index(request):
    #posts = Board.objects.all()

    search_query = request.GET.get('q', '')

    if search_query:
        posts = Board.objects.filter(name__contains=search_query)
    else:
        posts = Board.objects.all()

    return render(request, 'board/index.html', {'posts': posts})

def addadv(request):
    if request.method == "POST":
        form = AddAdvForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
        return redirect("/")
    else:
        form = AddAdvForm()

    return render(request, 'board/addadv.html', {"form": AddAdvForm})

def pageNotFound(request, exception):
    return HttpResponse('<h1>404 Страница не найдена</h1>')