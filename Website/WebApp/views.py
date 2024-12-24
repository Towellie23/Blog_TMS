from django.shortcuts import render


def index(request):
    return render(request, 'WebApp/index.html')

def about(request):
    return render(request, 'WebApp/about.html')