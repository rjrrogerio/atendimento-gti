# Generated by Django 4.2.2 on 2023-08-16 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_user_app', '0004_alter_unidade_nomeuo_alter_unidade_numerouo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unidade',
            old_name='nomeUOAD',
            new_name='nomeUOnoAD',
        ),
    ]
