# Generated by Django 4.2 on 2023-05-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placasdevideo', '0006_alter_searchvga_preco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchvga',
            name='preco_antigo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
