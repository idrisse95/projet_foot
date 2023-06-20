
from django.contrib import admin
from django.urls import path

from home.views import *
from equipes.views import *
from joueur.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addJoueur/', addJoueur, name='addJoueur'),
    path('addEquipe/', addEquipe, name='addEquipe'),
    path('editJoueur/<int:id>', editJoueurs, name='editJoueur'),
    path('editEquipe/<int:id>', editEquipes, name='editEquipe'),
    path('show/<int:id>', details_joueur, name='detail'),

    
]