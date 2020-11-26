# Generated by Django 3.1.3 on 2020-11-25 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.TextField(verbose_name='Modo de Preparo')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('quantidade', models.IntegerField()),
                ('validade', models.DateField()),
                ('tipo', models.CharField(choices=[('Unidade', 'Unidades'), ('Pacote', 'Pacotes'), ('Lata', 'Latas'), ('Caixa', 'Caixas'), ('Kg', 'Kg')], default='Unidade', max_length=10)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('validade',),
            },
        ),
    ]
