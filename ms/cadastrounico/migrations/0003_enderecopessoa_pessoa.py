# Generated by Django 4.0.2 on 2022-02-04 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrounico', '0002_logradouro'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnderecoPessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('complemento', models.CharField(max_length=255)),
                ('cep', models.PositiveIntegerField()),
                ('logradouro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrounico.logradouro')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pessoa', models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica'), ('O', 'Outra')], max_length=1)),
                ('nome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('cpfcnpj', models.CharField(max_length=14)),
                ('rg', models.PositiveIntegerField()),
                ('enderecos', models.ManyToManyField(to='cadastrounico.EnderecoPessoa')),
            ],
        ),
    ]
