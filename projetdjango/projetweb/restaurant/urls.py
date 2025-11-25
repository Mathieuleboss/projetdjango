from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_accueil, name='accueil'),
    path('menu/', views.page_menu, name='menu'),

    # Espace client/employé
    path('client/', views.page_client, name='client'),
    path('employe/', views.page_employe, name='employe'),

    # Authentification personnalisée
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Inscription
    path('register/', views.register_view, name='register'),

    # Réservations
    path('reservations/', views.reservations, name='reservations'),
    path('mes_reservations/', views.mes_reservations, name='mes_reservations'),

    # Autres pages
    path('commander/', views.commander, name='commander'),
    path('avis/', views.avis, name='avis'),
]
