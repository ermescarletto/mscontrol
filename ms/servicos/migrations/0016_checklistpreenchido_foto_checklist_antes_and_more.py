# Generated by Django 4.0.2 on 2022-05-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0015_checklistpreenchido_data_hora_delete_checklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistpreenchido',
            name='foto_checklist_antes',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='checklistpreenchido',
            name='foto_checklist_depois',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]