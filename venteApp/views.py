from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Categorie, SousCategorie
from django.contrib.auth import login, authenticate
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileForm
from .models import UserProfile, Produit, Panier, Article



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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.userprofile.address = form.cleaned_data.get('address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('produits')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'form': form})


@login_required
def ajouter_au_panier(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    panier, created = Panier.objects.get_or_create(utilisateur=request.user, valide=False)

    article, created = Article.objects.get_or_create(
        panier=panier,
        produit=produit,
        defaults={'prix': produit.prix, 'quantite': 1}
    )

    if not created:
        article.quantite += 1
        article.prix = produit.prix * article.quantite
        article.save()

    return redirect('voir_panier')

@login_required
def voir_panier(request):
    panier, created = Panier.objects.get_or_create(utilisateur=request.user, valide=False)
    articles = Article.objects.filter(panier=panier)
    total = sum(article.prix for article in articles)
    return render(request, 'panier.html', {'articles': articles, 'total': total})

@login_required
def valider_panier(request):
    panier = get_object_or_404(Panier, utilisateur=request.user, valide=False)
    panier.valide = True
    panier.save()
    messages.success(request, "Votre commande a été validée avec succès!")
    return redirect('confirmation_commande')



@login_required
def confirmation_commande(request):
    return render(request, 'confirmation_commande.html')