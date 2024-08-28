from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Panier(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)

    def __str__(self):
        return f"Panier de {self.utilisateur.username} créé le {self.date_creation}"

class Article(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} dans le panier de {self.panier.utilisateur.username}"