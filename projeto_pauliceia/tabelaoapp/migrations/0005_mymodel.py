# Generated by Django 4.2.2 on 2023-07-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelaoapp', '0004_alter_form_table_dt_realizacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=200)),
                ('field2', models.CharField(max_length=200)),
            ],
        ),
    ]
