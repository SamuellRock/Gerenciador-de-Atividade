from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import Inscrever_na_AtividadeForm, AtividadeForm, Usuario_ExternoForm, Lista_PrecencaForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required
from .models import Inscrever_na_Atividade, Atividade,Usuario_Externo
from django.contrib import messages


#TODO Fazer Update e Delete dos usuarios Internos e Externo


@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def cadastro_externo(request):
    if request.method == 'GET':
        form = Usuario_ExternoForm
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


'''SAMUEL ESTEVE AQUI  Atualizar usuario Externo'''
@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def lista_externa(request):
    usuarios = Usuario_Externo.objects.all()
    return render(request, 'lista_avante.html', {'usuarios': usuarios})



@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def update_usuario_externo(request, pk):
    usuario = get_object_or_404(Usuario_Externo, pk=pk)
    if request.method == 'POST':
        form = Usuario_ExternoForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Usuário Externo atualizado com sucesso!')
            return redirect(reverse('update_usuario_externo', args=[pk]))
    else:
        form = Usuario_ExternoForm(instance=usuario)
    return render(request, 'update/update_usuario_externo.html', {'form': form, 'usuario': usuario})
#ATÈ AQUI

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


'''SAMUEL ESTEVE AQUI atualizar atividade'''
@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def update_atividade(request, pk):
    atividade = get_object_or_404(Atividade, pk=pk)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Atividade atualizada com sucesso!')
            return redirect(reverse('update_atividade', args=[pk]))
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'update/update_atividade.html', {'form': form, 'atividade': atividade})
#ATÈ AQUI



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



