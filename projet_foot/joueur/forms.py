from django import forms
from .models import Joueur



class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = '__all__'
        null=True
        blank=True

def init (self, args, kwargs):
        super(JoueurForm, self).init(args, kwargs)
        self.fields["equipe"].requierd = False
