from django.shortcuts import render

from .models import SearchVGA


def placasdevideo(request):
    modelo = request.GET.get('select-modelo')
    if modelo:
        resultados = SearchVGA.objects.filter(
            marca__icontains=modelo).exclude(preco=0).order_by('preco')
    else:
        resultados = SearchVGA.objects.exclude(preco=0).order_by('preco')
    return render(request, 'placasdevideo/pages/index.html', {'resultados': resultados})  # noqa
