from django.contrib import admin
from .models import Profile, Locations

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile,ProfileAdmin)

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Locations,LocationAdmin)