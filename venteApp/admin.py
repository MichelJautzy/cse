from django.contrib import admin
from .models import Produit, Categorie, SousCategorie

admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(SousCategorie)