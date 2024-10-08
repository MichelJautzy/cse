# Generated by Django 5.0.4 on 2024-06-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('code_reference', models.CharField(max_length=16)),
                ('prix', models.FloatField()),
            ],
        ),
    ]
