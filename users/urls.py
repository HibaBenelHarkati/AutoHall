from django.urls import path
from .views import login_view
from django.urls import path
from .views import home_view,register_view,create_profile_location, edit
from .views import logout1

urlpatterns=[
    path("login/",login_view,name="login"),
    path("home/", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("profile/", create_profile_location, name="profile"),
    path("logout1/", logout1, name="logout1"),
    path("edit/<uuid:id>/", edit, name="edit")

]