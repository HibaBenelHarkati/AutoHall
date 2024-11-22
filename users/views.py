from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Locations, Listing
from .forms import ProfileForm,LocationForm,ListingForm
from django.contrib.auth.decorators import login_required

login_form = AuthenticationForm()

def home_view(request):
    listing=Listing.objects.all()   #recuperer tout des objects listing de voiture de la bd
    return render(request,"main/home.html",{"listing":listing})
def login_view(request):   # enregistrer l user
    if request.method=="POST":
        username=request.POST["username"]
        password = request.POST["password"]
        user=authenticate(request, username=username, password=password)  #returns an objt
        if user is not None:
            login(request, user)
            return redirect("home")
    else:
         return render(request, "users/login.html",{"login_form": login_form})


def register_view(request):  #cette fct permet d enregistrer(juste username et mt pass)
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #une fois qu on enregistrer l user on va lui creer un profil

                return redirect("home")
    else:
        register_form = UserCreationForm()
    return render(request, "users/register.html", {"register_form": register_form})


@login_required
def create_profile_location(request): #cette fct permet d ajouter les donnees du profil et les modififer
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        profile_form=ProfileForm(request.POST, request.FILES, instance=profile)
        location_form = LocationForm(request.POST, instance=profile.location)
        if profile_form.is_valid() and location_form.is_valid():
            location = location_form.save()
            profile.location = location
            profile = profile_form.save(commit=False)
            profile.save()
            return redirect("home")
    else:
        profile_form = ProfileForm(instance=profile)
        location_form = LocationForm(instance=profile.location)

    return render(request, "users/profile.html", {"profile_form": profile_form, "location_form": location_form})


def logout1(request):
    logout(request)
    return redirect("post_list")
def edit(request,id):
    listing = Listing.objects.get(id=id)
    if request.method=="POST":
        pass
    else:
        listing_form=ListingForm(instance=listing)
        location_form=LocationForm(instance=listing.location)
    return render(request,"main/edit.html",{"location_form":location_form, "listing_form":listing_form})




