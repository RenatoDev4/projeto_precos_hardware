from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def duvidas(request):
    return render(request, 'duvidas/pages/index.html')


def enviar_email(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        # Send E-mail
        send_mail(
            assunto,
            f'Mensagem de {nome} ({email}):\n\n{mensagem}',
            email,  # Remetente
            ['renatodev4@gmail.com'],  # Destinatário(s)
            fail_silently=False,
        )

        # Redirect to confimation page
        return HttpResponseRedirect(reverse('confirmacao'))


def confirmacao(request):
    return render(request, 'duvidas/pages/confirmacao.html')
