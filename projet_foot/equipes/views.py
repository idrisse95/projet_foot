
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from joueur.models import *
from .forms import *

# Create your views here.
def addEquipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquipeForm()
    return render(request, 'projet_foot/equipes/addEquipes.html', {'form':form})



def editEquipes(request,id):
    edit = Equipe.objects.get(id=id)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = EquipeForm(instance=edit)
    return render(request, 'projet_foot/equipes/editEquipes.html', {'form': form})

def details_equipe(request, id):
    equipe = get_object_or_404(Equipe, id=id)
    joueurs = Joueur.objects.filter(equipe=equipe)
    context = {'equipe': equipe, 'joueurs': joueurs}
    return render(request, 'projet_foot/equipes/showEquipes.html', context)
