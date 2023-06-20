
from django.shortcuts import render, redirect
from .models import Equipe
from .forms import EquipeForm

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