# Generated by Django 5.0.1 on 2024-08-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_user_app', '0014_alter_grupo_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='data',
            field=models.DateField(),
        ),
    ]
