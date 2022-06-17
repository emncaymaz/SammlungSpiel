from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from .models import Game, Review
from .forms import GameForm


def home_view(requerst):
    return render(requerst, 'game/home.html')

def game_view(request):

    games = Game.objects.all()

    context = {'games':games}
    return render(request, 'game/game.html', context)

def detail_view(request, pk):
    detail = get_object_or_404(Game, id=pk)
    context = {'detail':detail}
    return render(request, 'game/detail.html', context)


def create_view(request):
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('game:game'))
    context ={'form':form}
    return render(request, 'game/create.html', context)

def update_view(request,pk):
    game = get_object_or_404(Game, id=pk)
    form = GameForm(instance=game)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect(reverse('game:game'))
    context = {'form':form}
    return render(request, 'game/update.html',context)

def delete_view(request, pk):
    game = get_object_or_404(Game, id=pk)
    if request.method == 'POST':
        game.delete()
        return redirect(reverse('game:game'))
    return render(request, 'game/delete.html',{'game':game})