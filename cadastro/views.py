from django.shortcuts import render, get_object_or_404, redirect, reverse
from perfis.models import Users
from .forms import Inscrever_na_AtividadeForm, AtividadeForm, Usuario_ExternoForm, Lista_PrecencaForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required
from .models import Inscrever_na_Atividade, Atividade, Usuario_Externo
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt


# TODO Fazer Update e Delete dos usuarios Internos e Externo
@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def cadastro_externo(request):
    if request.method == 'GET':
        form = Usuario_ExternoForm()
        return render(request, 'cadastro_UserExterno.html', {'form': form})

    if request.method == 'POST':
        form = Usuario_ExternoForm(request.POST)

        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            usuario = Usuario_Externo.objects.filter(cpf=cpf)

            if usuario.exists():
                messages.add_message(request, messages.ERROR, 'Usuario ja existe!')
                return render(request, 'cadastro_UserExterno.html', {'form': form})

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Usuario Externo cadastrado com sucesso!')
            return redirect(reverse('cdE'))

        else:
            messages.add_message(request, messages.ERROR,
                                 'Erro ao cadastrar usuario externo. Verifique os dados e tente novamente.')
            return render(request, 'cadastro_UserExterno.html', {'form': form})


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
        form = AtividadeForm()
        return render(request, 'cadastro_atividade.html', {'form': form})

    elif request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.responsavel = form.cleaned_data['responsavel']
            atividade.save()

            messages.add_message(request, messages.SUCCESS, 'Atividade cadastrada com sucesso!')
            return redirect(reverse('cdA'))
        else:
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
        form = Inscrever_na_AtividadeForm()
        responsaveis = Users.objects.filter(is_superuser=False)
        return render(request, 'inscricao.html', {'form': form, 'responsaveis': responsaveis})

    elif request.method == 'POST':
        form = Inscrever_na_AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Inscrição realizada com sucesso!')
            return redirect(reverse('lista_inscricao'))
        else:
            messages.add_message(request, messages.ERROR, 'Erro ao realizar inscrição. Verifique os dados e tente novamente.')
            return render(request, 'inscricao.html', {'form': form})

@login_required(login_url='login')
@has_permission_decorator('lista_presenca')
def menu_atividade(request):
    atividades = Atividade.objects.filter(responsavel=request.user)
    return render(request, 'menu_atividade.html', {'atividades': atividades})


@login_required(login_url='login')
@has_permission_decorator('lista_de_atividade')
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
@has_permission_decorator('cadastro_interno')
def deletar_cliente(request, id):
    usuario = get_object_or_404(Usuario_Externo, pk=id)
    form = Usuario_ExternoForm(request.POST or None, instance=usuario)

    if request.method == 'POST':
        usuario.delete()
        messages.add_message(request, messages.SUCCESS, 'Deletado com Sucesso')
        return redirect(reverse('lista'))

    return render(request, 'delete/deletar_externo.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator('cadastro_interno')
def deletar_atividade(request, id):
    atividade = get_object_or_404(Atividade, pk=id)
    form = AtividadeForm(request.POST or None, instance=atividade)

    if request.method == 'POST':
        atividade.delete()
        messages.add_message(request, messages.SUCCESS, 'Atividade deletada com Sucesso')
        return redirect(reverse('lista_atividade'))

    return render(request, 'delete/deletar_atividade.html', {'form': form})


@has_permission_decorator('cadastro_interno')
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


# Ajax request---------------------------------------------------------------
@has_permission_decorator('cadastro_atividade')
def get_responsavel_data(request):
    responsavel_id = request.GET.get('responsavel_id')
    if responsavel_id:
        try:
            atividades_responsaveis = Atividade.objects.filter(responsavel_id=responsavel_id)

            atividades = [
                {
                    'id': atividade.id,
                    'nome_atividade': atividade.nome_atividade,
                    'hora_atividade': atividade.hora_atividade,
                    'dia_atividade': atividade.dia_atividade.dia_semana
                }
                for atividade in atividades_responsaveis
            ]

            data = {
                'atividades_do_responsavel': atividades,
                'email_do_responsavel': atividades_responsaveis[0].responsavel.email if atividades_responsaveis else ''
            }
            return JsonResponse(data)
        except Atividade.DoesNotExist:
            return JsonResponse({'error': 'Atividade não encontrada'}, status=404)
    return JsonResponse({'error': 'ID do responsável não fornecido'}, status=400)

