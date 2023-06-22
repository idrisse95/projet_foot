from django.shortcuts import render,redirect, get_object_or_404
from equipes.models import Equipe
from .models import Joueur
from .forms import JoueurForm

# Create your views here.
def addJoueur(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            equipe = form.cleaned_data['equipe']
            if equipe.joueur_set.count() >= 12:
                error_message = "The club already has the maximum number of players."
                return render(request, 'projet_foot/joueurs/addJoueurs.html', {'form': form, 'error_message': error_message})
            
            role = form.cleaned_data['role']
            if Joueur.objects.filter(role=role).count() >= 4:
                error_message = "The maximum limit of players for this role has been reached."
                return render(request, 'projet_foot/joueurs/addJoueurs.html', {'form': form, 'error_message': error_message})
            
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
    equipe = Equipe.objects.all()
    joueur = get_object_or_404(Joueur, id=id)
    return render(request, 'projet_foot/joueurs/showJoueurs.html', {'joueur': joueur,'equipe':equipe})