# Generated by Django 5.0.6 on 2024-05-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunter_app', '0005_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='imagens/'),
        ),
    ]
