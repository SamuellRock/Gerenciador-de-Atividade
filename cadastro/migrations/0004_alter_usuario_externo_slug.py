# Generated by Django 5.0.4 on 2024-05-29 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_usuario_externo_slug_alter_usuario_externo_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_externo',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, null=True, unique=True),
        ),
    ]
