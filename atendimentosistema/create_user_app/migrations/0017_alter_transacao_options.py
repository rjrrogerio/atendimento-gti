# Generated by Django 5.0.1 on 2024-08-06 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_user_app', '0016_alter_grupo_data_alter_grupo_nome_alter_grupo_script'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Transacoes'},
        ),
    ]