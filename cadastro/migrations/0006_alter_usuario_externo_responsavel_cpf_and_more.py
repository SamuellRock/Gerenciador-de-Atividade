# Generated by Django 5.0.4 on 2024-06-11 22:48

import cadastro.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_alter_inscrever_servico_dia_servico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_externo',
            name='responsavel_cpf',
            field=models.CharField(blank=True, default='Vazio', max_length=14, null=True, validators=[cadastro.validator.validate_cpf]),
        ),
        migrations.AlterField(
            model_name='usuario_externo',
            name='responsavel_nome',
            field=models.CharField(blank=True, default='Vazio', max_length=50, null=True, validators=[cadastro.validator.validate_nome]),
        ),
    ]
