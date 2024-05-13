# Generated by Django 5.0.6 on 2024-05-13 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunter_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('descricao', models.CharField(max_length=70)),
                ('custo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=8)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bunter_app.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_compra', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bunter_app.cliente')),
                ('produtos', models.ManyToManyField(to='bunter_app.produto')),
            ],
        ),
    ]