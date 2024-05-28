from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import auth
from .forms import UserFormTemplate
from .models import Users
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordChangeFormTemplate
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator
from django.core.mail import send_mail
from gerenciador.gerardor import gerar_senha
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt



@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_interno')
def cadastro_usuario(request):
    if request.method == "GET":
        grupoForm = UserFormTemplate

        return render(request, 'cadastro_interno.html', {"grupoForm": grupoForm})

    elif request.method == 'POST':
        email = request.POST.get('email')

        form = UserFormTemplate(request.POST)

        #Gerado de senha automatico
        senha = gerar_senha()
        print(senha)

        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        grupo = request.POST.get('grupo_de_acesso')

        #pegando do user da model e verficando se o email é igual
        user = Users.objects.filter(email=email)

        if user.exists():
            messages.add_message(request, messages.ERROR, 'Email ja existe!')
            return render(request, 'cadastro_interno.html', {"grupoForm": form, 'nome': nome, 'sobrenome':sobrenome})


        #caso o usuario não exista crie ele
        #o username é obrigatorio ou seja como nossa inscrição é pelo email coloquei o email no username
        user = Users.objects.create_user(username=email, email=email, password=senha, grupo_de_acesso=grupo,
                                         first_name=nome, last_name=sobrenome)
        user.save()
        send_mail(f'Senha do Cadastro Avante', f'Sua conta no sistema avante foi cadastrada com sucesso!.\nSua senha é: {senha} \nentre e mude a sua senha para uma personalizada', 'pedro@programador.com.br',[f'{email}'])
        messages.add_message(request, messages.SUCCESS, 'Usuario Cadastrado com sucesso!')
        return redirect(reverse('cadastro_usuario'))

    else:
        messages.add_message(request, messages.ERROR, 'Erro inesperado, tente novamente!')
        return redirect(reverse('cadastro_usuario'))


'''SAMUEL ESTEVE AQUI atualizar Users'''
@login_required(login_url='login')
@has_permission_decorator('cadastro_interno')
def update_usuario(request, pk):
    user = get_object_or_404(Users, pk=pk)
    if request.method == 'POST':
        form = UserFormTemplate(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Usuário atualizado com sucesso!')
            return redirect(reverse('update_usuario', args=[pk]))
    else:
        form = UserFormTemplate(instance=user)
    return render(request, 'update/update_usuario.html', {'form': form, 'user': user})
#ATÈ AQUI


def login(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return render(request, 'login.html')

    elif request.method == 'POST':
        if request.user.is_authenticated:
            return redirect(reverse('home'))

        email = request.POST.get('email')
        senha = request.POST.get('senha')
        #gerador de senha automatico user


        #passando os parametros para o user para ver se ele existe no banco
        user = auth.authenticate(username=email, password=senha)

        #Se o usuario for invalido ou seja nao achar ele no banco
        if not user:
            messages.add_message(request, messages.ERROR, 'Usuario invalido ou senha incorreta!')
            return redirect(reverse('login'))

        print(user.last_login)
        if user.last_login is None:
            auth.login(request, user)
            form = PasswordChangeFormTemplate(request.user)
            return render(request,'primeiro_login.html', {'form': form})

        #SE existe
        auth.login(request, user)
        return redirect(reverse('home'))


@login_required(login_url='login')
def alterar_senha(request):

    if request.method == 'GET':
        form = PasswordChangeFormTemplate(request.user)
        return render(request, 'primeiro_login.html', {'form': form})

    elif request.method == 'POST':
        form = PasswordChangeFormTemplate(user=request.user,data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect(reverse('home'))

        if not form.is_valid():
            messages.add_message(request, messages.ERROR, 'Senha invalida!')
            messages.add_message(request, messages.ERROR, 'Coloque uma senha mais elaborada com numeros, letras maiuscula e minusculas!')
            return redirect(reverse('alterar_senha'))
    else:
        form = PasswordChangeFormTemplate(request.user)
        messages.add_message(request, messages.ERROR, 'Senha invalida!')
        return render(request, 'primeiro_login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))





