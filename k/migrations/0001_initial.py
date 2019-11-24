# Generated by Django 2.2.1 on 2019-11-19 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('Client', 'CLIENT'), ('Ouvrier', 'OUVRIER'), ('Apprenti', 'APPRENTI'), ('Fournisseur', 'FOURNISSEUR'), ('Company', 'COMPANY')], default='CLIENT', max_length=20)),
                ('prenom', models.CharField(blank=True, max_length=30, null=True)),
                ('nom', models.CharField(blank=True, max_length=30, null=True)),
                ('sex', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('G', 'Garçon'), ('f', 'Fille'), ('A', 'Autres')], default='Homme', max_length=200)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('domicile', models.CharField(default='Lafiabougou', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modele', models.CharField(blank=True, max_length=30, null=True)),
                ('tissu', models.CharField(blank=True, max_length=30, null=True)),
                ('couleur', models.CharField(blank=True, max_length=30, null=True)),
                ('metrage', models.PositiveSmallIntegerField()),
                ('coud', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('epaule', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('manche', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('tour_manche', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('taille', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('poitrine', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('longueur_boubou', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('longueur_patanlon', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('fesse', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ceinture', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('cuisse', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('patte', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('avance', models.PositiveIntegerField()),
                ('montant_total', models.PositiveIntegerField()),
                ('rendez_vous', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='k.Person')),
            ],
        ),
    ]
