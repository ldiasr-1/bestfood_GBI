# Generated by Django 5.0.6 on 2024-09-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mercado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mercados', models.ManyToManyField(related_name='produtos', to='mercado.mercado')),
                ('tags', models.ManyToManyField(blank=True, to='produtos.tag')),
            ],
        ),
    ]
