from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import Inscrever_na_AtividadeForm, AtividadeForm, Usuario_ExternoForm, Lista_PrecencaForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required
from .models import Inscrever_na_Atividade, Atividade, Usuario_Externo
from django.contrib import messages


# TODO Fazer Update e Delete dos usuarios Internos e Externo


@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def cadastro_externo(request):
    if request.method == 'GET':
        form = Usuario_ExternoForm()
        return render(request, 'cadastro_benificiario.html', {'form': form})

    if request.method == 'POST':
        form = Usuario_ExternoForm(request.POST)

        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            usuario = Usuario_Externo.objects.filter(cpf=cpf)

            if usuario.exists():
                messages.add_message(request, messages.ERROR, 'Usuario ja existe!')
                return render(request, 'cadastro_benificiario.html', {'form': form})

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Usuario Externo cadastrado com sucesso!')
            return redirect(reverse('cdE'))

        else:
            messages.add_message(request, messages.ERROR,
                                 'Erro ao cadastrar usuario externo. Verifique os dados e tente novamente.')
            return render(request, 'cadastro_benificiario.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator('cadastro_atividade')
def cadastro_atividade(request):
    if request.method == 'GET':
        form = AtividadeForm
        return render(request, 'cadastro_atividade.html', {'form': form})

    elif request.method == "POST":
        form = AtividadeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Atividade cadastrada com sucesso!')
            return redirect(reverse('cdA'))

        elif not form.is_valid():
            messages.add_message(request, messages.ERROR, 'Ocorreu algum erro ao cadastrar')
            return render(request, 'cadastro_atividade.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator('cadastro_inscricao')
def inscricao(request):
    if request.method == 'GET':
        form = Inscrever_na_AtividadeForm
        return render(request, 'inscricao.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator('lista_presenca')
def menu_atividade(request):
    atividades = Atividade.objects.filter(responsavel=request.user)
    return render(request, 'menu_atividade.html', {'atividades': atividades})


@login_required(login_url='login')
@has_permission_decorator('lista_presenca')
def lista_presenca(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id, responsavel=request.user)
    alunos = Inscrever_na_Atividade.objects.filter(atividade=atividade)
    form = Lista_PrecencaForm()
    return render(request, 'precenca.html', {'form': form, 'alunos': alunos})


# lista---------------------------------------------------------------
@login_required(login_url='login')
def lista_usuario(request):
    usuario = Usuario_Externo.objects.all()
    return render(request, 'lista/lista_usuario.html', {'usuarios': usuario})


@login_required(login_url='login')
def lista_atividade(request):
    atividade = Atividade.objects.all()
    return render(request, 'lista/lista_atividade.html', {'atividades': atividade})


@login_required(login_url='login')
def lista_inscricao(request):
    inscrito = Inscrever_na_Atividade.objects.all()
    return render(request, 'lista/lista_inscricao.html', {'inscrito': inscrito})


# ---------------------------------------------------------------------


# Delete---------------------------------------------------------------
@login_required(login_url='login')
def deletar_cliente(request, id):
    usuario = get_object_or_404(Usuario_Externo, pk=id)
    form = Usuario_ExternoForm(request.POST or None, instance=usuario)

    if request.method == 'POST':
        usuario.delete()
        messages.add_message(request, messages.SUCCESS, 'Deletado com Sucesso')
        return redirect(reverse('lista'))

    return render(request, 'delete/deletar_externo.html', {'form': form})


@login_required(login_url='login')
def deletar_atividade(request, id):
    atividade = get_object_or_404(Atividade, pk=id)
    form = AtividadeForm(request.POST or None, instance=atividade)

    if request.method == 'POST':
        atividade.delete()
        messages.add_message(request, messages.SUCCESS, 'Atividade deletada com Sucesso')
        return redirect(reverse('lista_atividade'))

    return render(request, 'delete/deletar_atividade.html', {'form': form})


@login_required(login_url='login')
def deletar_inscricao(request, id):
    inscricao = get_object_or_404(Inscrever_na_Atividade, pk=id)
    form = Inscrever_na_AtividadeForm(request.POST or None, instance=inscricao)
    if request.method == 'POST':
        inscricao.delete()
        messages.add_message(request, messages.SUCCESS, 'Inscricao deletada com Sucesso')
        return redirect(reverse('deletar_inscricao'))

    return render(request, 'delete/deletar_inscricao.html', {'form': form})

# ---------------------------------------------------------------------
