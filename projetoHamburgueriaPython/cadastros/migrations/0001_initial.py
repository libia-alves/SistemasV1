# Generated by Django 4.2.9 on 2024-03-07 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pratos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('valor', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_atividade', models.IntegerField(max_length=50)),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('pontos', models.CharField(max_length=50)),
                ('detalhes', models.CharField(max_length=50)),
                ('Pratos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.pratos')),
            ],
        ),
    ]
