from django.shortcuts import render


def home(requests):
    return render(requests, 'home.html')

# Create your views here.
