# Generated by Django 3.2.8 on 2021-10-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comapp', '0004_alter_produit_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
    ]