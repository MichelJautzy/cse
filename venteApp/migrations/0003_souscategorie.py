# Generated by Django 5.0.4 on 2024-06-27 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venteApp', '0002_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='SousCategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venteApp.categorie')),
            ],
        ),
    ]
