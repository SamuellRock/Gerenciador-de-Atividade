# Generated by Django 5.0.4 on 2024-05-29 22:01

import cadastro.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_externo',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario_externo',
            name='nome',
            field=models.CharField(max_length=50, unique=True, validators=[cadastro.validator.validate_nome]),
        ),
    ]
