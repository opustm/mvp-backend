# Generated by Django 3.1.2 on 2020-12-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_user_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clique',
            name='isParent',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='teams',
        ),
        migrations.AddField(
            model_name='clique',
            name='cliqueType',
            field=models.CharField(choices=[('sub', 'SUB'), ('team', 'Team'), ('class', 'CLASS'), ('ensemble', 'ENSEMBLE'), ('club', 'CLUB'), ('social', 'SOCIAL')], default=('sub', 'SUB'), max_length=100),
        ),
        migrations.AddField(
            model_name='schedule',
            name='cliques',
            field=models.ManyToManyField(related_name='cliquesSchedule', to='main.Clique'),
        ),
    ]
