# Generated by Django 3.1.7 on 2023-05-24 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_auto_20230524_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='tel_per',
            field=models.CharField(max_length=30),
        ),
    ]