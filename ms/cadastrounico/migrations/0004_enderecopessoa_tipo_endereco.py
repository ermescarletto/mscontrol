# Generated by Django 4.0.2 on 2022-02-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrounico', '0003_enderecopessoa_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='enderecopessoa',
            name='tipo_endereco',
            field=models.CharField(choices=[('C', 'COMERCIAL'), ('R', 'RESIDENCIAL'), ('O', 'OUTROS')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
