from django.urls import path

from processadores.views import processadores

urlpatterns = [
    path('', processadores)

]
