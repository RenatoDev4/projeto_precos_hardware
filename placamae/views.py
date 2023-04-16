from django.shortcuts import render


def placamae(request):
    return render(request, 'index.html')
