# Generated by Django 5.0.6 on 2024-07-04 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='construction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.construction')),
            ],
        ),
        migrations.CreateModel(
            name='building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('floor', models.IntegerField()),
                ('lift', models.BooleanField()),
                ('construction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.construction')),
                ('arorganizationea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.organization')),
            ],
        ),
    ]