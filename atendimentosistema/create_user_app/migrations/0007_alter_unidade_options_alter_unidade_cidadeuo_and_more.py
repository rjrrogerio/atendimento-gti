# Generated by Django 4.2.2 on 2023-08-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_user_app', '0006_unidade_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unidade',
            options={'ordering': ['nomeUo']},
        ),
        migrations.AlterField(
            model_name='unidade',
            name='cidadeUo',
            field=models.CharField(blank=True, default='capital', max_length=500),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='nomeUOnoAD',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='nomeUo',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='numeroUo',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]