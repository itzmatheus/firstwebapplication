# Generated by Django 2.0.1 on 2018-02-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome completo')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
                ('plano', models.CharField(choices=[('PL1', 'PLANO 50'), ('PL2', 'PLANO 70'), ('PL3', 'PLANO 90'), ('PL4', 'PLANO 130')], max_length=3, verbose_name='Plano')),
                ('cep', models.CharField(max_length=12, verbose_name='Cep')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=6, verbose_name='Numero da casa')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('complemento', models.CharField(max_length=100, verbose_name='Complemento')),
            ],
        ),
    ]