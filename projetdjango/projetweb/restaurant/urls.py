from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.page_accueil, name='accueil'),
    path('menu/', views.page_menu, name='menu'),
    path('client/', views.page_client, name='client'),
    path('employe/', views.page_employe, name='employe'),

    # UTILISER TA VUE personnalisée pour gérer les rôles !
    path('login/', views.login_view, name='login'),

    # Logout standard
    path('logout/', auth_views.LogoutView.as_view(next_page='accueil'), name='logout'),

    # Inscription
    path('register/', views.register, name='register'),
]
