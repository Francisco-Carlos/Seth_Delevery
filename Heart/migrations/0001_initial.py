# Generated by Django 4.1.4 on 2024-03-24 15:02

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
            name='Bebidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=200)),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=100)),
                ('Img_bebbidas', models.ImageField(upload_to='Img_bebidas/%d/%m%Y')),
            ],
        ),
        migrations.CreateModel(
            name='Lanches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=200)),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=100)),
                ('Img_lanche', models.ImageField(upload_to='Img_lanche/%d/%m%Y')),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produto', models.CharField(blank=True, max_length=100)),
                ('Endereco', models.CharField(blank=True, max_length=100)),
                ('Nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
