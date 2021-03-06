# Generated by Django 4.0.2 on 2022-02-04 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrounico', '0005_alter_enderecopessoa_tipo_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='enderecos',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cidade',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='cadastrounico.cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='complemento',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastrounico.estado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='logradouro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastrounico.logradouro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='numero',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastrounico.pais'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EnderecoPessoa',
        ),
    ]
