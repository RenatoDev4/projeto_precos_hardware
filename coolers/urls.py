from django.urls import path

from coolers.views import coolers

urlpatterns = [
    path('', coolers),

]
