# Generated by Django 5.1.6 on 2025-02-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_produto_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
    ]
