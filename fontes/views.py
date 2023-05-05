from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import SearchPOWERSUPLY


def fontes(request):
    modelo = request.GET.get('select-modelo')
    loja = request.GET.get('select-loja')

    if modelo:
        valores = modelo.split(',')
        condicoes = Q()
        for valor in valores:
            condicoes |= Q(marca__icontains=valor)
        resultados = SearchPOWERSUPLY.objects.filter(
            condicoes).exclude(preco=0).exclude(valor_preco_prazo=0).order_by('preco')  # noqa
    else:
        resultados = SearchPOWERSUPLY.objects.exclude(preco=0).exclude(
            valor_preco_prazo=0).order_by('preco')

    if loja:
        resultados = resultados.filter(loja__icontains=loja)

    exclusoes_geral = ['Chaveada', '0.5A', '1A', '2A', '3A',
                       '4A', '5A', '10A', 'Almofada',
                       'Indicador', 'Compression', 'Radiador',
                       'Pasta Térmica de Silicone', 'Conexao Barrow',
                       'Suporte Para Reservatorio', 'Tubo de PETG',
                       'Tubo de Acrilico', 'Fita Led', 'Fitting Tampa',
                       'Barra de LED', 'Fita de Led']

    for exclusao in exclusoes_geral:
        resultados = resultados.exclude(marca__icontains=exclusao)

    # Setting the number of results per page
    resultados_por_pagina = 16

    # Creating the Paginator object
    paginator = Paginator(resultados, resultados_por_pagina)

    # Getting the page number to be displayed from the GET parameter
    page = request.GET.get('page')

    try:
        # Getting the results from the specified page
        resultados_pagina = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, return the first page
        resultados_pagina = paginator.page(1)
    except EmptyPage:
        # If the requested page is outside the page range, return the last page # noqa
        resultados_pagina = paginator.page(paginator.num_pages)

    # Defining the list of pages to display in pagination
    num_pags = paginator.num_pages
    pag_atual = resultados_pagina.number
    pags_visiveis = []
    for i in range(1, num_pags+1):
        if i == 1 or i == num_pags or i == pag_atual or i == pag_atual-1 or i == pag_atual+1:  # noqa
            pags_visiveis.append(i)
        elif i == pag_atual-2 or i == pag_atual+2:
            pags_visiveis.append('...')

    # Creating the context to render the template
    contexto = {
        'resultados': resultados_pagina,
        'selecionados': {
            'modelo': modelo,
            'loja': loja
        },
        'paginator': paginator,
        'pags_visiveis': pags_visiveis,
        'pag_atual': pag_atual
    }

    return render(request, 'fontes/pages/index.html', contexto)