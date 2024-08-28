from django.urls import path
from . import views
from .views import produit, produits, categories, sous_categories, signup, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('produits', produits, name='produits'),
    path('produits/<int:sousCategorieID>', produits, name='produits'),
    path('produit/<int:pk>', produit, name='produit'),

    path('categories', categories, name='categories'),
    path('sous-categories', sous_categories, name='sous-categories'),
    path('sous-categories/<int:categorieID>', sous_categories, name='sous-categories'),

    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='produits'), name='logout'),
    path('profile/', profile, name='profile'),

    path('ajouter-au-panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.voir_panier, name='voir_panier'),
    path('valider-panier/', views.valider_panier, name='valider_panier'),
    path('confirmation-commande/', views.confirmation_commande, name='confirmation_commande'),


]