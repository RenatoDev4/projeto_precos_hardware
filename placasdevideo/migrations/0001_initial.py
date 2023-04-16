# Generated by Django 4.2 on 2023-04-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchVGA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('url_marca', models.CharField(max_length=100)),
                ('loja', models.CharField(max_length=100)),
                ('precovista', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precoprazo', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]