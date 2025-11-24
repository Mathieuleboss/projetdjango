from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Page Accueil
def page_accueil(request):
    return render(request, "restaurant/accueil.html")

# Page Menu
def page_menu(request):
    return render(request, "restaurant/menu.html")

# Page Connexion
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')
            elif user.profile.role == 'employe':
                return redirect('/employe/')
            else:
                return redirect('/client/')
        else:
            messages.error(request, "Nom ou mot de passe incorrect.")

    return render(request, "restaurant/login.html")

# Page Client
def page_client(request):
    return render(request, "restaurant/client.html")

# Page Employé
def page_employe(request):
    return render(request, "restaurant/employe.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data["role"]

            # on met à jour le profil automatiquement créé
            user.profile.role = role
            user.profile.save()

            login(request, user)
            return redirect('accueil')
    else:
        form = RegisterForm()

    return render(request, 'restaurant/register.html', {'form': form})