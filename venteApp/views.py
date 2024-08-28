from django.shortcuts import render
from .models import Produit, Categorie, SousCategorie

def produit(request, pk):
    req = "select * from venteApp_produit where id=%s"
    produits= Produit.objects.raw(raw_query=req, params=[pk])
    return render(
        request,
        "produit.html", 
        context={'produit': produits[0]})

def produits(request, sousCategorieID=None):
    req = "select * from venteApp_produit"
    if sousCategorieID is not None:
        req += " where sous_categorie_id=%s"
    if sousCategorieID is None:
        produits= Produit.objects.raw(raw_query=req)
    else:
        produits= Produit.objects.raw(raw_query=req, params=[sousCategorieID])
    return render(
        request,
        "produits.html", 
        context={'produits': produits})

def categories(request):
    req = "select * from venteApp_categorie"
    cats= Categorie.objects.raw(raw_query=req)
    return render(
        request,
        "categories.html", 
        context={'categories': cats})

# sous_categories 
def sous_categories(request, categorieID=None):
    req = "select * from venteApp_souscategorie" 
    if categorieID is not None:
        req += " where categorie_id=%s"

    if categorieID is not None:
        cats= SousCategorie.objects.raw(raw_query=req , params=[categorieID]) 
    else:
        cats= SousCategorie.objects.raw(raw_query=req)  
    print(cats)
    return render(
        request,
        "sous-categories.html", 
        context={'souscategories': cats})

