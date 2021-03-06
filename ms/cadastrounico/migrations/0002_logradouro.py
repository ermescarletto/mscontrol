# Generated by Django 4.0.2 on 2022-02-04 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrounico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo_logradouro', models.CharField(choices=[('RUA', 'RUA'), ('AVENIDA', 'AVENIDA'), ('TRAVESSA', 'TRAVESSA'), ('ALAMEDA', 'ALAMEDA'), ('LADEIRA', 'LADEIRA')], default='RUA', max_length=255)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrounico.cidade')),
            ],
        ),
    ]
