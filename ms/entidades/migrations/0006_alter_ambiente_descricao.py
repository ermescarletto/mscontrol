# Generated by Django 4.0.2 on 2022-03-15 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0005_remove_tipoambiente_entidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambiente',
            name='descricao',
            field=models.CharField(max_length=255),
        ),
    ]
