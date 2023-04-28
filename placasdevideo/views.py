from django.shortcuts import render

from .models import SearchVGA


def placasdevideo(request):
    modelo = request.GET.get('select-modelo')
    loja = request.GET.get('select-loja')
    if modelo:
        resultados = SearchVGA.objects.filter(
            marca__icontains=modelo).exclude(preco=0).exclude(valor_preco_prazo=0).order_by('preco')  # noqa
    else:
        resultados = SearchVGA.objects.exclude(preco=0).exclude(
            valor_preco_prazo=0).order_by('preco')[:19]
    if loja:
        resultados = resultados.filter(loja__icontains=loja)

    selecionados = {
        'modelo': modelo,
        'loja': loja,
    }

    return render(request, 'placasdevideo/pages/index.html', {'resultados': resultados, 'selecionados': selecionados})  # noqa
