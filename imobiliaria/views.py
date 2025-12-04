from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def form(request):
    return render(request, 'pages/form.html')
