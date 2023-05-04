from django.urls import path

from .views import confirmacao, duvidas, enviar_email

urlpatterns = [
    path('', duvidas),
    path('enviar_email/', enviar_email, name='enviar_email'),
    path('confirmacao/', confirmacao, name='confirmacao'),

]
