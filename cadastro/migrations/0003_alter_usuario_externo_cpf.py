# Generated by Django 5.0.4 on 2024-06-05 23:46

import cadastro.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_alter_servico_dia_atividade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_externo',
            name='cpf',
            field=models.CharField(max_length=14, validators=[cadastro.validator.validate_cpf], verbose_name='CPF'),
        ),
    ]