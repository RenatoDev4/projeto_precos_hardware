from django.shortcuts import render


def placamae(request):
    return render(request, 'placamae/pages/index.html')
