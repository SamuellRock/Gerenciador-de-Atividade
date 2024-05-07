from django.http import HttpResponse
from django.shortcuts import render


def teste(request):
    return HttpResponse("Estou aqui")