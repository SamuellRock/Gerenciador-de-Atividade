from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import auth

from .forms import UserFormTemplate
from .models import Users



def cadastro_user(request):

    if request.method == 'GET':
        user_form = UserFormTemplate
        return render(request,'cadastro_user.html', {"form": user_form})

    elif request.method == 'POST':
        user_form = UserFormTemplate(request.POST or None)

        if user_form.is_valid():
            user_form.save()

        return render(request, 'cadastro_user.html', {"form": user_form})

def cadastro_usuario(request):
    if request.method == "GET":
        return render(request, 'cadastro_usuario.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        #pegando do user da model e verficando se o email é igual
        user = Users.objects.filter(email=email)

        if user.exists():
            return HttpResponse('Email existe')

        #caso o usuario não exista crie ele
        #o username é obrigatorio ou seja como nossa inscrição é pelo email coloquei o email no username
        user = Users.objects.create_user(username=email, email=email, password=senha, grupo_de_acesso='CI')

        return HttpResponse('Conta Criada')


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('cadastroUser'))
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=email, password=senha)
        
        if not user:
             return HttpResponse('Usuario invalido')
        
        auth.login(request, user)
        return HttpResponse('ENTROOOU, LOGOU, é para glorificar de pé igreja')

#linkar URL sair/ a um botão de logout
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))
    