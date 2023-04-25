from django.shortcuts import render


def memoria(request):
    return render(request, 'memoria/pages/index.html')
