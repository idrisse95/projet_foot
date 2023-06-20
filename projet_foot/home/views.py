from django.shortcuts import render, redirect
from joueur.models import Joueur
from equipes.models import Equipe


# Create your views here.
def home(request):
    allJoueur = Joueur.objects.all()
    allEquipe = Equipe.objects.all()
    return render(request, 'projet_foot/home.html', {"allJoueur":allJoueur, "allEquipe": allEquipe})


