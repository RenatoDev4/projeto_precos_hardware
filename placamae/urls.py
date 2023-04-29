from django.urls import path

from placamae.views import placamae

urlpatterns = [
    path('', placamae),


]
