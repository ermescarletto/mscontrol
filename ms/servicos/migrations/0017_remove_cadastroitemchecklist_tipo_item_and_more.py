# Generated by Django 4.0.2 on 2022-05-18 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicos', '0016_checklistpreenchido_foto_checklist_antes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastroitemchecklist',
            name='tipo_item',
        ),
        migrations.RemoveField(
            model_name='tiposervico',
            name='tipo_ambiente',
        ),
        migrations.AddField(
            model_name='checklistpreenchido',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
