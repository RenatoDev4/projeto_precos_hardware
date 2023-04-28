from django.db.models import Q
from django.shortcuts import render

from .models import SearchPROCESSORS


def processadores(request):
    modelo = request.GET.get('select-modelo')
    loja = request.GET.get('select-loja')

    if modelo:
        # Use a cláusula Q para buscar pelos valores especificados na opção HTML # noqa
        valores = modelo.split(',')
        condicoes = Q()
        for valor in valores:
            condicoes |= Q(marca__icontains=valor)
        resultados = SearchPROCESSORS.objects.filter(
            condicoes).exclude(preco=0).exclude(valor_preco_prazo=0).order_by('preco')  # noqa
    else:
        resultados = SearchPROCESSORS.objects.exclude(preco=0).exclude(
            valor_preco_prazo=0).order_by('preco')[:19]

    if loja:
        resultados = resultados.filter(loja__icontains=loja)

    # Create a dictionary with the infomations selected by the user
    selecionados = {
        'modelo': modelo,
        'loja': loja,
    }

    return render(request, 'processadores/pages/index.html', {'resultados': resultados, 'selecionados': selecionados})  # noqa
