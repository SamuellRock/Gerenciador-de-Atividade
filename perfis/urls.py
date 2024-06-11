from django.urls import path
from .views import cadastro_usuario, perfil_user
from .views import login, logout, alterar_senha, update_usuario
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('perfil/', perfil_user, name='perfil_user'),

    path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('login/', login, name='login'),
    path('', login, name='login'),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('update_usuario/<int:pk>/', update_usuario, name='update_usuario'),

    #Senhas
    path('senha_esquecida/', auth_views.PasswordResetView.as_view(template_name="registration/email_confirmacao.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/email_confirmacao_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/nova_senha.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/senha_confirmada.html"), name='password_reset_complete'),
    path('sair/', logout, name='sair'),
]