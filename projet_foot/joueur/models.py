from django.db import models
from equipes.models import Equipe

class Roles(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Joueur(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    image = models.URLField()
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, null=True, blank=True, on_delete=models.CASCADE)

