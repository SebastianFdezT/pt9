# Generated by Django 4.1 on 2022-09-28 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_preguntas_acierto'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='aciertoprueba',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='acierto',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
    ]
