# Generated by Django 4.2 on 2024-05-22 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='fecha_nac',
            field=models.DateField(blank=True, null=True),
        ),
    ]
