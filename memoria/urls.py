from django.urls import path

from memoria.views import memoria

urlpatterns = [
    path('', memoria)

]
