# Generated by Django 4.2.2 on 2023-08-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_user_app', '0008_alter_unidade_cidadeuo_alter_unidade_nomeuonoad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidade',
            name='cidadeUo',
            field=models.CharField(default='São Paulo', max_length=500),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='nomeUo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='numeroUo',
            field=models.CharField(max_length=10),
        ),
    ]
