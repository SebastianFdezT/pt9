# Generated by Django 4.1 on 2022-09-30 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_tema_aciertotema'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='aciertoestudiante',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
    ]
