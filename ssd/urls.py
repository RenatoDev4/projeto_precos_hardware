from django.urls import path

from ssd.views import ssd

urlpatterns = [
    path('', ssd),

]
