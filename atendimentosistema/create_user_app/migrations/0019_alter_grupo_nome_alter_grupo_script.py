# Generated by Django 5.0.1 on 2024-08-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_user_app', '0018_alter_grupo_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='script',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
    ]
