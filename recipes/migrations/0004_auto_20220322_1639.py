# Generated by Django 3.2 on 2022-03-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20220322_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
