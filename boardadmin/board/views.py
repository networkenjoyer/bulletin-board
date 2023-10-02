from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddAdvForm
from django.views.generic import DetailView


from .models import *
def index(request):
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

class CardDetailView(DetailView):
    model = Board
    template_name = 'board/descadv.html'
    #context_object_name = 'adv'

#def CardDView(request):
    #return render(request, "board/descadv.html")


def pageNotFound(request, exception):
    return HttpResponse('<h1>404 Страница не найдена</h1>')