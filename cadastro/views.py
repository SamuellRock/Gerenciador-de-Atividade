from django.shortcuts import render, get_object_or_404
from .forms import Inscrever_na_AtividadeForm, AtividadeForm, Usuario_ExternoForm,Lista_PrecencaForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required
from .models import Inscrever_na_Atividade, Atividade


@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def cadastro_externo(request):
    if request.method == 'GET':
        form = Usuario_ExternoForm
        return render(request, 'cadastro_benificiario.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator('cadastro_atividade')
def cadastro_atividade(request):
    if request.method == 'GET':
        form = AtividadeForm
        return render(request, 'cadastro_atividade.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator('cadastro_inscricao')
def inscricao(request):
    if request.method == 'GET':
        form = Inscrever_na_AtividadeForm
        return render(request, 'inscricao.html', {'form': form})


@login_required(login_url='login')
#TODO rolepermissions
def menu_atividade(request):
    atividades = Atividade.objects.filter(responsavel=request.user)
    return render(request, 'menu_atividade.html', {'atividades': atividades})


@login_required(login_url='login')
#TODO rolepermissions
def lista_presenca(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id, responsavel=request.user)
    alunos = Inscrever_na_Atividade.objects.filter(atividade=atividade)
    form = Lista_PrecencaForm()
    return render(request, 'precenca.html', {'form': form, 'alunos': alunos})


