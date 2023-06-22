from django.shortcuts import render,redirect, get_object_or_404
from equipes.models import Equipe
from .models import Joueur
from .forms import JoueurForm

# Create your views here.
def addJoueur(request):
    if request.method == "POST":
        form = JoueurForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            team = form.cleaned_data['equipe']
            num_players = Joueur.objects.filter(equipe=team).count()

            #? Max players by role
            if team:
                role = player.role
                if role != 'Remplacant' and team.joueur_set.filter(role=role).count() >= 4:
                    error_message = f"L'équipe {team.club} a déjà atteint le maximum de joueurs pour le rôle {role}."
                    return render(request, 'projet_foot/joueurs/addJoueurs.html', {'form': form, 'error_message': error_message})

            #? Max players by team
            if num_players >= 12:
                error_max_players = f"L'équipe {team.club} est déjà complète. Veuillez en choisir une autre."
                return render(request, 'projet_foot/joueurs/addJoueurs.html', {'form': form, 'error_max_players': error_max_players})

            player.team = team
            player.save()

            return redirect("home")
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