from django.shortcuts import render
from django.http import HttpResponse
from .forms import Inscrever_na_AtividadeForm, AtividadeForm, Usuario_ExternoForm


def cadastro_externo(request):
    if request.method == 'GET':
        form = Usuario_ExternoForm
        return render(request, 'cadastro_benificiario.html', {'form': form})


def cadastro_atividade(request):
    if request.method == 'GET':
        form = AtividadeForm
        return render(request, 'cadastro_atividade.html', {'form': form})


def inscricao(request):
    if request.method == 'GET':
        form = Inscrever_na_AtividadeForm
        return render(request, 'inscricao.html', {'form': form})
