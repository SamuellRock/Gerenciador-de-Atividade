from django.shortcuts import render, redirect,reverse, get_object_or_404
from .forms import UserFormTemplate


def cadastro_user(request):

    if request.method == 'GET':
        user_form = UserFormTemplate
        return render(request,'cadastro_user.html', {"form": user_form})

    elif request.method == 'POST':
        user_form = UserFormTemplate(request.POST or None)

        if user_form.is_valid():
            user_form.save()

        return render(request, 'cadastro_user.html', {"form": user_form})

