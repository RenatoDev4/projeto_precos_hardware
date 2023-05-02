from django.urls import path

from memoria.views import memoria

from . import views

urlpatterns = [
    path('', memoria),
    path('search/', views.search, name='search'),

]
