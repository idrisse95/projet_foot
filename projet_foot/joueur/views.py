from django.shortcuts import render,redirect, get_object_or_404
from .models import Joueur
from .forms import JoueurForm

# Create your views here.
def addJoueur(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JoueurForm()
    return render(request, 'projet_foot/joueurs/addJoueurs.html', {'form':form})


def editJoueurs(request,id):
    edit = Joueur.objects.get(id=id)
    if request.method == 'POST':
        form = JoueurForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = JoueurForm(instance=edit)
    return render(request, 'projet_foot/joueurs/editJoueurs.html', {'form': form})

def details_joueur(request, id):
    joueur = get_object_or_404(Joueur, id=id)
    return render(request, 'projet_foot/joueurs/showJoueurs.html', {'joueur': joueur})