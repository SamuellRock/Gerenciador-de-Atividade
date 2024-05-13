# Generated by Django 5.0.4 on 2024-05-08 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_alter_users_grupo_de_acesso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='grupo_de_acesso',
            field=models.CharField(choices=[('ADM', 'Administrador'), ('CE', 'Cadastro Externo'), ('CA', 'Cadastro Atividade'), ('CI', 'Cadastro Inscrição'), ('LP', 'Listagem de Pessoas')], max_length=3),
        ),
    ]