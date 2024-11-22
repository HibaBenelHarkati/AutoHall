from django.urls import path, include
from .views import main_view,home_view, list_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', main_view, name='post_list'),
    path('', home_view, name="home"),
    path("list/",list_view,name="list")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)