# Generated by Django 4.2.2 on 2023-12-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelaoapp', '0005_mymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_table',
            name='dt_realizacao',
        ),
        migrations.RemoveField(
            model_name='form_table',
            name='livro_emplacamento',
        ),
        migrations.RemoveField(
            model_name='form_table',
            name='observacao',
        ),
        migrations.RemoveField(
            model_name='form_table',
            name='responsavel',
        ),
        migrations.AddField(
            model_name='form_table',
            name='autor_da_alimentacao',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='form_table',
            name='data',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='form_table',
            name='data_final',
            field=models.CharField(default='2023-01-01', max_length=200),
        ),
        migrations.AddField(
            model_name='form_table',
            name='data_inicial',
            field=models.CharField(default='2023-01-01', max_length=200),
        ),
        migrations.AddField(
            model_name='form_table',
            name='fonte',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='form_table',
            name='id_da_rua',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='form_table',
            name='id_ponto',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='form_table',
            name='metragem',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='form_table',
            name='numero',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='form_table',
            name='numero_original',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AlterField(
            model_name='form_table',
            name='logradouro',
            field=models.CharField(default='teste', max_length=200),
        ),
    ]