# Generated by Django 4.1 on 2022-08-20 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=600)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço do produto')),
                ('imagem', models.ImageField(blank=True, max_length=250, null=True, upload_to='cosmeticos/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosmeticos.categoria')),
            ],
        ),
    ]