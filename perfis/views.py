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


@has_permission_decorator('cadastro_interno')
def cadastro_usuario(request):
    if request.method == "GET":
        grupoForm = UserFormTemplate

        return render(request, 'cadastro_usuario.html', {"grupoForm": grupoForm})

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        grupo = request.POST.get('grupo_de_acesso')

        print(grupo)

        #pegando do user da model e verficando se o email é igual
        user = Users.objects.filter(email=email)


        if user.exists():
            return HttpResponse('Email existe')

        #caso o usuario não exista crie ele
        #o username é obrigatorio ou seja como nossa inscrição é pelo email coloquei o email no username
        user = Users.objects.create_user(username=email, email=email, password=senha, grupo_de_acesso=grupo,
                                         first_name=nome, last_name=sobrenome)
        user.save()
        return HttpResponse('Conta Criada')


def login(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            #Se o usuario estiver autenticado nao precisa careegar o template login
            return redirect(reverse('cadastro_usuario'))
        return render(request, 'login.html')

    elif request.method == 'POST':
        if request.user.is_authenticated:

            return redirect(reverse('cadastro_usuario'))

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        #passando os parametros para o user para ver se ele existe no banco
        user = auth.authenticate(username=email, password=senha)

        #Se o usuario for invalido ou seja nao achae ele no banco
        if not user:
            return HttpResponse('Usuario Invalido')#TODO coloar mensagem de erro

        print(user.last_login)
        if user.last_login is None:
            auth.login(request, user)
            form = PasswordChangeFormTemplate(request.user)
            return render(request,'primeiro_login.html', {'form': form})

        #SE existe
        auth.login(request, user)
        return redirect(reverse('cadastro_usuario'))

@login_required()
def alterar_senha(request):

    if request.method == 'GET':
        form = PasswordChangeFormTemplate(request.user)
        return render(request, 'primeiro_login.html', {'form': form})

    elif request.method == 'POST':
        form = PasswordChangeFormTemplate(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect(reverse('cadastro_usuario'))

        else:
            return HttpResponse("primeiro_login.html")#TODO coloar mensagem de erro
    else:
        form = PasswordChangeFormTemplate(request.user)
        # Se o formulário não for válido, renderize o formulário novamente com os erros
        return render(request, 'primeiro_login.html', {'form': form})


#TODO linkar URL sair/ a um botão de logout
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))





