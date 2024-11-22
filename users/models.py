from django.db import models
from django.contrib.auth.models import User #user=modele
#chaque user doit avoir un profil
import uuid


class Locations(models.Model):
    address_1=models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    def __str__(self):
        return f"Location : {self.address_1}"

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(null=True)
    bio=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10,blank=True)
    location=models.OneToOneField(Locations, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"Profil de {self.user.username}"

#class pur lister les voitures voir (desc...)
CARS_BRANDS = (
    ('bmw', 'BMW'), #bmw=> stocker ds ma db et BMW va apparaitre  mon user
    ('mercedes benz', 'Mercedes Benz'),
    ('audi', 'Audi'),
    ('subaru', 'Subaru'),
    ('tesla', 'Tesla'),
    ('jaguar', 'Jaguar'),
    ('land rover', 'Land Rover'),
    ('bentley', 'Bentley'),
    ('bugatti', 'Bugatti'),
    ('ferrari', 'Ferrari'),
    ('lamborghini', 'Lamborghini'),
    ('honda', 'Honda'),
    ('toyota', 'Toyota'),
    ('chevrolet', 'Chevrolet'),
    ('porsche', 'Porsche')
)
TRANSMISSION_OPTIONS = (
    ('automatic', 'Automatic'),
    ('manual', 'Manual'),
)
def user_directory_path(instance, filename):
    return f"media/user_{0}/listing/{filename}"


class Listing(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True, editable=False)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    seller=models.ForeignKey(Profile,on_delete=models.CASCADE) #SI LE PROFILE EST SUPPRIME EN ELIMINE AUTOMTIQUEMENT LE LISTING DES VOITEURES
    brand=models.CharField(max_length=20,choices=CARS_BRANDS,default=None) #choices est une liste de tuple
    color=models.CharField(max_length=10)
    description=models.TextField()
    engine=models.CharField(max_length=20)
    transmission=models.CharField(max_length=20,choices=TRANSMISSION_OPTIONS,default=None)
    location=models.OneToOneField(Locations,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to=user_directory_path)
    def __str__(self):
        return f"Liste de { self.seller.user.username}"

