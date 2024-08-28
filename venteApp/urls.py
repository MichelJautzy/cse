from django.urls import path
from .views import produit, produits, categories, sous_categories

urlpatterns =[
    path('produits', produits, name='produits'),
    path('produits/<int:sousCategorieID>', produits, name='produits'),
    path('produit/<int:pk>', produit, name='produit'),
    
    path('categories', categories, name='categories'),
    path('sous-categories', sous_categories, name='sous-categories'),
    path('sous-categories/<int:categorieID>', sous_categories, name='sous-categories'),
]