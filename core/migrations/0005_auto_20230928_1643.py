# Generated by Django 3.2.21 on 2023-09-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_latidade_estadosbrasileiros_latitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadosbrasileiros',
            name='latitude',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='estadosbrasileiros',
            name='longitude',
            field=models.CharField(max_length=15),
        ),
    ]