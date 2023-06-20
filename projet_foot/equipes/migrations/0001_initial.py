# Generated by Django 4.2.1 on 2023-06-19 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('pays', models.CharField(max_length=50)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipes.continent')),
            ],
        ),
    ]
