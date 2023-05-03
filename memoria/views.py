from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import SearchMemory


def memoria(request):
    modelo = request.GET.get('select-modelo')
    loja = request.GET.get('select-loja')

    resultados = SearchMemory.objects.exclude(preco=0).exclude(
        valor_preco_prazo=0)
    resultados = resultados.order_by('preco')

    if modelo:
        # Use a cláusula Q para buscar pelos valores especificados na opção HTML # noqa
        valores = modelo.split(',')
        condicoes = Q()
        for valor in valores:
            condicoes |= Q(marca__icontains=valor)
        resultados = resultados.filter(condicoes)  # noqa

    if loja:
        resultados = resultados.filter(loja__icontains=loja)

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

    contexto = {
        'resultados': resultados_pagina,
        'selecionados': {
            'modelo': modelo,
            'loja': loja,

        },
        'paginator': paginator,
        'pags_visiveis': pags_visiveis,
        'pag_atual': pag_atual
    }

    return render(request, 'memoria/pages/index.html', contexto)


def search(request):
    query = request.GET.get('q')
    results = SearchMemory.objects.all()

    if query:
        results = results.filter(marca__icontains=query).order_by('preco')

    results = results.exclude(preco=0).exclude(valor_preco_prazo=0)

    resultados_por_pagina = 16
    paginator = Paginator(results, resultados_por_pagina)

    page = request.GET.get('page')

    try:
        resultados_pagina = paginator.page(page)
    except PageNotAnInteger:
        resultados_pagina = paginator.page(1)
    except EmptyPage:
        resultados_pagina = paginator.page(paginator.num_pages)

    num_pags = paginator.num_pages
    pag_atual = resultados_pagina.number
    pags_visiveis = []
    for i in range(1, num_pags+1):
        if i == 1 or i == num_pags or i == pag_atual or i == pag_atual-1 or i == pag_atual+1:  # noqa
            pags_visiveis.append(i)
        elif i == pag_atual-2 or i == pag_atual+2:
            pags_visiveis.append('...')

    contexto = {
        'results': resultados_pagina,
        'paginator': paginator,
        'pags_visiveis': pags_visiveis,
        'pag_atual': pag_atual,
        'query': query,  # Certifique-se de que a variável query está presente no contexto # noqa
    }

    return render(request, 'memoria/pages/search_results.html', contexto)
