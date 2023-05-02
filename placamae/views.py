from django.db.models import Q
from django.shortcuts import render

from .models import SearchMOTHERBOARDS


def placamae(request):
    modelo = request.GET.get('select-modelo')
    chipset = request.GET.get('select-chipset')
    loja = request.GET.get('select-loja')

    resultados = SearchMOTHERBOARDS.objects.exclude(
        preco=0).exclude(valor_preco_prazo=0)

    if modelo:
        valores = modelo.split(',')
        condicoes = Q()
        for valor in valores:
            condicoes |= Q(marca__icontains=valor)
        resultados = resultados.filter(condicoes)

    if chipset:
        resultados = resultados.filter(marca__icontains=chipset)

    if loja:
        resultados = resultados.filter(loja__icontains=loja)

    resultados = resultados.order_by('preco')[:19]

    selecionados = {
        'modelo': modelo,
        'chipset': chipset,
        'loja': loja,
    }

    return render(request, 'placamae/pages/index.html', {'resultados': resultados, 'selecionados': selecionados})


def search_motherboards(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = SearchMOTHERBOARDS.objects.filter(marca__icontains=query).exclude(
            preco=0).exclude(valor_preco_prazo=0)
    return render(request, 'placamae/pages/search_results.html', {'results': results})
