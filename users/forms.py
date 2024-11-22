from django import forms
from .models import Profile,Locations, Listing
#ref: https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/#the-meta-class
#creons un formulaire a partir de django formd

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["user","bio", "photo", 'phone_number']


class LocationForm(forms.ModelForm):
    class Meta:
        model=Locations
        fields = ["address_1", "address_2", "city"]

class ListingForm(forms.ModelForm):
    class Meta:
        model=Listing
        fields = ["brand", "color", "engine", "transmission","image"]
        #j ai eliminer le id car il est genere et non editable
