# Generated by Django 4.1 on 2022-10-02 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_estudiante_aciertoestudiante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntas',
            name='user',
        ),
    ]
