from django.db import models
from django.urls import reverse


class Categorie(models.Model):
    nom = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("sous-categories", kwargs={"categorieID": self.pk})

class SousCategorie(models.Model):
    nom = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='images', blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE) # SET_NULL

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("produits", kwargs={"sousCategorieID": self.pk})

class Produit(models.Model):
    nom = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    code_reference = models.CharField(max_length=16)
    prix = models.FloatField()
    sous_categorie = models.ForeignKey(SousCategorie, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("produit", kwargs={"pk": self.pk})