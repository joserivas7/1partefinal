# Generated by Django 4.1.3 on 2022-12-15 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNueva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='año_antiguedad',
            field=models.DateField(blank=True),
        ),
    ]
