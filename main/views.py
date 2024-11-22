from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from users.models import Listing
from users.forms import ListingForm,LocationForm

def main_view(request):
    return render(request,"main/post_list.html",{"name":"site"})


def home_view(request):
    return render(request,"main/home.html")

def list_view(request):
    if request.method == "POST":
        pass
    if request.method == "GET":
        listing_form=ListingForm()
        location_form=LocationForm()
    return render(request, "main/list.html",{"listing_form":listing_form,"location_form":location_form})
