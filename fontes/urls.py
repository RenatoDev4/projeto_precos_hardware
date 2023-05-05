from django.urls import path

from fontes.views import fontes

urlpatterns = [
    path('', fontes),

]
