# Generated by Django 3.1.3 on 2021-03-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20210215_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='de_ferias',
            field=models.BooleanField(default=False),
        ),
    ]
