# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 14:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_endereco_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='dtAlteracao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='dtCriacao',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='uf',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=50, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='dtAlteracao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='dtCriacao',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='horaFim',
            field=models.CharField(max_length=5, verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='horaInicio',
            field=models.CharField(max_length=5, verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='lider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_pesssoa_lide', to='api.Pessoa', verbose_name='Líder'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='viceLider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_pessoa_vice_lider', to='api.Pessoa', verbose_name='Vice Líder'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='dtAlteracao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='regional',
            name='dtAlteracao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='regional',
            name='dtCriacao',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
