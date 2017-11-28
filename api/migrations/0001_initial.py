# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=50)),
                ('dtCriacao', models.DateTimeField(auto_now_add=True)),
                ('dtAlteracao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('dtCriacao', models.DateTimeField(auto_now_add=True)),
                ('dtAlteracao', models.DateTimeField(default=django.utils.timezone.now)),
                ('horaInicio', models.CharField(max_length=5)),
                ('horaFim', models.CharField(max_length=5)),
                ('idEndereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('erro', models.CharField(max_length=255)),
                ('linha', models.IntegerField()),
                ('metodo', models.CharField(max_length=100)),
                ('pagina', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('primeiroNome', models.CharField(max_length=50)),
                ('ultimoNome', models.CharField(max_length=50)),
                ('isMembro', models.BooleanField()),
                ('dtCriacao', models.DateTimeField(auto_now_add=True)),
                ('usuarioCriacao', models.IntegerField()),
                ('dtAlteracao', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuarioAlteracao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Regional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('dtCriacao', models.DateTimeField(auto_now_add=True)),
                ('dtAlteracao', models.DateTimeField(default=django.utils.timezone.now)),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regional_pessoa_responsavel', to='api.Pessoa')),
                ('usuarioAlteracao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regional_usuario_alteracao', to='api.Pessoa')),
                ('usuarioCriacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regional_usuario_criacao', to='api.Pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='idPessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_pessoa', to='api.Pessoa'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='idRegional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Regional'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='lider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_pesssoa_lide', to='api.Pessoa'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='usuarioAlteracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_usuario_alteracao', to='api.Pessoa'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='usuarioCriacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_usuario_criacao', to='api.Pessoa'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='viceLider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_pessoa_vice_lider', to='api.Pessoa'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='usuarioAlteracao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco_usuario_alteracao', to='api.Pessoa'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='usuarioCriacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco_usuario_criacao', to='api.Pessoa'),
        ),
    ]