# Generated by Django 4.0.2 on 2022-04-04 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0009_rename_tipo_item_cadastrochecklist_itens_and_more'),
        ('entidades', '0006_alter_ambiente_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoambiente',
            name='checklists_relacionados',
            field=models.ManyToManyField(to='servicos.CadastroChecklist'),
        ),
    ]
