from django.db.models import Q
from django.shortcuts import render

from .models import SearchMemory


def memoria(request):
    modelo = request.GET.get('select-modelo')
    numero_de_pentes = request.GET.get('select-numero-de-pentes')
    desktop_ou_notebook = request.GET.get('select-desktop_ou_note')
    loja = request.GET.get('select-loja')

    resultados = SearchMemory.objects.exclude(preco=0).exclude(
        valor_preco_prazo=0)

    if modelo:
        # Use a cláusula Q para buscar pelos valores especificados na opção HTML # noqa
        valores = modelo.split(',')
        condicoes = Q()
        for valor in valores:
            condicoes |= Q(marca__icontains=valor)
        resultados = resultados.filter(condicoes)  # noqa

    if loja:
        resultados = resultados.filter(loja__icontains=loja)

    resultados = resultados.order_by('preco')[:19]

    # Create a dictionary with the infomations selected by the user
    selecionados = {
        'modelo': modelo,
        'numero_de_pentes': numero_de_pentes,
        'desktop_ou_notebook': desktop_ou_notebook,
        'loja': loja,
    }

    return render(request, 'memoria/pages/index.html', {'resultados': resultados, 'selecionados': selecionados})  # noqa


def search(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = SearchMemory.objects.filter(marca__icontains=query).exclude(
            preco=0).exclude(valor_preco_prazo=0)[:30]

    return render(request, 'memoria/pages/search_results.html', {'results': results})
