# Generated by Django 3.2.21 on 2023-09-28 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estadosbrasileiros',
            old_name='nome_dO_estado',
            new_name='nome_do_estado',
        ),
    ]
