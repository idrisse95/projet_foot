
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
    path('showEquipe/<int:id>', details_equipe, name='detailEquipe')

    
]

# une section ( équipes remplies )
# une section ( 2 équipes non remplies )
# une section ( 4 joueurs sans équipes au hasard )
# une section ( 4 joueurs avec équipe )
# une section ( les equipes d'europes )
# une section ( les équipes hors europes )
# Une section 5 joueuses au hasard qui ont une équipe !
# Une section 5 joueurs homme et qui ont une équipe !
