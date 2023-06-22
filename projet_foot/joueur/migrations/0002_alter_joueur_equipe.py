# Generated by Django 4.2.1 on 2023-06-20 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipes', '0001_initial'),
        ('joueur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joueur',
            name='equipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipes.equipe'),
        ),
    ]
