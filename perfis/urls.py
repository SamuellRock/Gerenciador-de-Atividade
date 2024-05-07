from django.contrib import admin
from django.urls import path,include
from .views import cadastro_user


urlpatterns = [

    path('cadastro/', cadastro_user, name='cadastroUser'),

]