from django.urls import path

from placasdevideo.views import placasdevideo

urlpatterns = [
    path('', placasdevideo),

]
