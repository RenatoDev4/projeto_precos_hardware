from django.urls import path

from placamae.views import placamae

from . import views

urlpatterns = [
    path('', placamae),
    path('search/', views.search_motherboards, name='search_motherboards'),
]
