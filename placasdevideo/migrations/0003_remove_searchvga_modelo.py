# Generated by Django 4.2 on 2023-04-15 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placasdevideo', '0002_rename_precovista_searchvga_preco_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchvga',
            name='modelo',
        ),
    ]