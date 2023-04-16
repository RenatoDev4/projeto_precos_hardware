from django.shortcuts import render


def processadores(request):
    return render(request, 'processadores/pages/index.html')
