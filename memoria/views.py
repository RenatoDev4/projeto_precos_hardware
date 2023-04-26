from django.db.models import Q
from django.shortcuts import render

from .models import SearchMemory


def memoria(request):
    modelo = request.GET.get('select-modelo')
    numero_de_pentes = request.GET.get('select-numero-de-pentes')
    desktop_ou_notebook = request.GET.get('select-desktop_ou_note')
    loja = request.GET.get('select-loja')

    if modelo:
        # Use a cláusula Q para buscar pelos valores especificados na opção HTML # noqa
        valores = modelo.split(',')
        condicoes = Q()
        for valor in valores:
            condicoes |= Q(marca__icontains=valor)
        resultados = SearchMemory.objects.filter(
            condicoes).exclude(preco=0).exclude(valor_preco_prazo=0).order_by('preco')  # noqa
    else:
        resultados = SearchMemory.objects.exclude(preco=0).exclude(
            valor_preco_prazo=0).order_by('preco')[:19]

    if numero_de_pentes:
        resultados = resultados.filter(marca__icontains=numero_de_pentes)

    if desktop_ou_notebook == 'Para Desktop':
        resultados = resultados.filter(~Q(marca__icontains='para Notebook'))
    elif desktop_ou_notebook == 'Para Notebook':
        resultados = resultados.filter(Q(marca__icontains='para Notebook'))

    if loja:
        resultados = resultados.filter(loja__icontains=loja)

    # Create a dictionary with the infomations selected by the user
    selecionados = {
        'modelo': modelo,
        'numero_de_pentes': numero_de_pentes,
        'desktop_ou_notebook': desktop_ou_notebook,
        'loja': loja,
    }

    if not resultados:
        return render(request, 'memoria/pages/empty.html', {'selecionados': selecionados})

    return render(request, 'memoria/pages/index.html', {'resultados': resultados, 'selecionados': selecionados})
