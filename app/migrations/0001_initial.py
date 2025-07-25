# Generated by Django 5.2.3 on 2025-07-08 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaAtuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('setor', models.CharField(max_length=40)),
                ('site', models.CharField(max_length=40)),
                ('telefone', models.CharField(max_length=25)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nasc', models.DateField()),
                ('email', models.EmailField(max_length=15)),
                ('area_atuacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.areaatuacao')),
                ('ocupacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ocupacao')),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('requisitos', models.CharField(max_length=40)),
                ('beneficios', models.CharField(max_length=40)),
                ('area_atuacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.areaatuacao')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
                ('ocupacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ocupacao')),
            ],
        ),
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_candidatura', models.DateField()),
                ('status', models.CharField(max_length=40)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vaga')),
            ],
        ),
    ]
