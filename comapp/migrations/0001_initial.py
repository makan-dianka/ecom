# Generated by Django 3.2.8 on 2021-10-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('description', models.TextField(max_length=500)),
                ('price', models.FloatField()),
            ],
        ),
    ]
