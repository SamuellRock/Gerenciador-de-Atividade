from django.shortcuts import render, redirect,reverse, get_object_or_404,HttpResponse
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


