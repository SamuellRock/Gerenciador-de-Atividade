from django.shortcuts import render, get_object_or_404, redirect, reverse
from perfis.models import Users
#from django.contrib.auth.models import User
from .forms import Inscrever_AulaForm, AtividadeForm, Usuario_ExternoForm, ServicoAtividadeForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required
from .models import Inscrever_Aula, Atividade, Usuario_Externo, Servico, DiaAtividade
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError



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


@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_atividade')
def cadastro_atividade(request):
    if request.method == 'GET':
        form = AtividadeForm()
        return render(request, 'cadastro_atividade_aula/cadastro_atividade_aula.html', {'form': form})

    elif request.method == 'POST':
        form = AtividadeForm(request.POST)

        if form.is_valid():
            atividade = form.save(commit=False)
            form.save_m2m()
            atividade.save()
            messages.add_message(request, messages.SUCCESS, 'Atividade cadastrada com sucesso!')
            return redirect(reverse('cdA'))
        else:
            messages.add_message(request, messages.ERROR, 'Ocorreu algum erro ao cadastrar')
            return render(request, 'cadastro_atividade_aula/cadastro_atividade_aula.html', {'form': form})


def inscricao_aula(request):
    if request.method == 'GET':
        form = Inscrever_AulaForm()
        return render(request, 'inscricao_aula/inscricao_aula.html', {'form': form})
    elif request.method == 'POST':
        form = Inscrever_AulaForm(request.POST)
        if form.is_valid():
            print(request.POST)
            aluno = form.cleaned_data['nome_aluno']
            ativida_nome = form.cleaned_data['nome_atividade']
            horario = form.cleaned_data['horario_aula']
            responsavel = form.cleaned_data['responsavel']

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Inscrição cadastrada com sucesso!')
            return redirect(reverse('inscricao_aula'))
        else:
            messages.add_message(request, messages.ERROR, 'Ocorreu algum erro ao cadastrar')
            return render(request, 'inscricao_aula/inscricao_aula.html', {'form': form})


def get_horarios(request, atividade_id):
    atividade = Atividade.objects.get(id=atividade_id)
    horario = atividade.hora_atividade  # Diretamente o campo de hora
    horarios_data = [{'hora': horario.strftime('%H:%M')}]
    return JsonResponse({'horarios': horarios_data})


def get_responsaveis(request, atividade_id, horario):
    # Filtra a atividade com base no ID e no horário
    atividade = get_object_or_404(Atividade, id=atividade_id, hora_atividade=horario)

    # Obtém o responsável pela atividade
    responsavel = atividade.responsavel

    # Cria a resposta JSON com as informações do responsável
    data = {
        'id': responsavel.id,
        'username': responsavel.username,
        'email': responsavel.email,
        'first_name': responsavel.first_name,
        'last_name': responsavel.last_name,
    }

    return JsonResponse(data)
@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_atividade')
def cadastro_servico(request):
    if request.method == 'GET':
        form = ServicoAtividadeForm()
        return render(request, 'cadastro_atividade_servicos/cadastro_atividade_servicos.html', {'form': form})

    elif request.method == 'POST':
        form = ServicoAtividadeForm(request.POST)
        if form.is_valid():

            dia_atividade = form.cleaned_data['dia_atividade']
            responsavel = form.cleaned_data['responsavel']
            if Servico.objects.filter(dia_atividade=dia_atividade, responsavel=responsavel).exists():
                messages.add_message(request, messages.ERROR, 'Já existe um serviço cadastrado para esse responsável nesse dia')
                return render(request, 'cadastro_atividade_servicos/cadastro_atividade_servicos.html', {'form': form})

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Atividade cadastrada com sucesso!')
            return redirect(reverse('cdS'))
        else:
            messages.add_message(request, messages.ERROR, 'Ocorreu algum erro ao cadastrar')
            return render(request, 'cadastro_atividade_servicos/cadastro_atividade_servicos.html', {'form': form})


# UPDATE---------------------------------------------------------------
@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def update_aula(request, id):
    atividade = get_object_or_404(Atividade, pk=id)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        print(form)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Atividade atualizada com sucesso!')
            return redirect(reverse('update_aula', args=[id]))
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'update/update_aula.html', {'form': form, 'atividade': atividade})


@xframe_options_exempt
@login_required(login_url='login')
def update_servico(request,id):
    servico = get_object_or_404(Servico, pk=id)
    if request.method == 'POST':
        form = ServicoAtividadeForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect(reverse(update_servico, args=[id]))
    else:
        form = ServicoAtividadeForm(instance=servico)

    return render(request, 'update/update_servico.html', {'form': form, 'servico': servico})

# ---------------------------------------------------------------------

# Vizualizar---------------------------------------------------------------


@xframe_options_exempt
@login_required(login_url='login')
def vizualizar_aula(request, id):
    vizualizar = get_object_or_404(Atividade, id=id)
    return render(request, 'vizualizar_aula/vizualizar_aula.html', {'vizualizar': vizualizar})


@xframe_options_exempt
@login_required(login_url='login')
def vizualizar_servico(request, id):
    vizualizar = get_object_or_404(Servico, id=id)
    return render(request, 'vizualizar_servico/vizualizar_servico.html', {'vizualizar': vizualizar})

# ---------------------------------------------------------------------

# lista---------------------------------------------------------------


@cache_page(60)
@login_required(login_url='login')
def lista_usuario_interno(request):
    internoList = Usuario_Externo.objects.all()
    return render(request, 'lista/listagemUsuariosInternos.html', {'internoList': internoList})


@cache_page(60)
@login_required(login_url='login')
def lista_usuario_externo(request):
    externoList = Usuario_Externo.objects.all()
    return render(request, 'lista/listagemUsuariosExternos.html', {'externoList': externoList})


@xframe_options_exempt
@login_required(login_url='login')
def lista_aula(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        aulaList = Atividade.objects.all()
        aulaList = aulaList.filter(nome_atividade__icontains=pesquisa)


    else:
        aulaList = Atividade.objects.all()
        return render(request, 'lista/listagemAulas.html', {'aulaList': aulaList})

    return render(request, 'lista/listagemAulas.html', {'aulaList': aulaList})


@xframe_options_exempt
@login_required(login_url='login')
def lista_servico(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:

        servicoList = Servico.objects.all()
        servicoList = servicoList.filter(nome_servico__icontains=pesquisa)

    else:
        servicoList = Servico.objects.all()

    return render(request, 'lista/listagemServicos.html', {'servicoList': servicoList})

# ---------------------------------------------------------------------


# Delete---------------------------------------------------------------

@login_required(login_url='login')
@has_permission_decorator('cadastro_interno')
def deletar_cliente(request, slug):
    usuario = get_object_or_404(Usuario_Externo, slug=slug)
    form = Usuario_ExternoForm(request.POST or None, instance=usuario)

    if request.method == 'POST':
        usuario.delete()
        messages.add_message(request, messages.SUCCESS, 'Deletado com Sucesso')
        return redirect(reverse('lista'))

    return render(request, 'delete/deletar_externo.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator('cadastro_interno')
@require_POST
def deletar_aula(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    atividade.delete()
    return JsonResponse({'message': 'Aula deletada com sucesso!'})


@login_required(login_url='login')
@has_permission_decorator('cadastro_interno')
@require_POST
def deletar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    servico.delete()
    return JsonResponse({'message': 'Serviço deletado com sucesso!'})


# ---------------------------------------------------------------------

